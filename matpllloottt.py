import matplotlib.pyplot as plt
import random

year = [i for i in range(1970, 2016)]
value = [random.randint(1, 5) for a in range(46)]

plt.plot(year, value)
plt.show()
