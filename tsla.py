import pandas as pd
#import pandas.io.data as web
import pandas_datareader.data as web
import numpy as np


def adjustedVolume(change, volume):
    if change < 0:
        return volume
    else:
        return 0

source = 'google'

start = '1/1/2016'
end = '7/6/2016'

def isPocketPivot(symbol):
    df = web.DataReader(symbol, source, start, end)

    #df['50DMA'] = df['Close'].rolling(50).mean()
    df['Difference'] = df['Close'].diff()

    df['Adjusted volume'] = list(map(adjustedVolume, df['Difference'], df['Volume']))

    #print(df['Adjusted volume'].tail(11))
    last_volume = df['Volume'][-1]
    checking_volume = df['Adjusted volume'][-11:-1].max()

    if last_volume > checking_volume:
        return True
    else:
        return False


df1 = pd.read_csv('C://Users//Michal//Desktop//stocksup.txt', header = None)
df1 = list(df1[0])

for item in df1:
    if isPocketPivot(item):
        print(item)
