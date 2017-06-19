import random

def hodKockou():
    a = random.randint(1, 6)
    b = random.randint(1, 6)

    if a < b:
        return True
    else:
        return False

pocetVyhier = 0

for x in range(10):
    
    kapital = 100
    stavka = 1

    for a in range(10):
        if hodKockou():
            kapital += 1
        else:
            kapital -= 1

    if kapital > 100:
        pocetVyhier += 1

    print(kapital)

print(pocetVyhier)
