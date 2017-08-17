from tqdm import tqdm
from time import sleep

for x in tqdm(range(100), 'Main Loop'):
    for y in tqdm(range(10), 'Second loop'):
        for z in tqdm(range(5), 'Third loop'):
            sleep(0.1)
