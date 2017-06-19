from pandas_datareader import data as web
import datetime

dnes = datetime.date.today()
pred_rokom = datetime.date(dnes.year - 1, dnes.month, dnes.day)
sp = web.DataReader('^GSPC', 'yahoo', start=pred_rokom, end=dnes)

zoznam_str = 'AEIS FNGN MRCY MTSI RP FOXF AVGO MPWR ELLI LOGM ANW CSFL SBGI MCHP CBF FCB TNET AMKR SBCF SNPS IPGP ALRM CYTK BLDR TREX PAH CBM RDN AXTI SNV KLIC SSP VMW SANM AMN GSIT SSNC SINO EWBC WTW LAZ NUVA MEI WB HZO SORL PTLA HUSA MIME BXS SOXL AUPH AVXS CATY JBT FATE CSTE LEA CBAY RGNX FL BOJA BA WRK LNTH FIG SLAB TPC TRCH HLIT PME LLNW PXLW CVEO HBHC TEAM ZBRA SBY HQY CNCE FMI MVIS TVTY BWXT TGTX ESPR CALA STX WMB BANC SQ DELT KITE CTXS LJPC ENS MDP'
zoznam_list = zoznam_str.split()

for akcia in zoznam_list:
    df = web.DataReader(akcia, 'google', start=pred_rokom, end=dnes)
    df['RSI'] = df.Close / sp['Adj Close']
    range_min = df['RSI'].min()
    range_max = df['RSI'].max()
    range_total = range_max - range_min
    index = round((df['RSI'][-1] - range_min) / (range_max - range_min) * 100, 2)
    if index >= 95:
        print('{:8s}{}'.format(akcia, index))
    
