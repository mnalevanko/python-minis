import pandas as pd
import pandas_datareader.data as web
import numpy as np
import datetime

def getATR(ticker, N=20, precision=3, source='yahoo'):
    '''Calculates the average true range for a given stock symbol and a period (in days).'''

    start=datetime.date.today()-datetime.timedelta(int(N*10))
    end=datetime.date.today()

    df = web.DataReader(ticker, source, start, end)
    
    df = df.round(2)
    df['TR1'] = df.High - df.Low
    df['TR2'] = abs(df.High - df.Close.shift())
    df['TR3'] = abs(df.Low - df.Close.shift())
    df['TR'] = df[['TR1', 'TR2', 'TR3']].max(axis=1)

    trs = np.array(df.TR)
    atrs = np.zeros(len(trs))
    atrs[N-1] = np.mean(trs[:N])

    for i in range(N, len(trs)):
        atrs[i] = ((N-1) * atrs[i-1] + trs[i])/N

    atrs = atrs.round(precision)

    return atrs[-1]

if __name__ == '__main__':
    print(getATR('MSFT'))
