import numpy as np

print('Numpy has been loaded.')

def even(n):
    if n % 2 == 0:
        return 1
    else:
        return 0

a = np.arange(10)
b = np.vectorize(even)(a)

print(b)
