import itertools
import pikepdf
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse

def generate_passwords(chars, min_len, max_len):
    start_time = time.time()
    for length in range(min_len,max_len+1):
        if(time.time()-start_time>15):
            raise KeyboardInterrupt
        
        for password in itertools.product(chars,repeat=length):
            yield ''.join(password)

def load_wordlist(wordlist_file):
    with open("wordlist.txt",'r') as file:
        for line in file:
            yield line.strip()

def try_password(pdf_file,password):
    try:
        with pikepdf.open(pdf_file,password=password) as file:
            print(f"[+] Password found {password}")
            return password
    except pikepdf._core.PasswordError:
        return None
    
def decrypt_pdf(pdf_file, passwords, total_passwords, max_workers=4):
    with tqdm(total=total_passwords, desc="Decrypting PDF", unit='password') as pbar:
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_passwords = {executor.submit(try_password,pdf_file,pwd):pwd for pwd in passwords}

            for future in tqdm(future_to_passwords,total=total_passwords):
                password = future_to_passwords[future]
                if future.result():
                    return future.result()
                pbar.update(1)
    print("Unable to succeed")
    return None