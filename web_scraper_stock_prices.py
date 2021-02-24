import requests
from bs4 import BeautifulSoup
import datetime
import json
import pandas as pd

def stock_price(ticker):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

    url = f'https://finance.yahoo.com/quote/{ticker}'

    r = requests.get(url,  headers= header)

    soup = BeautifulSoup(r.text , 'html.parser')

    #price = soup.find('span', class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text.strip()
    #change = soup.find('span', class_= 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)').text.strip()

    #'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)'
    
    date_time = datetime.datetime.now()
    date_time = date_time.strftime("%d/%m/%Y %H:%M:%S")
    
    info = {
    'date-time': date_time ,
    'symbol': ticker ,
    'price' :  soup.find('div', class_ = 'D(ib) Mend(20px)').find_all('span')[0].text.strip() ,
    'change' : soup.find('div', class_='D(ib) Mend(20px)').find_all('span')[1].text.strip()
    }
    
    return info

stocks= ['FB', 'AMZN', 'MSFT',  'NFLX', 'BKNG', 'TSLA', 'BRK-A', 'BRK-B']

mystocks= []

for item in stocks:
    print('Getting: ', item)
    mystocks.append(stock_price(item))

with open('stock_data.json', 'w') as file:
    json.dump(mystocks, file)

df1 = pd.read_json('stock_data.json')
df1.to_csv(r'C:\Users\wajda\Desktop\Chris Project\stock_data_json.csv')

df2 = pd.DataFrame(mystocks)
df2.to_csv(r'C:\Users\wajda\Desktop\Chris Project\stock_data_csv.csv')

