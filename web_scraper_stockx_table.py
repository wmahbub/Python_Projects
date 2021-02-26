import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json


url_bid =['https://stockx.com/api/products/5f212cfa-1910-4d01-b254-fabf09dded14/activity?state=400&currency=USD&limit=100&page=1&sort=amount&order=ASC&country=US',
          'https://stockx.com/api/products/302c03e2-3e51-42da-8682-90542a6c878e/activity?state=400&currency=USD&limit=100&page=1&sort=amount&order=ASC&country=US'

            ]

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

r = requests.get(url_bid[1], headers = header)

soup = BeautifulSoup(r.text, 'html.parser')

data_dict = json.loads(soup.text)

product = data_dict['ProductActivity']

df_bid = pd.DataFrame(product)

print('Bids Table')
print(df_bid[[ 'shoeSize', 'frequency', 'localAmount','localCurrency']].head(5))


url_ask = ['https://stockx.com/api/products/5f212cfa-1910-4d01-b254-fabf09dded14/activity?state=300&currency=USD&limit=100&page=1&sort=amount&order=DESC&country=US',
           'https://stockx.com/api/products/302c03e2-3e51-42da-8682-90542a6c878e/activity?state=300&currency=USD&limit=100&page=1&sort=amount&order=DESC&country=US'
            
            ]

r = requests.get(url_ask[1], headers=header)

soup = BeautifulSoup(r.text, 'html.parser')

data_dict = json.loads(soup.text)

product = data_dict['ProductActivity']

df_ask = pd.DataFrame(product)

print('Ask Table')
print(df_ask[['shoeSize', 'frequency', 'localAmount','localCurrency']].head(5))


#'https://stockx.com/api/products/5f212cfa-1910-4d01-b254-fabf09dded14/activity?state=400&currency=USD&limit=100&page=1&sort=amount&order=ASC&country=US'

"""
f'https://stockx.com/api/products/{sku_number}/activity?state={bid/ask}&currency={currency}&limit={number_rows}&page={page_number}&sort=amount&order=ASC&country={country}'

params = {'sku_number': '',
          'bid/ask': '',
          'currency': '',
          'number_rows': '' ,
          'page_number': '',
          'country': '',
          }
"""


url_last_sale = ['https://stockx.com/api/products/5f212cfa-1910-4d01-b254-fabf09dded14/activity?state=480&currency=USD&limit=10&page=1&sort=createdAt&order=DESC&country=US'
                 'https://stockx.com/api/products/715fc618-f9a3-4bc2-90c2-bbfb9f24e9dd/activity?state=480&currency=USD&limit=10&page=2&sort=createdAt&order=DESC&country=US'
                 ]

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

r = requests.get(url_last_sale[0], headers=header)

soup = BeautifulSoup(r.text, 'html.parser')

data_dict = json.loads(soup.text)

product = data_dict['ProductActivity']

df_last_sale = pd.DataFrame(product)

print('Last Sale Table')
print(df_last_sale.head(10))
