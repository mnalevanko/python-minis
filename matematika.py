import random

uspesne = 0

meno = input('Ako sa voláš? ')
print('Ahoj {}. Ja som počítač a budem sa s tebou hrať s číslami.'.format(meno.title()))
print()

limit = 20
pocet_prikladov = 10

spravne = 0

for abc in range(pocet_prikladov):
    a = random.randint(1, limit)
    b = random.randint(1, limit)
    sucet = a + b
    message = str(a) + ' + ' + str(b) + ' = '
    odpoved = int(input(message))

    if odpoved == sucet:
        print('Výborne! Si dobrý, {}.'.format(meno.title()))
        spravne += 1
        print('*'*spravne + '\n')
    else:
        print('To nie, urobil si chybu. Ale nevadí.')

print('Koniec hry, {}!'.format(meno.title()))
print('Z {} príkladov si správne vypočítal {}.'.format(pocet_prikladov, spravne) )

