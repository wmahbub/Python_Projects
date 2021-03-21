import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import datetime
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df1= pd.read_csv('sale_history.csv')
df1[['Date','Time']] = df1['createdAt'].str.split('T', expand= True)
df1[['Time', 'xxx']] = df1['Time'].str.split('+', expand=True)

df1 = df1.drop(['createdAt', 'xxx', 'state', 'customerId', 'localAmount', 'localCurrency', 'productId'], axis=1)
df1['Date'] = pd.to_datetime(df1['Date'], format = '%Y-%m-%d')
df1['Time'] = pd.to_datetime(df1['Time'], format= '%H:%M:%S')

a= df1.sort_values(by= ['shoeSize', 'Date', 'Time'], ascending=[True, False, False]).groupby(by='shoeSize', as_index= False)['amount'].first()

print(df1.head(5))
print(a.head(20))

#df1.to_csv('formated_table.csv', index= False)



