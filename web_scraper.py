import requests
from bs4 import BeautifulSoup
import time
import datetime

def time_now():
    now = time.localtime()
    now = time.strftime("%H:%m:%S", now)
    return now
 
def stk_price():
     
    #html_text = requests.get('https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch')
    html_text = requests.get('https://finance.yahoo.com/quote/9988.HK?p=9988.HK&.tsrc=fin-srch')
    soup= BeautifulSoup(html_text.text, 'lxml')

    price = soup.find_all('div', class_="D(ib) Mend(20px)")[0].find('span').text

    return price

if __name__ == '__main__':
    
    while True:
        
        t = datetime.datetime.now()
        t = t.strftime("%x %X")
        
        print(t , stk_price())
        
        c = t + ' ' + stk_price()
      
        f = open(r'C:\Users\xxxxx\Desktop\xxxxx Project\data.txt', 'a')
        
        f.write(f'{c}\n')
        
        f.close
        
        time.sleep(0.5)





