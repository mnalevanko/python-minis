import numpy as np

file_path = 'C://Users//Michal//Desktop//faktury.txt'

with open(file_path) as fhandle:
    pole = fhandle.read()
    print(pole)
