import pandas as pd

good_student_qualities=['Self_Dicipline','Self-Dicpline','self-Oriented','Punctuality','Diligence and hard work','respectful','passive']
serie=pd.Series(good_student_qualities)
print (serie)
#El tamaño de la serie
print(f'el tamaño de la serie es el siguiente:{serie.size}')
#La serie tiene valores duplicados
print(f'la serie tiene valores duplicados:{serie.is_unique}')
#informacion de los indices
print(f'Este atributo muestra informacion de los indices:{serie.index}')
#Informacion del almacenamiento de los valores de la serie 
print(f'informacion de los valores de la serie :{serie.values}')
#Informacion del tipo de datos que se utilizan para almacenar los valores de la serie
print(f'Tipo de taos:{type(serie.values)}')