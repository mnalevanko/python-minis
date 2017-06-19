'''
Modul pre sledovanie novych emisii na akciovom trhu (IPOs)

Autor:  Ing. Michal Nalevanko
Verzia: 1.0
'''

#Nacitanie aktualnych datumov a urcenie intervalov pre stahovanie dat

import datetime
import pandas as pd

dnes = datetime.datetime.today()
mesiac = dnes.month
rok = dnes.year

zaciatok_mesiac = mesiac
zaciatok_rok = rok - 3

#Tu zadavam, ako daleko do historie chcem ist

pocet_mesiacov = 24

m = int(mesiac)
y = int(rok) - int(pocet_mesiacov/12)
urls = []

def vratMesiac(n):
    if n >= 10:
        return str(n)
    else:
        return '0' + str(n)

for a in range(pocet_mesiacov):
    urls.append('http://www.nasdaq.com/markets/ipos/activity.aspx?tab=pricings&month=' + str(y) + '-' + vratMesiac(m))
    if m == 12:
        y += 1
        m = 0
    m += 1

urls.append('http://www.nasdaq.com/markets/ipos/activity.aspx?tab=pricings')

tickers = []

for url in urls:
    try:
        print(url)
        df = pd.read_html(url)
        tickers += list(df[3].Symbol)
    except:
        pass

filepath = 'C://Users/michal.data/Desktop/ipos.txt'

with open(filepath, 'w') as fhandle:
    for ticker in tickers:
        fhandle.write(ticker + '\n')

print('Koniec programu.')
    
