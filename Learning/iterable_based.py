from tqdm import *
from time import sleep

# Wrap TQDM around any iterable.
text = ""
for char in tqdm(["a", "b", "c", "d"]):
    text = text + char

# trange(i) is a special optimised instance of tqdm(range(i)):
for i in trange(10000000):
    pass

# Instantiation outside of the loop allows for manual control over tqdm():
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)
    sleep(0.5)

# Manual control on tqdm() updates by using a with statement:
with tqdm(total=100) as pbar:
    for i in range(10):
        pbar.update(10)
        sleep(0.5)

# If the optional variable total (or an iterable with len()) is provided, predictive stats are displayed.
#
# with is also optional (you can just assign tqdm() to a variable, but in this case don’t forget to del or close() at the end:
pbar = tqdm(total=100)
for i in range(10):
    pbar.update(10)
    sleep(0.5)
pbar.close()
