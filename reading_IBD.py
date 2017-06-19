import requests
import re

url = 'http://research.investors.com/stock-quotes/nasdaq-microsoft-corp-msft.htm'

r = requests.get(url).text
print(r[:100])
