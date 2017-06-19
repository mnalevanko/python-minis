import pandas as pd
import datetime
from pandas_datareader import data as web

def n_years_into_days(n):
    '''Turns a number of years into number of records in trading statistics.'''

    today = datetime.date.today()
    year_today = today.year
    start_date = datetime.date(today.year - n, today.month, today.day)

    sp500_df = web.DataReader('^GSPC', data_source='yahoo', start=start_date, end=today)

    return len(sp500_df)

DNES = datetime.date.today()
PRED_ROKOM = DNES - datetime.timedelta(days=n_years_into_days(1))
SP500 = web.DataReader('^GSPC', 'yahoo', PRED_ROKOM, DNES)

def rs_percentage(ticker):
    df = web.DataReader(ticker, 'google', PRED_ROKOM, DNES)
    rsl = df['Close'] / SP500['Adj Close']
    total_range = rsl.max() - rsl.min()
    result = (rsl[-1] - rsl.min()) / total_range * 100
    result = round(rs_percentage, 2)
    #print('{:10}{}'.format(ticker, rs_percentage))
    return result

print(rs_percentage('TSLA'))
