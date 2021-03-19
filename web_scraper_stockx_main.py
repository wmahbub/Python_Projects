import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime

def high_low_vol(sku):
    url = f'https://stockx.com/api/products/{sku}/market?currency=USD&country=US'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    
    proxy = {'http': '207.157.220.8:3128', 'https': '207.157.220.8:8080'}
    
    r = requests.get(url, headers=header, proxies= proxy)

    soup = BeautifulSoup(r.text, 'html.parser').text.strip()

    sku_dictionary = json.loads(soup)

    info = [
        sku_dictionary['Market']['annualLow'],
        sku_dictionary['Market']['annualHigh'],
        sku_dictionary['Market']['deadstockRangeLow'],
        sku_dictionary['Market']['deadstockRangeHigh'],
        round(sku_dictionary['Market']['volatility']*100, 2)
    ]

    return info


def sku_info():
    url = 'https://stockx.com/air-jordan-1-mid-signal-blue'

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    proxy = {'http': '207.157.220.8:3128', 'https': '207.157.220.8:8080'}
    
    r = requests.get(url, headers=header, proxies= proxy)

    soup = BeautifulSoup(r.text, 'html.parser')

    body = soup.find('script', type='application/ld+json').string.strip()

    data = json.loads(body)

    today = datetime.date.today()
    date = today.strftime("%m/%d/%Y")

    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
        
    info = soup.find('div', class_='product-details detail-row')

    #release_price = info.find_all('div', class_='detail')[2]
    #release_price = release_price.find_all('span')[2].text.strip()
    
    manuf_code = info.find_all('div', class_='detail')[0]
    manuf_code = manuf_code.find_all('span')[2].text.strip()

    release_date = info.find_all('div', class_='detail')[3]
    release_date = release_date.find_all('span')[2].text.strip()
    
    

    skus= []
    
    """
    main = {'scrape_date': date, 
            'scrape_time': time, 
            'release_date': release_date,
            'name': data['name'] , 
            'sku': data['sku'], 
            'size': 0, 
            'lowest_ask_price': 0, 
            'currency': 'USD'}
    
    skus.append(main)
    """
    
    for i in range(len(data['offers']['offers'])):
    
        product = {
            'scrape_date': date,
            'scrape_time': time,
            'release_date': release_date,
            'style_code': manuf_code, 
            'name': data['name'],
            'main_product_id': data['sku'],
            'sku': data['offers']['offers'][i]['sku'],
            'size': data['offers']['offers'][i]['description'],
            #'lowest_ask_price': data['offers']['offers'][i]['price'],
            #'currency': data['offers']['offers'][i]['priceCurrency'],
            '52_week_low': high_low_vol(data['offers']['offers'][i]['sku'])[0],
            '52_week_high': high_low_vol(data['offers']['offers'][i]['sku'])[1],
            'traderange_low': high_low_vol(data['offers']['offers'][i]['sku'])[2],
            'traderange_high': high_low_vol(data['offers']['offers'][i]['sku'])[3],
            'volatility': high_low_vol(data['offers']['offers'][i]['sku'])[4]
        
        }
    
        skus.append(product)
        
    df = pd.DataFrame(skus)
    df.to_csv('skus.csv', index=False)
    
    return skus


start= datetime.datetime.now()

print(sku_info())

end = datetime.datetime.now()
print()
print('Completed in: ', end-start, ' seconds')
print()




"""
if __name__ == '__main__' :
    
    start = datetime.datetime.now()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(sku_info)

    end = datetime.datetime.now()

    print('Completed in: ', end-start, ' seconds')
"""

# market information
'https://stockx.com/api/products/b181e394-326a-4ca3-a455-10bd84d69a30/market?currency=USD&country=US'

'b181e394-326a-4ca3-a455-10bd84d69a30'

'https://stockx.com/api/products/57c2cdc3-e398-4661-8bb2-a975c0a00710/activity?state=400&currency=USD&limit=100&page=1&sort=amount&order=ASC&country=US'

'https://stockx.com/api/products/57c2cdc3-e398-4661-8bb2-a975c0a00710/activity?state=300&currency=USD&limit=100&page=2&sort=amount&order=DESC&country=US'

'https://stockx.com/api/products/57c2cdc3-e398-4661-8bb2-a975c0a00710/activity?state=400&currency=USD&limit=100&page=1&sort=amount&order=ASC&country=US'

'https://stockx.com/api/products/57c2cdc3-e398-4661-8bb2-a975c0a00710/market?currency=USD&country=US'
