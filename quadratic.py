def diskriminant(a, b, c):
    diskriminant = b**2 - 4 * a * c

    if diskriminant < 0:
        return -1, diskriminant

    if diskriminant == 0:
        return 0, diskriminant

    if diskriminant > 0:
        return 1, diskriminant

def riesenie(a, b, c):

    d = diskriminant(a, b, c)

    if d[0] == -1:
        print('Rovnica nema riesenie.')

    if d[0] == 0:
        print('Rovnica ma jedno riesenie.')
        res = (-b + d[1]) / (2 * a)
        print(res)

    if d[0] == 1:
        print('Rovnica ma dve riesenia.')
        res1 = (-b + d[1]) / (2 * a)
        res2 = (-b - d[1]) / (2 * a)
        print(res1, res2)

if __name__ == '__main__':

    print('Program riesi kvadraticke rovnice.')
    a, b, c = 1, -5, 1
    riesenie(a, b, c)
