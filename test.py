import os
import pandas as pd
import pandas_datareader.data as web

df = web.DataReader('EDU', 'google', '1950/1/1', '2016/12/8')
print(df.tail())
