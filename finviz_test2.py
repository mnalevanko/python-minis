from pandas_datareader import data as web
import datetime

today_date = datetime.date.today()
one_year_ago_date = datetime.date(today_date.year - 1, today_date.month, today_date.day)
two_years_ago_date = datetime.date(today_date.year - 2, today_date.month, today_date.day)

SP500_1Y = web.DataReader('^GSPC', 'yahoo', one_year_ago_date, today_date)
SP500_2Y = web.DataReader('^GSPC', 'yahoo', two_years_ago_date, today_date)

class St
