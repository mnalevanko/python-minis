import pandas as pd
from pandas_datareader import data as web
import datetime
from time import sleep


def number_of_stocks(url):
    '''Returns the total number of stocks for given screen's URL.'''

    df_temp = pd.read_html(url)
    total = int(df_temp[9][0].str.split()[0][1]) # Reads the number behind "Total: "
    #print('Number of stocks to check: {}'.format(total))
    return total


def symbols_from_url(url):
    '''Returns a list of stocks from a single Finviz page.'''

    df = pd.read_html(url)
    stocks = list(df[10][1])[1:]
    return stocks


def get_column_names(url):
    '''Returns a list with column names from a single Finviz page.'''

    df = pd.read_html(url)[10] # Extracts the table #10 from a list of dataframes
    vals = df.values
    zoznam = list(vals[0])
    return zoznam


def change_name(ret:str):
    '''Clears a string from specific characters'''

    restricted_chars = ['.', ' ', '/']
    new_char = []

    for i in ret:
        if i not in restricted_chars:
            new_char.append(i.lower())
    return ('').join(new_char)


def get_all_symbols(url):
    '''Returns a list of all stock tickers from given screener.'''

    total = number_of_stocks(url)
    counter = 1
    stocks = []

    while counter <= total:
        appendix = '&r=' + str(counter) if counter > 1 else ''
        path = url + appendix
        #print(path)
        stocks += symbols_from_url(path)
        counter += 20

    return stocks


def n_years_into_days(n):
    '''Turns a number of years into number of records in trading statistics.'''

    today = datetime.date.today()
    year_today = today.year
    start_date = datetime.date(today.year - n, today.month, today.day)

    sp500_df = web.DataReader('^GSPC', data_source='yahoo', start=start_date, end=today)

    return len(sp500_df)

DNES = datetime.date.today()
PRED_ROKOM = DNES - datetime.timedelta(days=n_years_into_days(1))
SP500 = web.DataReader('^GSPC', 'yahoo', PRED_ROKOM, DNES)



def rs_index(ticker):
    '''Generates a Relative Strength Index'''

    sleep(1)
    try:
        df = web.DataReader(ticker, 'yahoo', PRED_ROKOM, DNES)
        rsl = df['Adj Close'] / SP500['Adj Close']
        total_range = rsl.max() - rsl.min()
        rs_percentage = (rsl[-1] - rsl.min()) / total_range * 100
        rs_percentage = round(rs_percentage, 2)
        print('{:10}{}'.format(ticker, rs_percentage))
        return rs_percentage
    except:
        print('{:10}{}'.format(ticker, 'N/A'))
        return 'N/A'


def generate_dataframe(url):
    '''Generates a dataframe object from Finviz table data.'''

    column_names_set = False        # Test existencie pola s nazvami rubrik
    total = number_of_stocks(url)   # Celkovy pocet akcii v screene
    counter = 1
    records = []                    # Ulozisko individualnych riadkov tabulky

    while counter <= total:
        appendix = '&r=' + str(counter) if counter > 1 else ''
        path = url + appendix

        # Read all data from a table

        df_temp = pd.read_html(path)
        values_temp = df_temp[10].values.tolist()

        if not column_names_set:
            column_names = values_temp[0]
            column_names_set = True

        records.extend(values_temp[1:])
        counter += 20

    columns = [change_name(item) for item in column_names]

    df = pd.DataFrame(records, columns=columns)
    del df['no']

    return df

'''
if __name__ == '__main__':
    print('Zaciname:', datetime.datetime.now())
    url = 'http://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_avgvol_o50,sh_price_o5,ta_sma200_sb50&ft=3'
    pole = get_all_symbols(url)
    counter = 1

    for item in pole:
        if '-' in item:
            item = item.replace('-', '')
        print('#{}:\t{}\tData from WSJ.com: {}'.format(counter, item, get_stock_price_from_wsj(item)))
        counter += 1

    print('Koniec:', datetime.datetime.now())
'''
