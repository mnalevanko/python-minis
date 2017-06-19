from copy_finviz import *
import time
from pandas_datareader import data as web

url = 'http://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_avgvol_o50,sh_price_o5,ta_sma200_sb50,ta_sma50_pa&ft=3'
print('Retrieving all symbols...')
stocks_to_check = get_all_symbols(url)
fails = 0
failed_tickers = []

def get_ipo_year(symbol):
    try:
        df = web.DataReader(symbol, 'google')
##        ipo_year = df.index[0].year
        return len(df)
    except:
        global fails
        global failed_tickers
        fails += 1
        failed_tickers.append(symbol)
        return 'N/A'

print('Retrieving IPO dates...')
start = time.time()
for idx, stock in enumerate(stocks_to_check):
    print('Ticker #{}: {}\tIPO: {}'.format(idx + 1, stock, get_ipo_year(stock)))

end = time.time()
print('Time needed: {:2f} seconds'.format(end - start))
print('Number of failed attempts: {}'.format(fails))
print('These tickers failed:')
for item in failed_tickers:
    print(item, end=' ')
