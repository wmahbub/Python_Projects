import requests
import random

url_test_header = 'https://httpbin.org/headers'
url_test_ip = 'https://httpbin.org/ip'
url_actual1 = 'https://finance.yahoo.com/quote/AMZN/'
url_actual2 = 'https://finance.yahoo.com/quote/MSFT/'

names = ['Josh', 'Aakash', 'Karthik', 'Mahesh', 'Vinay', 'David', 'Bruno', 'Jason', 'Jack', 'Chris', 'Rishi', 'Pranav', 'Julia', 'Evgeny', 'Dan']
referers = ['https://www.google.com/', 'https://www.bing.com/', 'https://search.yahoo.com/', 'https://yandex.com/', 'https://duckduckgo.com/']

user_agents = [

'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36' ,
'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
]
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'

header = {
    'User-Agent': random.choice(user_agents),
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': random.choice(referers),
    'DNT' : '1',
    'user': random.choice(names)
    }

proxy = {
    'http': 'http://143.198.2.174:3128',
    'https': 'http://143.198.2.174:8080'
    }

r1 = requests.get(url_test_header, headers= header, proxies= proxy)
r2 = requests.get(url_test_ip, headers=header, proxies=proxy)
r3 = requests.get(url_actual1, headers=header, proxies=proxy)
r4 = requests.get(url_actual2, headers=header, proxies=proxy)

print(r1.text)
print(r2.text)

print('Test: ', (r1.status_code, r2.status_code) , 'Actual: ', (r3.status_code, r4.status_code))