import pyppdf.patch_pyppeteer
from requests_html import HTMLSession


url = 'https://www.beerwulf.com/en-gb/c/all-beers?segments=Beer&catalogCode=Beer_1'

s = HTMLSession()

r = s.get(url)

r.html.render(sleep = 1)

products = r.html.xpath('//*[@id="product-items-container"]', first= True) # this is XPath copied from Chrome

for item in products.absolute_links:
    r = s.get(item)
    
    name = r.html.find('div.product-detail-info-title', first=True).text.strip()
    subtext = r.html.find('div.product-subtext', first=True).text.strip()
    
    try:
        rating = r.html.find('span.label-stars', first=True).text.strip() # some don't have ratings so use try-except 
    
    except:
        rating = 'None'
        
    if r.html.find('div.add-to-cart-container'):
        stock = "In Stock"
    
    else:
        stock = "Not In Stock"
    
    print(name, subtext, rating, stock)
    
    
