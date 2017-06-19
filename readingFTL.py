import urllib.request
from bs4 import BeautifulSoup

url = 'http://bit.ly/Free-Tech-Learning'

resp = urllib.request.urlopen(url)
html = resp.read()

soup = BeautifulSoup(html, 'html.parser')
obj = soup('h2')

print(obj[0].text.strip())

'''
#print(type(obj))

for item in obj:
    print(item.text)
'''
