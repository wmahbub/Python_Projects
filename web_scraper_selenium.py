from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://stockx.com/air-jordan-1-mid-signal-blue-td'

driver = webdriver.Chrome(r'D:\Programs\Chrome Driver\chromedriver_win32_88\chromedriver.exe')

driver.get('https://stockx.com/air-jordan-1-mid-signal-blue-td')

link = driver.find_element_by_link_text('View All Asks')
link.click()

element_html = link.get_attribute('innerHTML')

print(element_html)