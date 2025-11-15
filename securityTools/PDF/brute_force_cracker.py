import itertools
import string
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
    
# def decrypt_pdf(pdf_file, passwords, total_passwords, max_workers=4):
#     with tqdm(total=total_passwords, desc="Decrypting PDF", unit='password') as pbar:
#         with ThreadPoolExecutor(max_workers=max_workers) as executor:
#             future_to_password = {executor.submit(try_password,pdf_file,pwd):pwd for pwd in passwords}

#             for future in tqdm(future_to_password,total=total_passwords):
#                 password = future_to_password[future]
#                 if future.result():
#                     return future.result()
#                 pbar.update(1)
#     print("Unable to succeed")
#     return None


def decrypt_pdf(pdf_file, passwords, total_passwords, max_workers=4):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(try_password, pdf_file, pwd): pwd for pwd in passwords}

        for future in tqdm(as_completed(futures), total=total_passwords, desc="Decrypting PDF"):
            result = future.result()
            if result:
                return result
    print("Unable to succeed")
    return None


if __name__== '__main__':
    
    parser = argparse.ArgumentParser(description="Decrypt a password protected PDF file")
    parser.add_argument("pdf_file",help="Path to password protected PDF file")
    parser.add_argument("-w", "--wordlist", help="Path to password list file",default=None)
    parser.add_argument("-g","--generate", action="store_true",help="Generate passwords")
    parser.add_argument("-min", "--min-length",type=int, help="Minimum length of password to generate",default=1)
    parser.add_argument("-max","--max-length",type=int,help="Max length of password",default=5)
    parser.add_argument("-c","--charset",type=str, help="Characters in use for password generation",default=string.ascii_letters + string.digits + string.punctuation)
    parser.add_argument("--max_workers",type=int, help="Max # of workers of threads", default=4)
    args = parser.parse_args()

    if args.generate:
        passwords = generate_passwords(args.charset, args.min_length, args.max_length)
        total_passwords = sum(1 for _ in generate_passwords(args.charset, args.min_length, args.max_length))
    elif args.wordlist:
        passwords = load_wordlist(args.wordlist)
        total_passwords = sum(1 for _ in load_wordlist(args.wordlist))
    else:
        print("Either --wordlist must be provided or --generate must be specified")
        exit(1)
    decrypted_password = decrypt_pdf(args.pdf_file, passwords, total_passwords,args.max_workers)

    if decrypted_password:
        print(f"PDF Decrypted, password is: {decrypted_password}")
    else:
        print("Unsuccessful to decrypt PDF. Password not found")