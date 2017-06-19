import pyperclip
import datetime

nazov = input('Ako chces nazvat novy subor? ')
nazov_suboru = nazov + '.txt'

schranka = ''

while True:
    obsah = pyperclip.paste()
    if obsah != schranka:
        with open(nazov_suboru, 'a') as fhandle:
            fhandle.write(str(pyperclip.copy(obsah)))
    else:
        pass
            
