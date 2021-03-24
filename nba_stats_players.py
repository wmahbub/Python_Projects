import pandas as pd

data = pd.read_html('https://www.basketball-reference.com/players/j/jamesle01.html', header= 0)[0]

# 'https://www.basketball-reference.com/players/c/curryst01.html'

df = pd.DataFrame(data)

df = df.set_index((['Season']))
df = df.drop(['Career'], axis= 0)
df = df.reset_index()
df[['Season', 'xxx']] = df['Season'].str.split('-', expand= True)
df = df.dropna(axis= 0)
df = df.drop('xxx', axis= 1)
df['Season'] = df['Season'].astype('float64', errors='ignore')


print(df[df['Season']>=2016])
