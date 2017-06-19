print('Importing modules...')

import pandas as pd
import pandas_datareader.data as web
import datetime
import time

print('Modules successfuly imported.')

end = datetime.datetime.today()
delta = datetime.timedelta(days=370)
start = end - delta

zoznam = []

with open('C:\\Users\\Michal\\Desktop\\stocksinbase.txt') as fhandle:
    for line in fhandle:
        zoznam.append(line + '\n')


def isConsolidating(tickers):
    for ticker in tickers:
        time.sleep(1)
        try:              
            
            df = web.DataReader(ticker, 'google', start, end)
            df['25dh'] = df.High.rolling(25).max()
            #print(ticker.strip())
            #print(df.iloc[-1]['50dh'])
            #print(df.iloc[-50]['50dh']) 
            if df.iloc[-1]['25dh'] == df.iloc[-25]['25dh']:
                print(ticker.strip())
        except:
            print('Ticker {} nedokazem posudit.'.format(ticker.strip()))

isConsolidating(zoznam)
