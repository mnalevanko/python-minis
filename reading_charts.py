from urllib.request import Request, urlopen
url = 'http://stockcharts.com/c-sc/sc?s=GIMO&p=D&b=5&g=0&i=0&r=1480944414802'

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

file = open('GIMOstock.png', 'wb')
file.write(webpage)
file.close()
