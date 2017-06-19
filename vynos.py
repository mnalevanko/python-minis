rocny_urok = 1.01
mesacny_urok = rocny_urok**(1/12)

pocet_rokov = 5
pocet_mesiacov = pocet_rokov * 12

mesacna_investicia = 146

nasporene = []

for a in range(pocet_mesiacov+1, -1, -1):
    print(a)
    nasporene.append(mesacna_investicia * (mesacny_urok**(a/12)))

print(sum(nasporene))
