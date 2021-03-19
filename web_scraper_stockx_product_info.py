import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime
    
url = 'https://stockx.com/air-jordan-1-mid-signal-blue'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

r = requests.get(url, headers=header)

soup = BeautifulSoup(r.text, 'html.parser')

info = soup.find('div', class_ ='product-details detail-row')
#price = info.find_all('span')[-4]

release_price = info.find_all('div', class_ ='detail')[2]
release_price = release_price.find_all('span')[2].text

release_date = info.find_all('div', class_='detail')[3]
release_date = release_date.find_all('span')[2].text


print(release_price, release_date)


