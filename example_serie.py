import pandas as pd

list_ice_cream = ['lemon', 'Chocolate', 'Vainilla']
series= pd.Series(list_ice_cream)
print(f'Esten es el contenido de la serie \n {series}')

#indice personalizado
index=['a','b','c']
serie_2=pd.Series(list_ice_cream,index)