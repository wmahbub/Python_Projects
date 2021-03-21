import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime



url = 'https://stockx.com/air-jordan-1-mid-signal-blue'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
proxy = {'http': '207.157.220.8:3128', 'https': '207.157.220.8:8080'}


'207.157.220.8' ; 3128 , 8080





r = requests.get(url, headers=header, proxies= proxy)

#soup = BeautifulSoup(r.text, 'html.parser')

#body = soup.find('script', type='application/ld+json').string()

print(r.status_code)
