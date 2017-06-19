import numpy as np
import matplotlib.pyplot as plt

simulations = 10000
avg_return = 0.1
std = 0.1
size = 20 #pocet rokov investovania

final = []

for i in range(simulations):
    returns = np.random.normal(avg_return, std, size)
    returns_cum = np.cumsum(returns)
    final.append(returns_cum[-1])
    plt.plot(final)

print('Vykonal som {} simulacii a toto su moje vysledky:'.format(simulations))
maxim = np.max(final)
minim = np.min(final)
negat = len([x for x in final if x <= 0])
priemer = np.mean(final)
stdeviation = np.std(final)

print('Maximalna hodnota: {}'.format(maxim))
print('Minimalna hodnota: {}'.format(minim))
print('Pocet negativnych vysledkov: {}'.format(negat))
print('Priemerna hodnota: {}'.format(priemer))
print('Standardna odchylka: {}'.format(stdeviation))

plt.show()
