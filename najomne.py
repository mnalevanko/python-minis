import random
import numpy as np

def prveMinimum(zoznam):
    return min(zoznam[:20])

def druheMinimum(zoznam):
    najdene = zoznam[20]
    for cena in zoznam[21:]:
        if cena < najdene:
            najdene = cena
            break
    return najdene
    

#ceny = [random.randint(400, 900) for x in range(60)]

uspech_list = []
n = 1000
for r in range(100):
    uspech = 0
    for a in range(n):
        ceny = [random.randint(400, 900) for x in range(60)]
    #    random.shuffle(ceny)
        if prveMinimum(ceny) > druheMinimum(ceny):
            uspech += 1

    print('Urobil som celkovo {} pokusov.'.format(n))
    print('Strategia bola uspesna v {} pripadoch.'.format(uspech))
    uspech_list.append(uspech)
    
print(np.array(uspech_list).mean())
print(np.array(uspech_list).std())
