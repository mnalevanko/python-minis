def average():
    veta = input('Enter a sentence: ')
    slova = veta.split()
    pocet_slov = len(slova)

    count = 0
    for slovo in slova:
        count += len(slovo)

    return count/pocet_slov

print(average())
