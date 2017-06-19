f = open('C:/Users/michal.data/Desktop/zoznam.txt')
for line in f:
    try:
        #line = line.strip()
        #if len(line) == 1 and line[0] == 'Z':
        print(line)
    except:
        pass
