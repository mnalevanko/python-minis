def z_score(value, mean, std):
    '''Calculates the z-score for given value, mean and standard deviation.'''

    result = (value - mean) / std
    return result

priemer = 120
st = 40

hodnoty = [205, 137, 20, 90]

for udaj in hodnoty:
    print(z_score(udaj, priemer, st))
