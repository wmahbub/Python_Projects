
import requests
from bs4 import BeautifulSoup
import pandas as pd

# ETL (Extract - Load - Transform) Approach

def extract(page):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=python+developer&l=Dorchester,+MA&start={page}'
    
    r = requests.get(url, headers)
    
    soup = BeautifulSoup(r.content ,  'html.parser')
    
    return soup


def transform(soup):
    
    divs = soup.find_all('div' , class_= 'jobsearch-SerpJobCard')
    
    for item in divs:
        title =item.find('a').text.strip()
        company = item.find('span', class_ = 'company').text.strip()
        
        try:
            salary = item.find('span', class_='salaryText').text.strip()
        
        except:
            salary = ''
        
        summary = item.find('div', class_ = 'summary').text.strip().replace('\n', '')
        
        #summary = item.find('div', {'class': 'summary'} ).text.strip() use for ID tag
        
        job= {'title': title, 'company': company, 'salary': salary, 'summary': summary}
        
        joblist.append(job)
    
    return
        
        
joblist= []       

  
for i in range(0 , 40, 10):
    print( f'Getting Page...{i}')
    c = extract(i)
    transform(c)


df = pd.DataFrame(joblist)
print(df.head(10))

df.to_csv(r'C:\Users\wajda\Desktop\Chris Project\jobs.csv')
df.to_csv('jobs.csv')
