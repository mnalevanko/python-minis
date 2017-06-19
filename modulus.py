def power_mod(x, y, m):
    zostatky = []
    for a in range(m):
        cislo = x**a % m
        zostatky.append(cislo)
    hladanyIndex = y % m
    
    return zostatky[hladanyIndex]

print(power_mod(11, 10, 300))
