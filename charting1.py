from pandas.io.data import get_data_yahoo
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.pyplot import subplots, draw
from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt

# get the data on a symbol (gets last 1 year)
symbol = "TSLA"
data = get_data_yahoo(symbol, datetime.now() - timedelta(days=365))

# drop the date index from the dateframe
data.reset_index(inplace = True)

# convert the datetime64 column in the dataframe to 'float days'
data.Date = mdates.date2num(data.Date)

# make an array of tuples in the specific order needed
dataAr = [tuple(x) for x in data[['Date', 'Open', 'Close', 'High', 'Low']].to_records(index=False)]

# construct and show the plot
fig = plt.figure()
ax1 = plt.subplot(1,1,1)
candlestick2_ohlc(ax1, dataAr)
plt.show()
