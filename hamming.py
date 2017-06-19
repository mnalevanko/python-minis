def hamming(n):
        
    import math

    pole = []

    for a in range(0, n):
        for b in range(0, n):
            for c in range(0, n):
                cislo = 2**a * 3**b * 5**c
                pole.append((cislo, (a, b, c)))
    pole.sort()
    print(pole)
    return pole[n-1][0]

print(hamming(18))
