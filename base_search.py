import os
import pandas as pd
import pandas_datareader.data as web
import datetime
from time import sleep

os.chdir('C:\\Users\\michal.data\\Documents\\CodingProjects')

filename = 'zoznam.txt'
tickers_l = []
unique_tickers = []
with open(filename) as f:
    for line in f:
        if len(line.split()) == 1:
            #print(line.strip())
            tickers_l.append(line.strip())

from collections import Counter
tickers_d = Counter(tickers_l)
#print(tickers_d)
for k, v in tickers_d.most_common():
    unique_tickers.append(k)

end = datetime.date.today()
start = end - datetime.timedelta(days=730)

def stock_available(ticker, start, end):
    try:
        df = web.DataReader(ticker, 'google', start, end)
        return True
    except:
        return False

def is_consolidating(ticker, start, end):
    df = web.DataReader(ticker, 'google', start, end)
    if len(df) > 0:
        df['200DMA'] = df['Close'].rolling(200).mean()
        df['50DMA'] = df['Close'].rolling(50).mean()
        df['Ymin'] = df['Low'].rolling(250).min()
        df['AboveMin'] = ((df.Close - df.Ymin) / df.Ymin) * 100
        df['VolumeAvg'] = df['Volume'].rolling(50).mean()
        df['Ymax'] = df['High'].rolling(250).max()
        test1 = df['50DMA'][-1] >= df['200DMA'][-1]
        test2 = df.Close[-1] > df['50DMA'][-1]
        test3 = df['Ymax'][-1] == df['Ymax'][-21]
        test4 = df['VolumeAvg'][-1] >= 200000
        test5 = df['AboveMin'][-1] >= 40.00
        if test1 and test2 and test3 and test4 and test5:
            return True
        else:
            return False

for symbol in unique_tickers:
    sleep(1)
    #print('Checking: {}'.format(symbol))
    if stock_available(symbol, start, end):
        #print('Availability: OK')
        if is_consolidating(symbol, start, end):
            print('Konsoliduje: {}'.format(symbol))
        else:
            #print('Nekonsoliduje: {}'.format(symbol))
            pass
    else:
        print('Symbol {} not available.'.format(symbol))

