import pandas_datareader.data as web
import pandas as pd

url = 'http://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_avgvol_o200,sh_price_o10,ta_sma200_sb50,ta_sma50_pa&ft=3'
df_temp = pd.read_html(url)
number_of_stocks = int(df_temp[9][0].str.split()[0][1])

