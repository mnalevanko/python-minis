import random

mena = []

for a in range(100):
    dlzka_mena = random.randint(3, 7)
    meno = ''
    for x in range(dlzka_mena):
        meno += chr(random.randint(97, 122))
    meno = meno.title()
    mena.append(meno)
