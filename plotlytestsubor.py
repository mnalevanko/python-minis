import plotly 
plotly.tools.set_credentials_file(username='mnalevanko', api_key='052po991ys')

import plotly.plotly as py
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import Line, Marker
from datetime import datetime

import pandas.io.data as web

df = web.DataReader("aapl", 'yahoo', datetime(2008, 1, 1), datetime(2009, 4, 1))

# Make increasing ohlc sticks and customize their color and name
fig_increasing = FF.create_ohlc(df.Open, df.High, df.Low, df.Close, dates=df.index,
    direction='increasing', name='AAPL',
    line=Line(color='rgb(150, 200, 250)'))

# Make decreasing ohlc sticks and customize their color and name
fig_decreasing = FF.create_ohlc(df.Open, df.High, df.Low, df.Close, dates=df.index,
    direction='decreasing',
    line=Line(color='rgb(128, 128, 128)'))

# Initialize the figure
fig = fig_increasing

# Add decreasing data with .extend()
fig['data'].extend(fig_decreasing['data'])

py.iplot(fig, filename='finance/aapl-ohlc-colors', validate=False)

