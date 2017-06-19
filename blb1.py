def three_words(words):
    pole = words.split()
    #print(pole)
    pole_1_0 = [0 if item.isnumeric() else 1 for item in pole]
    if len(pole) < 3:
        return False
    else:
        for indx in range(len(pole)-2):
            suma = sum(pole_1_0[indx:indx+3])
            #print(suma)
            if suma == 3:
                return True
    return False

print(three_words('Volam sa 54 26 a byvam v Medzibrode, Za mlynom 34.'))
