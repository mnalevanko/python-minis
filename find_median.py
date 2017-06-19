import random

def find_median(pole):
    pole.sort()
    if len(pole) == 1:
        return pole[0]

    elif len(pole) == 2:
        return (pole[0] + pole[1]) / 2

    else:
        del pole[0]
        del pole [-1]
        return find_median(pole)

zoznam = [random.randint(1, 500) for x in range(10000)]
zoznam1 = zoznam.copy()
#zoznam = [1, 3, 5, 8]

print(find_median(zoznam1))
