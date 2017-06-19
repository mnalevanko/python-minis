import pyperclip
import string
from time import sleep

while True:
    retazec = pyperclip.paste()
    new_retazec = ''
    for char in retazec:
        if char in string.ascii_letters or char in string.digits:
            new_retazec += char
        elif char == '.':
            new_retazec += '_'
        elif char == ' ':
            new_retazec += ' '
        else:
            pass

    pyperclip.copy(new_retazec)
    sleep(1)
