def lcm(*args):

    if 0 in args:
        return 0

    maximum = max(args)
    mozny_nasobok = 0

    while True:
        vyskyt = 0
        mozny_nasobok += maximum
        for a in args:
            if mozny_nasobok % == 0:
                vyskyt += 1
