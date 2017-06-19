import pandas as pd
import pandas_datareader.data as web
import datetime

end = datetime.datetime.today()
rozdiel = datetime.timedelta(days=30)
start = end - rozdiel

print(start)
print(end)

df1 = web.DataReader('MSFT', 'google', start, end)
df2 = web.DataReader('MSFT', 'yahoo', start, end)

