import random

pocetHodov = 30
pocetHlav = 25
pocetPokusov = 10000

'''
Hlava na minci bude ekvivalentom nahodnej hodnoty 1.
'''


makro = []

for xxx in range(100):
    vysledky = []
    for pokus in range(pocetPokusov):
        hlava = 0
        for hod in range(pocetHodov):
            vysledok = random.randint(0,1)
            if vysledok == 1:
                hlava = hlava + 1
        vysledky.append(hlava)

    novy = [item for item in vysledky if item >= pocetHlav]
    print(len(novy))
    makro.append(len(novy))
