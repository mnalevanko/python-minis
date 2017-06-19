import random

cislo_list = []
for a in range(1000000):
    nahoda = random.randint(1, 9)
    cislo_list.append(str(nahoda))

velke_cislo = ''.join(cislo_list)

with open('velke_num.txt', 'w') as f:
    f.write(velke_cislo)
