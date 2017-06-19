import os
import datetime
from collections import Counter
from time import sleep
import pandas_datareader.data as web
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
from urllib.request import Request, urlopen

'''
Kontrola toho, ci dnes ma byt program spusteny alebo nie. Skript by mal
pracovat len v pracovny den, t.j. nie v sobotu ani v nedelu.
'''

dnes = datetime.date.today()

def is_working_day(dnes):
    '''Funkcia vrati hodnotu True, ak zadany den nie je sobota alebo nedela.'''
    holidays = [datetime.date(2016, 12, 26), datetime.date(2017, 1, 2), datetime.date(2017, 1, 16), datetime.date(2017, 2, 20), datetime.date(2017, 4, 14),
                datetime.date(2017, 5, 29), datetime.date(2017, 9, 4), datetime.date(2017, 12, 25)]
    if 0<= dnes.weekday() <=4 and dnes not in holidays:
        return True
    else:
        return False
        
if not is_working_day(dnes):
    sys.exit()

'''
Nasledovny blok programu vytvori object typu dictionary nazvany 'd', ktory
nacita jednotlive watchlisty do prislusnych poloziek slovnika.
'''

path_to_file = 'C:/Users/michal.data/Desktop/zoznam.txt'
d = dict()

'''
Vycistim folder, do ktoreho budem ukladat grafy akcii.
'''
def vycisti_folder():
    path_to_folder = 'C:/Users/michal.data/Desktop/Akcie/'
    obsah = os.listdir(path_to_folder)
    if len(obsah) > 0:
        for f in obsah:
            new_path = os.path.join(path_to_folder, f)
            os.remove(new_path)


'''
Vytvaram prazdny slovnik, ktoreho indexom su nazvy jednotlivych watchlistov.
'''

for line in open(path_to_file):
    line = line.strip()
    line_l = line.split()
    if len(line_l) > 1:
        #print(line)
        #print('Creating a dictionary with the index of {}.'.format(line))
        d[line] = []

'''
Po vytvoreni slovnika nacitavam opat subor, aby som jednotlive symboly priradil
do prislusneho elementu slovnika 'd'.
'''
        
for line in open(path_to_file):
    line = line.strip()
    line_l = line.split()
    if len(line_l) > 1:
        label = line
    if len(line_l) == 1:
        d[label].append(line)

tickers_l = [] # Zoznam vsetkych tickerov v subore

for line in open(path_to_file):
    line = line.strip()
    line_l = line.split()
    if len(line_l) == 1:
        tickers_l.append(line)

'''
tickers_l teraz obsahuje nacitany zoznam vsetkych tickerov aj duplicitami.
'''        

tickers_d = Counter(tickers_l)
unique_tickers = []

for (k, v) in tickers_d.most_common():
    unique_tickers.append(k)

'''
unique_tickers teraz obsahuje vsetky symboly po vyluceni duplicity a zoradene
podla pocetnosti vyskytu.
'''    
    
def kde_je_ticker(symbol):
    '''Funkcia vracia retazec s nazvami vsetkych watchlistov, na ktorych je
    dany symbol.'''
    kde_je = []
    for key in d.keys():
        if symbol in d[key]:
            kde_je.append(key)
    vysledok = (', ').join(kde_je)
    return vysledok

'''
Teraz musim nacitat vsetky tickery zo suboru txt a vlozit ich
do pola sent_tickers.
'''

sent_tickers = []

with open('C:/Users/michal.data/Desktop/sent.txt') as fhandle:
    for line in fhandle:
        if len(line) > 0:
            sent_tickers.append(line.strip())
            
end = datetime.date.today()
start = end - datetime.timedelta(days=730)
source = 'yahoo'

def stock_available(ticker, start, end):
    try:
        df = web.DataReader(ticker, source, start, end)
        return True
    except:
        return False

def is_consolidating(ticker, start, end):
    '''Checks whether the stock is consolidating, trading above 50DMA'''
    df = web.DataReader(ticker, source, start, end)
   
    if len(df) >= 21:
        df['200DMA'] = df['Close'].rolling(200).mean()
        df['50DMA'] = df['Close'].rolling(50).mean()
        df['Ymin'] = df['Low'].rolling(250).min()
        df['AboveMin'] = ((df.Close - df.Ymin) / df.Ymin) * 100
        df['VolumeAvg'] = df['Volume'].rolling(50).mean()
        df['Ymax'] = df['High'].rolling(250).max()
        test1 = df['50DMA'][-1] >= df['200DMA'][-1]
        test2 = df.Close[-1] > df['50DMA'][-1]
        test3 = df['Ymax'][-1] == df['Ymax'][-21]
        test4 = df['VolumeAvg'][-1] >= 200000
        test5 = df['AboveMin'][-1] >= 40.00
        if all((test1, test2, test3, test4, test5)):
            return True, len(df)
        else:
            return False, None
           
    elif 0 < len(df) < 21:
        return True, len(df)

def uloz_graf(ticker):
    link1 = 'http://stockcharts.com/c-sc/sc?s='
    link2 = '&p=W&b=5&g=0&i=t81488322412&r=1481280545466'  
    
    os.chdir('C:/Users/michal.data/Desktop/Akcie/')
    
    url = link1 + ticker.upper() + link2
    
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    file = open(ticker.upper() + '.png', 'wb')
    file.write(webpage)
    file.close()        
        
def posli_ticker(symbol):
    '''Funkcia posle email, ktoreho prilohou bude graf akcie. Telo emailu bude
    mat dve casti: ticker a zoznam watchlistov, na ktorych ticker je.
    '''
    predmet2 = kde_je_ticker(symbol)
    
    if predmet2.count(',') < 10:
            
        uloz_graf(symbol)
        sleep(1)
        recipients = ['michal.nalevanko@gmail.com']
        emaillist = [elem.strip().split(',') for elem in recipients]
        msg = MIMEMultipart()
        
        predmet1 = symbol
        #predmet2 = kde_je_ticker(symbol)
        msg['Subject'] = '{} in {}'.format(predmet1, predmet2)
        msg['From'] = 'nalevanko.data@gmail.com'
        msg.preamble = 'Multipart massage.\n'
        part = MIMEText("mn") # Toto sa objavi v samotnom e-maili
        msg.attach(part)
        
        nazov_suboru = 'C:/Users/michal.data/Desktop/Akcie/{}.png'.format(symbol.upper())
        part = MIMEApplication(open(nazov_suboru,"rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=nazov_suboru)
        msg.attach(part)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login("nalevanko.data@gmail.com", "Lkjtp,tbats.")
        server.sendmail(msg['From'], emaillist , msg.as_string())
        server.close()
           
consolidating_stocks = []
recent_ipos = []
unavailable_stocks = []  

for i, symbol in enumerate(unique_tickers):
    if len(symbol) > 0:
       
        sleep(1)
        print('#{} Checking: {}'.format(i, symbol))
       
        if stock_available(symbol, start, end):
            #print('Availability: OK')
            term = is_consolidating(symbol, start, end)
            if term != None and term[0] and term[1] >= 21:
                print('Konsoliduje: {}'.format(symbol))
                posli_ticker(symbol)
                consolidating_stocks.append(symbol)
            elif term != None and term[0] and term[1] < 21:
                recent_ipos.append(symbol)
            else:
                #print('Nekonsoliduje: {}'.format(symbol))
                pass
        else:
            #print('Symbol {} not available.'.format(symbol))
            unavailable_stocks.append(symbol)


            
