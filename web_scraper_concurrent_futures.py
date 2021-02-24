import requests
from bs4 import BeautifulSoup
from csv import reader
import pandas as pd
import datetime
import concurrent.futures

urls = []
titles = []

with open(r'C:\Users\wajda\Desktop\Chris Project\speedupscraping-master\bookslinks.csv', 'r') as file:
    
    csv_reader = reader(file)
    
    for row in csv_reader:
        urls.append(row[0]) # row[0]

def transform(url):
    
    r = requests.get(url) # str(url)
    
    soup = BeautifulSoup(r.content , 'html.parser')
    
    title = soup.find('h1').text.strip()
    titles.append(title)
    print(title)
    
    return 

start = datetime.datetime.now()

#for url in urls: # remove urls index to get whole list of titles
    #transform(url)

#for i in range(0,10):
    #transform(urls[i])
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(transform, urls)

df = pd.DataFrame(titles)
df.to_csv('standard_booktitles.csv', index= False)

finish = datetime.datetime.now()

print('Complete ' + str(len(titles)) + ' in ' + str(finish - start) )
    
