import matplotlib.pyplot as plt

pole = []
fhandle = open('show.txt')
for line in fhandle:
    pole.append(float(line.strip()))

fhandle.close()

print(pole)

plt.hist(pole, bins = 500)
plt.show()
