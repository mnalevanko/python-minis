from pandas_datareader import data as web
import random

tickers = ['TSLA', 'MSFT', 'EDU', 'GTN', 'FB']
iterations = 1000

for a in range(iterations):
    ticker = random.choice(tickers)    
    df = web.DataReader(ticker, 'google')
    print('#{}: {}'.format(a+1, len(df)))
