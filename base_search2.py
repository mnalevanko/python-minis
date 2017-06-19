import os
import pandas as pd
import pandas_datareader.data as web
import datetime
from time import sleep
from collections import Counter
from urllib.request import Request, urlopen

subor = 'zoznam.txt'
cesta = 'C:/Users/michal.data/Desktop'
path_to_folder = 'C:/Users/michal.data/Desktop/Akcie'

obsah = os.listdir(path_to_folder)

if len(obsah) > 0:
    for f in obsah:
        new_path = os.path.join(path_to_folder, f)
        os.remove(new_path)

filepath = os.path.join(cesta, subor)
all_symbols = []
unique_symbols = []
consolidating_stocks = []
recent_ipos = []
unavailable_stocks = []

for line in open(filepath):
    #print(line.strip(), len(line.strip()))
    if len(line.strip()) > 0:
        pole = line.strip().split()
        if len(pole) == 1:
            all_symbols.append(pole[0])
    
symbols_d = Counter(all_symbols)

for k, v in symbols_d.most_common():
    unique_symbols.append(k)

'''
print(len(unique_symbols)) # Obsahuje vsetky unikatne tickery z nacitanych zoznamov
'''

end = datetime.date.today()
start = end - datetime.timedelta(days=730)
source = 'yahoo'

def is_consolidating(ticker):
    '''Checks is the stock is consolidating or not.'''
    sleep(1)
    print('Checking {}...'.format(ticker))
    try:
        df = web.DataReader(ticker, source, start, end)
        if len(df) < 21:
            recent_ipos.append(ticker)
            #print('{} seems to be a recent IPO.'.format(ticker))
        else:
            df['200DMA'] = df['Close'].rolling(200).mean()
            df['50DMA'] = df['Close'].rolling(50).mean()
            df['Ymin'] = df['Low'].rolling(250).min()
            df['AboveMin'] = ((df['Close'] - df['Ymin']) / df['Ymin']) * 100
            df['VolumeAvg'] = df['Volume'].rolling(50).mean()
            df['Ymax'] = df['High'].rolling(250).max()

            test1 = df['50DMA'][-1] >= df['200DMA'][-1] # 50DMA must be above 200DMA
            test2 = df['Close'][-1] > df['50DMA'][-1] # Last close must be above 50DMA
            test3 = df['Ymax'][-1] == df['Ymax'][-21] # Testing the equality of 52Wk highs
            test4 = df['VolumeAvg'][-1] >= 200000
            test5 = df['AboveMin'][-1] >= 40.00

            if all((test1, test2, test3, test4, test5)):
                print('{} is consolidating.'.format(ticker))
                consolidating_stocks.append(ticker)
            else:
                #print('{} is not consolidating.'.format(ticker))
                unavailable_stocks.append(ticker)
            
    except:
        print('Symbol {} is not available.'.format(ticker))
        unavailable_stocks.append(ticker)

pocitadlo = 0
for symbol in unique_symbols:
    print('#{}: '.format(pocitadlo + 1), end='')
    is_consolidating(symbol)
    pocitadlo += 1

link1 = 'http://stockcharts.com/c-sc/sc?s='
link2 = '&p=W&b=5&g=0&i=t81488322412&r=1481280545466'
os.chdir('C:/Users/michal.data/Desktop/Akcie/')

def download_chart(ticker):
    sleep(1)
    url = link1 + ticker.upper() + link2
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    file = open(ticker.upper() + '.png', 'wb')
    file.write(webpage)
    file.close()

if len(consolidating_stocks) > 0:
    for akcia in consolidating_stocks:
        download_chart(akcia)
