import fractions

def nacitaj(zoznam):

    if len(zoznam) == 0:
        return None

    zlomky = []

    for par in zoznam:
        zlomok = fractions.Fraction(par[0], par[1])
        zlomky.append(zlomok)

    sucet = sum(zlomky)

    if sucet.denominator == 1:
        print(sucet.nominator)
    else:
        print(sucet)

nacitaj([[1, 2], [1, 3], [1, 4]])
