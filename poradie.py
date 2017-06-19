def month(n):
    mesiace = 'JanFebMarAprMayJunJulAugSepOctNovDec'
    index = n-1
    return mesiace[index*3:index*3+3]

print(month(9))
