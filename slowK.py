print('Inicializujem knižnice.')

import pandas as pd
import pandas_datareader.data as web
import time

print('Začínam analyzovať údaje o akciách...')


def isSignal(symbol):
    
    ticker = symbol
    source = 'yahoo'
    start = '07-01-2016'
    end = '07-25-2016'

    df = web.DataReader(ticker, source, start, end).tail(13)
    high = df.High.max()
    low = df.Low.min()
    close = df.Close[-1]

    if ((close - low) / (high - low)) < 0.2:
        return True
    else:
        return False

#Nacitanie zdrojoveho suboru tickerov

#print(isSignal('TSLA'))

tickers = []

with open('C://Users//Michal//Desktop//slowK.txt') as fhandle:
    for line in fhandle:
        tickers.append(line.strip())

with open('C://Users//Michal//Desktop//slowKstocks.txt', 'w') as bubo:

    for ticker in tickers:
        time.sleep(1)
        try:
            if isSignal(ticker):
                print(ticker)
                bubo.write(ticker + '\n')
            else:
                continue

        except:
            print('Ticker {} neviem analyzovat.'.format(ticker))

print('\nKoniec programu.')
    
