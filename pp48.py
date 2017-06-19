def words(subor):
    fhandle = open(subor)
    content = fhandle.read()
    fhandle.close()

    table = content.maketrans('!,.:;?', 6 * ' ')
    content = content.translate(table)
    content = content.lower()
    return content.split()

print(words('C:/Python35/example.txt'))
