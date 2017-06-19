ibd_akcie = []
finviz_akcie = []

with open('C:/Users/michal.data/Desktop/zoznam.txt') as fhandle:
    for line in fhandle:
        try:
            line = line.split()
            if len(line) == 1:
                ibd_akcie.append(line[0])
        except:
            pass

#print(len(set(ibd_akcie)))

with open('C:/Users/michal.data/Desktop/finviz.txt') as fhandle:
    for line in fhandle:
        finviz_akcie.append(line.strip())

tickers = set(ibd_akcie).intersection(set(finviz_akcie))

print(len(tickers))

with open('C:/Users/michal.data/Desktop/prienik.txt', 'w') as f:
    for ticker in tickers:
        f.write(str(f) + '\n')
