from pandas_datareader import data as web
import numpy as np
import datetime

class Stock():
    '''A simple representation of a stock.'''

    def __init__(self, ticker):
        self.ticker = ticker
        try:
            self.df = web.DataReader(ticker, data_source='google')
        except:
            self.df = None

    @property
    def ipo_date(self):
        return self.df.index[0]

    @property
    def ipo_stars(self):

        date = datetime.date(self.df.index[0].year, self.df.index[0].month, self.df.index[0].day)

        if date < PRED_PIATIMI_ROKMI:
            return ''

        if date >= datetime.date(DNES.year - 1, DNES.month, DNES.day):
            return '*'

        if date >= datetime.date(DNES.year - 2, DNES.month, DNES.day):
            return '**'

        if date >= datetime.date(DNES.year - 3, DNES.month, DNES.day):
            return '***'

        if date >= datetime.date(DNES.year - 4, DNES.month, DNES.day):
            return '****'

        if date >= datetime.date(DNES.year - 5, DNES.month, DNES.day):
            return '*****'

    @property
    def is_consolidating(self, days=25):

        self.df['52Wk High'] = self.df['High'].rolling(250).max()

        try:
            if self.df['52Wk High'][-1] == self.df['52Wk High'][-days]:
                return True
            else:
                return False
        except:
            return False

    @property
    def rs_line_np(self):

        if len(self.df) >= DF_LENGTH:
            df_1y = self.df['Close'][-DF_LENGTH:]
            rsl_np = np.array(df_1y) / np.array(sp_df['Close'][-DF_LENGTH:])
            return rsl_np

        else:
            dlzka = len(self.df)
            df_1y = self.df['Close'][-dlzka:]
            rsl_np = np.array(df_1y) / np.array(sp_df['Close'][-dlzka:])
            return rsl_np

    @property
    def rs_range(self):
        return self.rs_line_np.max() - self.rs_line_np.min()

    @property
    def rs_line_percentage(self):
        citatel = self.rs_line_np[-1] - self.rs_line_np.min()
        menovatel = self.rs_range
        percentage = round(citatel / menovatel * 100, 2)
        return percentage

    @property
    def meets_the_threshold(self, threshold=80):

        if self.rs_line_percentage >= threshold:
            return True
        else:
            return False

tickers = ['AAPL', 'HALO', 'TSLA']

for idx, ticker in enumerate(tickers, 1):
    akcia = Stock(ticker)
    if akcia.df is not None:
        print('#{}: Ticker {} je OK.'.format(idx, akcia.ticker))
    else:
        print('#{}: Ticker {} je nedostupny.'.format(idx, akcia.ticker))
