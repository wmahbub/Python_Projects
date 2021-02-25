import pandas as pd

df = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti',parse_dates=True, skiprows=0)

print(df[0].head(10))

df[0].to_csv('lsr.csv')
