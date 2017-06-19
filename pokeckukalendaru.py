import calendar
ciel = 'C:/Users/Michal/Desktop/pokec.txt'

zoznam =  dir(calendar)
'''
for item in zoznam:
    a = (help('calendar.' + item))
    print(item)

'''
with open(ciel, 'a') as fhandle:
    for item in zoznam:
        fhandle.write(help('calendar.' + item))
        #fhandle.write('\n' * 21)
