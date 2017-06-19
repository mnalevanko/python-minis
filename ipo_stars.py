from pandas_datareader import data as web
import datetime

def ipo_stars(ticker):

    df = web.DataReader(ticker, 'yahoo', start='1950/1/1')
    ipo_date = df.index[0].date()
    dnes = datetime.date.today()
    print(ipo_date)

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

print(ipo_stars('KITE'))
