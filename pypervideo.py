import pyperclip

retazec = ''

def uprav(ret):
    new_ret = ''
    for c in ret:
        if c in ['.', ',']:
            c = '_'
        elif c in [':']:
            c = ''
        new_ret += c
    return new_ret

#print(pyperclip.copy())


while True:
    if pyperclip.paste() != retazec:
        retazec = pyperclip.paste()
        pyperclip.copy(retazec)
       
