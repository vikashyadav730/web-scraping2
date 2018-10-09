import requests
from bs4 import BeautifulSoup as bs


page = requests.get("https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250")

movie = dict()

soup = bs(page.text,"html.parser")
a = soup.find_all('td',class_='titleColumn')
#print a
b = soup.find_all('td', class_='ratingColumn imdbRating')
print b
for col1, col2 in zip(a , b):
    print(col1.find('a').text,': ',col2.find('strong').text)