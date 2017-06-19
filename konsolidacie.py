import pandas as pd
import pandas_datareader.data as web
import datetime

source = 'google'
end = datetime.datetime.today()
pocet_dni = datetime.timedelta(days=500)
start = end - pocet_dni

def is_consolidating(symbol):
    """Testing whether the stock is consolidating."""
    
    try:
        df = web.DataReader(symbol, source, start, end)
        df['52wk High'] = df.High.rolling(250).max()
        if df['52wk High'][-1] == df['52wk High'][-20]:
            return True
        else:
            return False
    except:
        print('Ticker {} nedokazem nacitat.'.format(symbol))
        return False
    
        
def main():

    filepath = 'C:/Users/Michal/Desktop/stocktest.txt'

    with open(filepath) as fhandle:
        tickers = fhandle.read()
        #print(tickers)
        
        tickers = tickers.split('\n')
        #print(tickers)

    for ticker in tickers:
        if is_consolidating(ticker):
            print(ticker)

    print('Koniec testovania.')

main()
