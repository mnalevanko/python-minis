import random

uspesne = 0

meno = input('Ako sa voláš? ')
print('Ahoj {}. Ja som počítač a toto je hra na odčítanie.'.format(meno.title()))
print()

limit = 30

spravne = 0

for abc in range(10):
    a = random.randint(1, limit)
    b = random.randint(0, a)
    vysledok = a - b
    message = str(a) + ' - ' + str(b) + ' = '
    odpoved = int(input(message))

    if odpoved == vysledok:
        print('Výborne! Si dobrý, {}.\n'.format(meno.title()))
        spravne += 1
        print('*'*spravne)
    else:
        print('To nie, urobil si chybu. Ale nevadí.\n')

print('Koniec hry, {}!'.format(meno.title()))
print('Z 10 príkladov si správne vypočítal {}'.format(spravne) )
