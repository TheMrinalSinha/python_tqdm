from tqdm import tqdm
from time import sleep

for x in tqdm(range(100), 'PROGRESS'):
    sleep(0.1)
