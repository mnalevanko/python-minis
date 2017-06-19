def priemer(*hodnoty):
    sucet = sum(hodnoty)
    print('Sucet je: {}.'.format(sucet))
    pocet = len(hodnoty)
    print('Pocet je {}.'.format(pocet))
    avg = sucet / pocet
    return avg

#pole = [1, 3, 5, 4, 2, 2]
print(priemer(1, 3, 5, 4, 2, 2, 8))
