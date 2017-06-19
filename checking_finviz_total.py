import pandas as pd
import datetime
import sys

start = datetime.datetime(2017, 4, 6, 19, 30, 0)
end = datetime.datetime(2017, 6, 6, 21, 0, 0)

teraz = datetime.datetime.now()

if not start <= teraz <= end:
    print('Ešte nie je čas.')
    sys.exit()
else:
    with open('/opt/cirque/finviz_log.txt', 'a') as fhandle:
        url = 'http://finviz.com/screener.ashx?v=111&f=ind_stocksonly,sh_avgvol_o50,sh_price_o5,ta_sma200_sb50,ta_sma50_pa&ft=3&r=1'
        list_of_dfs = pd.read_html(url)
        total = int(list_of_dfs[9][0].str.split()[0][1])
        date = str(datetime.datetime.now())
        fhandle.write('Check @ {}:\t{}\n'.format(date, total))

sys.exit()


# Je teraz menej hodin ako 22:00?
