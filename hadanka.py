mozne = []

for a in range(72):
    for b in range(72):
        for c in range(72):
            if a * b * c > 72:
                continue
            if a * b * c == 72:
                mozne.append((a+b+c,(a, b, c)))

#print(mozne)
    
sucty = []

for item in mozne:
    if item[1][0] == item[1][1]:
        print(item)
