import random
import matplotlib.pyplot as plt

N = 100

x = [a for a in range(N)]
y = [random.random() for uu in range(N)]

plt.scatter(x, y)
plt.show()
