import re
import urllib.request

url = 'http://www.sme.sk'
html = urllib.request.urlopen(url).read()

print('Stranka precitana.')
print(type(html))
