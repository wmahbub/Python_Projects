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

consolidated.to_csv('nba_stats_salary1.csv', index = False)