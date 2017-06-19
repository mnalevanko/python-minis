def even(n):
    for a in range(1, n+1):
        if (a % 2 == 0) or (a % 3 ==0):
            print(a, end = ' ')

even(17)
