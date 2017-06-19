def myGrep(subor, hladanyText):
    fhandle = open(subor)
    for line in fhandle:
        if hladanyText in line:
            print(line.strip())

myFile = 'C:/Python35/example.txt'
myGrep(myFile, 'line')
