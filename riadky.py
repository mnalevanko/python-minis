import os

cesta = 'C:/Users/michal.data/Desktop/zoznam.txt'
folder = 'C:/Users/michal.data/Desktop/Akcie/'

existujuce_subory = []

for current_folder, subfolders, file_names in os.walk(folder):
    for file_name in file_names:
        #print(os.path.join(current_folder, file_name))
        existujuce_subory.append(os.path.join(current_folder, file_name))

for subor in existujuce_subory:
    os.remove(subor)
