# Kde sa subor s datami nachadza?
file_path = 'C:/Users/michal.data/Desktop/zoznam.txt'

rubriky = []

with open(file_path) as f:
    for line in f:
        if len(line.split()) > 1:
            rubriky.append(line)

# Teraz uz mam v premennej 'rubriky' mena vsetkych rubrik, t.j. pouzitych watchlistov

with open(file_path, 'w') as f:
    for item in rubriky:
        f.write(item + '\n')

print('Koniec programu.')
