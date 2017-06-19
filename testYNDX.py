import datetime
from pandas_datareader import data as web

DNES = datetime.date.today()
PRED_ROKOM = datetime.date(DNES.year - 1, DNES.month, DNES.day)
SP500 = web.DataReader('^GSPC', 'yahoo', PRED_ROKOM, DNES)

def rs_percentage(ticker):
    df = web.DataReader(ticker, 'google', PRED_ROKOM, DNES)
    # if df.index[-1].date != SP500.index[-1].date():
    #     return 'N/A'
    #print(df.head())
    #print(df.tail())
    rsl = df['Close'] / SP500['Adj Close']
    total_range = rsl.max() - rsl.min()
    rs_percentage = (rsl[-1] - rsl.min()) / total_range * 100
    rs_percentage = round(rs_percentage, 2)
    #print('{:10}{}'.format(ticker, rs_percentage))
    return rs_percentage

print(rs_percentage('GTN'))
