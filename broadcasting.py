import pandas as pd
from numpy.ma.core import subtract

nba_players = pd.read_csv('C:\\DataFiles\\nba_players_a.csv', usecols=['DRtg']).squeeze()
some_values = nba_players.iloc[:5]

addition_1 = some_values + 10
addition_2 = some_values.add(10)

print('Realizacion de la suma')

print(some_values)
print(addition_1)
print(addition_2)

print('Realizacion de la resta')
subtract_1 = some_values - 10
subtract_2 = some_values.sub(10)

print(subtract_1)
print(subtract_2)

#Realizar la operacion para la multiplicacion y resta
print('Realizacion de la multiplicacion')
multi_1 = some_values * 10
multi_2 = some_values.mul(10)

print(multi_1)
print(multi_2)

print('Realizacion de la division')
div_1 = some_values / 10
div_2 = some_values.div(10)

print(div_1)
print(div_2)