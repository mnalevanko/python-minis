medz = 0
znaky = 0
with open('hamlet.txt') as fhandle:
    for line in fhandle:
        medz += line.count(' ')
        znaky += len(line)

print(medz)
print('Z celkoveho poctu {} znakov zaberaju medzery presne {} %.'.format(znaky, round(medz/znaky * 100, 2)))
