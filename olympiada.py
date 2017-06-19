for a in range(1, 1001):
    for b in range(1, 1001):
        cit = a**2 + b**2
        men = a*b + 1
        if cit % men == 0:
            print('***')

            print(a, b)
            print(cit / men)
            print('***\n')

