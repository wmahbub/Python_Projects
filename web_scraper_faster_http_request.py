import requests
from bs4 import BeautifulSoup
import datetime

def gettitle(x):
    
    url = f'https://scrapethissite.com/pages/forms/?page_num={x}'
    
    r = s.get(url)
    
    soup = BeautifulSoup(r.text, 'html.parser')
    
    print(soup.title.text)
    
    return


def gettitle_session(x):

    url = f'https://scrapethissite.com/pages/forms/?page_num={x}'

    r = s.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.title.text)

    return


# no sessions - 0:00:04.013268

if __name__ == '__main__':
    
    s = requests.Session()
    
    start = datetime.datetime.now()
    
    for x in range(1,21):
        gettitle_session(x)
    
    finish = datetime.datetime.now() - start
    
    print(finish)
