veta = 'Moje meno je Michal Nalevanko.'

pismena = dict()

for char in veta.lower():
    if 'a' <= char <= 'z':
        pismena[char] = pismena.get(char, 0) + 1

dvojice = []

for (k, v) in pismena.items():
    dvojice.append((v, k))

sorted(dvojice, reverse=True)

print(dvojice[0])
        
