import random

cisla = [random.randint(10, 10000) for a in range(1975)]

with open('datatest.csv', 'w') as fhandle:
    for cislo in cisla:
        fhandle.write(str(cislo) + '\n')
