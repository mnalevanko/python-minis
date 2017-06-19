import pandas as pd
#import re

def number_of_stocks(url):
    '''Returns the total number of stocks for given screen's URL.'''

    df_temp = pd.read_html(url)
    total = int(df_temp[9][0].str.split()[0][1]) # Reads the number behind "Total: "
    return total


def symbols_from_url(url):
    '''Returns a list of stocks from a single Finviz page.'''

    df = pd.read_html(url)
    stocks = list(df[10][1])[1:]
    return stocks


def get_all_symbols(url):
    '''Returns a list of all stock tickers from given screener.'''

    total = number_of_stocks(url)
    counter = 1
    stocks = []

    while counter <= total:
        appendix = '&r=' + str(counter) if counter > 1 else ''
        path = url + appendix
        #print(path)
        stocks += symbols_from_url(path)
        #print(stocks)
        counter += 20

    return stocks

##print('Test:')
##url = 'http://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_avgvol_o100,sh_price_o10,ta_highlow52w_a40h,ta_sma200_sb50,ta_sma50_pa&ft=3'
##print(get_all_symbols(url))

url = 'http://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_avgvol_o100,sh_price_o10,ta_highlow52w_a40h,ta_sma200_sb50,ta_sma50_pa&ft=3'

print(get_all_symbols(url))
