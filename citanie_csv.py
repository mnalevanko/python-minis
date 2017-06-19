import os
import re

os.chdir(r'C:\Users\michal.data\Documents\CodingProjects')
dlzky = []
for line in open('finviz.csv'):
    #print(line.strip())
    pole = re.findall('^([0-9]+?)[|]([0-9]+?)[|]', line.strip())
    dlzky.append(len(pole))

print(set(dlzky))
