from yahoo_finance import Share

stock = Share('TSLA')
start_date = '2016-01-01'
end_date = '2016-06-08'

print('Retrieving data...')
closes = [c['Close'] for c in stock.get_historical(start_date, end_date)]

print('Data retrieved.')
for c in closes:
    print(c)
