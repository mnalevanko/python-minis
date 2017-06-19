import pandas as pd
import numpy as np
import datetime

N = 20

df = pd.read_csv('table.csv')
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

df.drop(['Adj Close', 'Volume'], axis=1, inplace=True)
df = df.round(2)

df['TR1'] = df.High - df.Low
df['TR2'] = abs(df.High - df.Close.shift(1))
df['TR3'] = abs(df.Low - df.Close.shift(1))
df['TR'] = df[['TR1', 'TR2', 'TR3']].max(axis=1)

trs = np.array(df.TR)

atrs = np.zeros(len(trs))
#print(atrs)

atrs[N-1] = np.mean(trs[:20])

for i in range(N, len(trs)):
    atrs[i] = ((N-1) * atrs[i-1] + trs[i])/20

atrs = atrs.round(3)
print(atrs)
