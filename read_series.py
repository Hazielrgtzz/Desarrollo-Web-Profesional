import pandas as pd

nba_players = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', sep=',', usecols=['Name']).squeeze()

#Funcion describe
print(f'Funcion describe con una seria: \n {nba_players.describe()}')

#Funcion head
print(f'Primeros 5 elementos de una serie: \n {nba_players.head()}')
print(f'\n\nPrimeros 10 elementos de una serie: \n {nba_players.head(10)}')

#Funcion tail
print(f'\n\n\nUltimos 5 elementos de una serie: \n {nba_players.tail()}')
print(f'\n\nUltimos 10 elementos de una serie: \n {nba_players.tail(10)}')