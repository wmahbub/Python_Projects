import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime

sku = '57c2cdc3-e398-4661-8bb2-a975c0a00710'

def sale_history(sku):
    
    url= f'https://stockx.com/api/products/{sku}/activity?state=480&currency=USD&limit=500&page=1&sort=createdAt&order=DESC&country=US'
    
    'https://stockx.com/api/products/57c2cdc3-e398-4661-8bb2-a975c0a00710/activity?state=480&currency=USD&limit=500&page=1&sort=createdAt&order=DESC&country=US'
    
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

    proxy = {'http': '207.157.220.8:3128', 'https': '207.157.220.8:8080'}

    r = requests.get(url, headers= header, proxies = proxy)
    
    soup = BeautifulSoup(r.text, 'html.parser').text.strip()
    
    sale_history_dict = json.loads(soup)
    
    df = pd.DataFrame(sale_history_dict['ProductActivity'])
    
    return df
    
    #df.to_csv('sale_history.csv',index= False)
    

sale_history(sku)
    
