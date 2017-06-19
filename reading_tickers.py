file_path = r'C:\Users\michal.data\Desktop\zoznam.txt'

d = {}

with open(file_path) as fhandle:
    for line in fhandle:
        line = line.strip()
        line_list = line.split()
        
        if line_list:
            if len(line_list) > 1:
                group = ' '.join(line_list)
                #print(group)
                
            if line_list[0] in d:
                d[line_list[0]].append(group)
            
            else:
                d[line_list[0]] = [group]
                
print(d)