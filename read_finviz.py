print('Loading the modules...')
import pandas_datareader.data as web
import os
import datetime
from time import sleep

os.chdir('C:/Users/michal.data/Desktop')

def konsoliduje(symbol):
    source = 'google'
    end = datetime.date.today()
    start = end - datetime.timedelta(days=730)
    try:
        df = web.DataReader(symbol, source, start, end)
        if len(df) > 21:
            #print('Currently checking {}...'.format(symbol))
            df['Ymax'] = df['High'].rolling(250).max()
            df['BelowYmax'] = (df.Close - df.Ymax) / df.Close
            test1 = df['Ymax'][-1] == df['Ymax'][-21]
            test2 = True
            #test2 = df.Below[-1] >= -0.2
            #print(ticker, df.Below[-1])
            if all(test1, test2):
                return True
            else:
                return False
        else:
            return False
    except:
        return False

print('Starting the checking process...')
with open('finviz.txt') as fhandle:

    for line in fhandle:
        sleep(1)
        ticker = line.strip()
        if konsoliduje(ticker):
            print(ticker)
