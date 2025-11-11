from tqdm import tqdm
import time

def simulation(item):
    time.sleep(0.1)

for item in tqdm(range(100), desc="Processing"):
    simulation(item)