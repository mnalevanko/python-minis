#!/usr/bin/env python3

from pandas_datareader import data as web
import datetime

df_g = web.DataReader('AAPL', 'google')
df_y = web.DataReader('AAPL', 'yahoo')
now = datetime.datetime.now()

#print(now)

print('\nTime of the check: {}'.format(now))
print('Google {}'.format(df_g.index[-1]))
print('Yahoo {}'.format(df_y.index[-1]))

with open('tracking_stocks.txt', 'a') as f:
    f.write('\nTime of the check: {}'.format(now))
    f.write('Google {}'.format(df_g.index[-1]))
    f.write('Yahoo {}'.format(df_y.index[-1]))