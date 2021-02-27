import requests
import pandas as pd
from bs4 import BeautifulSoup
import json


url_last_sale = ['https://stockx.com/api/products/5f212cfa-1910-4d01-b254-fabf09dded14/activity?state=480&currency=USD&limit=10&page=1&sort=createdAt&order=DESC&country=US',
                 'https://stockx.com/api/products/715fc618-f9a3-4bc2-90c2-bbfb9f24e9dd/activity?state=480&currency=USD&limit=10&page=2&sort=createdAt&order=DESC&country=US',
                 'https://stockx.com/api/products/b5250116-e4e3-4ecc-a7c0-b730e40d9e79/activity?state=480&currency=USD&limit=10&page=8&sort=createdAt&order=DESC&country=US'
                 
                 ]

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

r = requests.get(url_last_sale[0], headers=header)

soup = BeautifulSoup(r.text, 'html.parser')

data_dict = json.loads(soup.text)

last_sale = data_dict['ProductActivity']

df_last_sale = pd.DataFrame(last_sale)

df_last_sale[['Date','Time']] = df_last_sale['createdAt'].str.split('T', expand=True)

print()
print('Last Sale Table')
print()
print(df_last_sale[['Date', 'Time','shoeSize', 'amount', 'localAmount', 'localCurrency']].head(10))

