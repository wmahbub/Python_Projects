from urllib.request import Request, urlopen
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pyppdf.patch_pyppeteer
from requests_html import HTMLSession
import json


url_bid = 'https://stockx.com/api/products/5f212cfa-1910-4d01-b254-fabf09dded14/activity?state=400&currency=USD&limit=100&page=1&sort=amount&order=ASC&country=US'



header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

r = requests.get(url_bid, headers = header)

soup = BeautifulSoup(r.text, 'html.parser')

data_dict = json.loads(soup.text)

product = data_dict['ProductActivity']

df_bid = pd.DataFrame(product)

print(df_bid.head(5))


url_ask = 'https://stockx.com/api/products/5f212cfa-1910-4d01-b254-fabf09dded14/activity?state=300&currency=USD&limit=100&page=1&sort=amount&order=DESC&country=US'

r = requests.get(url_ask, headers=header)

soup = BeautifulSoup(r.text, 'html.parser')

data_dict = json.loads(soup.text)

product = data_dict['ProductActivity']

df_ask = pd.DataFrame(product)

print(df_ask.head(5))
