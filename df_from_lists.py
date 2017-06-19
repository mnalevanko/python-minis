'''Creating a dataframe object from lists with data columns.'''
import pandas as pd
from finviz import number_of_stocks

symbols = ['TSLA', 'AAPLE', 'MSFT', 'GOOGL']
names = ['Tesla', 'Apple', 'Microsoft', 'Google']
biz = ['auta, vesmir', 'spotrebna elektronika', 'software', 'internet']

df = pd.DataFrame({'Nazov spolocnosti':names, 'Ticker':symbols, 'Predmet podnikania':biz}, columns=[ 'Ticker', 'Nazov spolocnosti', 'Predmet podnikania'], index=None)

print(df)
