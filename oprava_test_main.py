import pandas as pd
import datetime
from pandas_datareader import data as web
import smtplib
import random
import sys

# def n_years_into_days(n):
#     '''Turns a number of years into number of records in trading statistics.'''
#
#     today = datetime.date.today()
#     year_today = today.year
#     start_date = datetime.date(today.year - n, today.month, today.day)
#
#     sp500_df = web.DataReader('^GSPC', data_source='yahoo', start=start_date, end=today)
#
#     return len(sp500_df)


DNES = datetime.date.today()
PRED_ROKOM = datetime.date(DNES.year - 1, DNES.month, DNES.day)
SP500 = web.DataReader('^GSPC', 'yahoo', PRED_ROKOM, DNES)
TAIL_DATE = SP500.index[-1]

def is_working_day(dnes):
    holidays = [datetime.date(2017, 5, 29), datetime.date(2017, 9, 4), datetime.date(2017, 12, 25)]

    if 0 <= dnes.weekday() <= 4 and dnes not in holidays:
        return True
    return False

if not is_working_day(DNES):
    sys.exit()


def number_of_stocks(url):
    '''Returns the total number of stocks for given screen's URL.'''

    df_temp = pd.read_html(url)
    total = int(df_temp[9][0].str.split()[0][1]) # Reads the number behind "Total: "
    print('Total number of stocks:', total)
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
        print(path)
        stocks += symbols_from_url(path)
        counter += 20

    return stocks


def rs_percentage(ticker):
    df = web.DataReader(ticker, 'google', PRED_ROKOM, DNES)
    # if df.index[-1].date != SP500.index[-1].date():
    #     return 'N/A'
    #print(df.head())
    #print(df.tail())
    rsl = df['Close'] / SP500['Adj Close']
    total_range = rsl.max() - rsl.min()
    rs_percentage = (rsl[-1] - rsl.min()) / total_range * 100
    #rs_percentage = round(rs_percentage, 2)
    #print('{:10}{}'.format(ticker, rs_percentage))
    return round(rs_percentage, 2)

def stocks_with_required_rsl(zoznam_akcii, threshold=80):
    vyhovuje = []
    for symbol in zoznam_akcii:
        try:
            level = rs_percentage(symbol)
            if level >= threshold:
                vyhovuje.append((level, symbol))
        except:
            pass

    return sorted(vyhovuje, reverse=True)

def is_consolidating(stock, days=25):
    df = web.DataReader(stock, 'google')
    #print(stock, len(df))
    df['Ymax'] = df['High'].rolling(250).max()
    try:
        if df['Ymax'][-1] == df['Ymax'][-days]:
            return True
        return False
    except:
        return False

def ipo_stars(ticker):

    df = web.DataReader(ticker, 'yahoo', start='1950/1/1')
    ipo_date = df.index[0].date()
    dnes = datetime.date.today()
    #print(ipo_date)

    if ipo_date < datetime.date(dnes.year - 5, dnes.month, dnes.day):
        return ''

    if ipo_date >= datetime.date(dnes.year - 1, dnes.month, dnes.day):
        return '*'

    if ipo_date >= datetime.date(dnes.year - 2, dnes.month, dnes.day):
        return '**'

    if ipo_date >= datetime.date(dnes.year - 3, dnes.month, dnes.day):
        return '***'

    if ipo_date >= datetime.date(dnes.year - 4, dnes.month, dnes.day):
        return '****'

    if ipo_date >= datetime.date(dnes.year - 5, dnes.month, dnes.day):
        return '*****'


url = 'http://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_avgvol_o200,sh_price_o10,ta_highlow52w_a40h,ta_sma200_sb50,ta_sma50_pa&ft=3'
tickers = get_all_symbols(url)
print(tickers)
print('All tickers acquired. Starting the check...')
random.shuffle(tickers)
tickers_alt = tickers

stocks_with_sufficient_rsl = stocks_with_required_rsl(tickers_alt)

final_list = []

for item in stocks_with_sufficient_rsl:
    if is_consolidating(item[1]):
        final_list.append((item[1], item[0]))

pocet_akcii = len(final_list)
print('Printing the final list', final_list)
