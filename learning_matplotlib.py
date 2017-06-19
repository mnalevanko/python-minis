from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style

df = web.DataReader('AAPL', 'google')

ax1 = plt.subplot2grid((3,1), (0,0), colspan=1, rowspan=2)
ax2 = plt.subplot2grid((3,1), (2,0), colspan=1, rowspan=1, sharex=ax1)

ax1.plot(df.index, df['Close'])
ax2.bar(df.index, df['Volume'])

plt.show()
