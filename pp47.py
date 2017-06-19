def stringCount(filename, text):
    fhandle = open(filename)
    content = fhandle.read()
    count = content.count(text)
    fhandle.close()

    return count

subor = 'C:/Python35/example.txt'
print(stringCount(subor, 'line'))
