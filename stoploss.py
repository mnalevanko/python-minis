# Program na výpočet úrovní stop loss príkazov

while True:

    print('\nPre koľko pozícií chceš počítať stop loss? (1, 2, "q")')
    pokyn = input()
    if pokyn == '1':
        pocet = int(input('\nZadaj pocet kupenych akcii: '))
        cena = float(input('Zadaj nakupnu cenu: '))
        sl = ((pocet * cena + 1)/pocet) * 0.97
        print('Tvoj stop loss je na úrovni', round(sl, 4))

    elif pokyn == '2':
        pocet1 = int(input('\nZadaj velkost prvej pozicie: '))
        cena1 = float(input('Zadaj nakupnu cenu: '))
        pocet2 = int(input('\nZadaj velkost druhej pozicie: '))
        cena2 = float(input('Zadaj nakupnu cenu: '))
        sl = ((pocet1 * cena1 + pocet2 * cena2 + 2)/(pocet1 + pocet2))*0.93
        print('Tvoj stop loss je na úrovni', round(sl, 4))

    elif pokyn == 'q':
        break

print('Ďakujem za využitie tohto programu.')
