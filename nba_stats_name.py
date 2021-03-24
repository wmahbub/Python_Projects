import pandas as pd

consolidated = pd.DataFrame(columns=['RK', 'NAME', 'TEAM', 'SALARY', 'POS', 'SEASON'])


for year in range(2016, 2021, 1):
    
    data = pd.read_html(f'http://www.espn.com/nba/salaries/_/year/{year}', header=0)[0]

    df= pd.DataFrame(data)
    df = df.set_index((['RK']))
    df = df.drop('RK')
    df = df.reset_index()
    df[['NAME', 'POS']] = df['NAME'].str.split(', ', expand= True)
    df['SEASON'] = year
    consolidated = consolidated.append(df, ignore_index= True)

names = consolidated['NAME'].unique()

names = pd.DataFrame({'Names': names } )

names[['first_name', 'last_name', 'xxx']] = names['Names'].str.split(' ', expand= True)
names = names.drop('xxx', axis=1)

names['first_name'] = names['first_name'].str.replace("'", '')

names['part_1'] = names['last_name'].str[0].str.lower()

names['link'] = 'https://www.basketball-reference.com/players/'+ names['part_1'] + str('/') + names['last_name'].str[0:5] +  names['first_name'].str[0:2] + str('01') + str('.html')

names['link'] = names['link'].str.lower()


print(names)

names.to_csv('nba_stats_player_names.csv')
