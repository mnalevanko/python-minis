import random
import numpy as np
from prettytable import PrettyTable

pocet_tankov = 150
pole_np = np.arange(1, pocet_tankov + 1)
random.shuffle(pole_np)
pocet_pokusov = 1000
means = []
stds = []

for a in range(pocet_pokusov):
    priemer = np.array(pole_np[:4]).mean()

    means.append(np.array(pole_np[:4]).mean())
    stds.append(np.array(pole_np[:4]).std(ddof = 1))
    random.shuffle(pole_np)

print(np.array(means).mean())
print(np.array(stds).std())

