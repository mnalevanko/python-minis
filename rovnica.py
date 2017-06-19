def riesenie(a, b, c, d):
    if a - b == 9:
        if c - d == 14:
            if a + c == 12:
                if b + d == 2:
                    print(a, b, c, d)

for a in range(-100, 100):
    for b in range(-100, 100):
        for c in range(-100, 100):
            for d in range(-100, 100):
                riesenie(a, b, c, d)
                
