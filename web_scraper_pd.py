import pandas as pd

url= 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'

df = pd.read_html(url, header = 0)

df2019 = df[0]


aa = df2019.drop(df2019[df2019['Age'] == 'Age'].index )

print(aa.shape)