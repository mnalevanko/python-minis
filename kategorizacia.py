from collections import Counter

path_to_file = 'C:/Users/michal.data/Desktop/zoznam.txt'
d = dict()

for line in open(path_to_file):
    line = line.strip()
    line_l = line.split()
    if len(line_l) > 1:
        #print(line)
        #print('Creating a dictionary with the index of {}.'.format(line))
        d[line] = []
        
for line in open(path_to_file):
    line = line.strip()
    line_l = line.split()
    if len(line_l) > 1:
        label = line
    if len(line_l) == 1:
        d[label].append(line)

tickers_l = [] # Zoznam vsetkych tickerov v subore

for line in open(path_to_file):
    line = line.strip()
    line_l = line.split()
    if len(line_l) == 1:
        tickers_l.append(line)

#print(tickers_l)

tickers_d = Counter(tickers_l)
unique_tickers = []

for (k, v) in tickers_d.most_common():
    unique_tickers.append(k)

def kde_je_ticker(symbol):
    kde_je = []
    for key in d.keys():
        if symbol in d[key]:
            kde_je.append(key)
    vysledok = (', ').join(kde_je)
    return vysledok

print(kde_je_ticker('POLA'))
