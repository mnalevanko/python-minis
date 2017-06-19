import pandas as pd
import pandas_datareader.data as web
import datetime


def adjustedVolume(change, volume):
    if change < 0:
        return volume
    else:
        return 0

source = 'google'
i = datetime.datetime.now()
start = '1/1/2016'
end = str(i.month) + '/' + str(i.day) + '/' + str(i.year)

def isPocketPivot(symbol):
    
    try:
        df = web.DataReader(symbol, source, start, end)
        if len(df) > 0:

            df['Difference'] = df['Close'].diff()
            df['Adjusted volume'] = list(map(adjustedVolume, df['Difference'], df['Volume']))

            last_volume = df['Volume'][-1]
            checking_volume = df['Adjusted volume'][-11:-1].max()

            if last_volume > checking_volume:
                return True
            else:
                return False
    except:
        print('Ticker {} nedokážem posúdiť.'.format(item))
        
df1 = pd.read_csv('C://Users//Michal//Desktop//stocksup.txt', header = None)
df1 = list(df1[0])

for item in df1:
    
    if isPocketPivot(item):
        print(item)
