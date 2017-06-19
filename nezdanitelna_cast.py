import numpy as np
import matplotlib.pyplot as plt

def nezdanitelna_cast(zaklad):
    if zaklad <= 19809:
        return 3803.33
    else:
        return 8755.578 - (zaklad / 4)

prijem = np.arange(500, 100000, 100)
dane = [nezdanitelna_cast(suma) for suma in prijem]
plt.plot(prijem, dane)
plt.show()
