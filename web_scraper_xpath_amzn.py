from requests_html import HTMLSession
import datetime


url_list = [
    'https://www.amazon.com/HP-15-dh1054nr-Gaming-i7-10750H-GeForce/dp/B08CBNKQ3K/ref=sr_1_3?dchild=1&keywords=hp+omen+laptop&qid=1614219523&refinements=p_n_feature_five_browse-bin%3A13580790011&rnid=2257851011&s=pc&sr=1-3',
    'https://www.amazon.com/dp/B08WYJSW5D/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B08WYJSW5D&pd_rd_w=5jjKy&pf_rd_p=4269e1a0-a218-4fbd-9748-1cd337d2f2a5&pd_rd_wg=angCI&pf_rd_r=DS05XZ4T3TC0T3Z8SP4C&pd_rd_r=7fd8c974-a699-4127-b279-67a1370c7ed3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNTlHV0pYOE1LT09FJmVuY3J5cHRlZElkPUEwODUxNTY5MlRaQkpDVEoxTlBHNyZlbmNyeXB0ZWRBZElkPUEwMjk4ODk5MTNFTDFFTDJUUzBMWiZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=',
    'https://www.amazon.com/dp/B0892Q7JLN/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B0892Q7JLN&pd_rd_w=Gv0qw&pf_rd_p=4269e1a0-a218-4fbd-9748-1cd337d2f2a5&pd_rd_wg=fs0TC&pf_rd_r=WH5WEMVA9T6C9B8T5W63&pd_rd_r=c838dff9-cd29-472c-acab-caddf5616aaa&smid=A2TC87EJKQMY9O&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNVJLREs4MUwzNUJZJmVuY3J5cHRlZElkPUEwNzYzNDU4MzhUMVlVNkRLS084WiZlbmNyeXB0ZWRBZElkPUEwOTgxMDA5MVI4MFJDTDlQQU4zNCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    ]

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep = 1)
    
    product = {'title': r.html.xpath('//*[@id="productTitle"]', first = True).text.strip(), 
               'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first = True).text.strip()
    }
    
    return product

prices = []

start = datetime.datetime.now()
for url in url_list:
    prices.append(getPrice(url))

end = datetime.datetime.now()

print('Completed normal in: ', str(end-start))
print(prices)
