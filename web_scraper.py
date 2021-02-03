import requests
from bs4 import BeautifulSoup
import time
import datetime

def time_now():
    now = time.localtime()
    now = time.strftime("%H:%m:%S", now)
    return now
 
def stk_price():
    
    try:
     
        html_text = requests.get('https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch')
        
        soup= BeautifulSoup(html_text.text, 'lxml')

        price_normal = soup.find_all('div', class_="D(ib) Mend(20px)")[0].find('span').text

        return price_normal
    
    except:
        return str(0)


def stk_price_alt():
    
    try:
     
        html_text = requests.get('https://finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch')
        
        soup= BeautifulSoup(html_text.text, 'lxml')

        price_alt = soup.find_all('p', class_= "Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)")[0].find('span').text

        return price_alt
    
    except:
        
        return str(0)



if __name__ == '__main__':
    
    while True:
        
        t = datetime.datetime.now()
        t = t.strftime("%x  %X")
        
        print(t ,' ' , stk_price(),' ', stk_price_alt() )
        
        c = t + '  ' + stk_price() + '  ' + stk_price_alt()
      
        f = open(r'C:\Users\wajda\Desktop\Chris Project\data.txt', 'a') # Data Location
        
        f.write(f'{c}\n')
        
        f.close
        
        time.sleep(2)





