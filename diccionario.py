<<<<<<< HEAD
import pandas as pd
kid_gifts={
    'videogames':'Play 5',
    'boardgames':'monopoli'
}

serie =pd.Series(kid_gifts)

print(f'\n{serie}')
=======
#Declarar un diccionario en Python

student = {
    'name': 'Pedrito Perez',
    'age': 25,
    'language': 'python',
    'city': 'lerma',
}

#Acceso a los valores de un diccionario
print(f'Contenido total del estudiante:  {student}')
print(f'Nombre: {student["name"]}') 
print(f'Edad: {srudent.get("age")}')


print('...Operaciones basicas sobre diccionarios ...')
#Modificar los valores de un diccionario
student['language'] = 'C#'
print(f'Contenido actual del estudiante:  {student}')

#Eliminar un elemento de un diccionario
student.pop('city')
print(f'Contenido del estudiante una vez eliminada la ciudad: {student}')

#Agregar un nuevo elemento
student ['food'] = 'galletas'
print(f'Contenido del estudiante una vez agregada una nueva propiedad: {student}')

print('\n\n\n---Iterar sobre un diccionario ---')
print('\iteracion de los elementos de un diccionario, simple ')

for element in student:
print(f'{element}: {student[element]}')

print('\nIteracion de los elementos de un diccionario, destructuración - unpacking ')

for key, value in student.items():
print(f'LLave: {key}, Valor: {value}')

print('\n\nIteracion de los elementos de un diccionario, Llaves')

for key in student.keys():
print(f'LLave: {key}')

print('\n\nIteracion de los elementos de un diccionario, valores ')
for value in student.values():
    print(f'valor: {value}')
>>>>>>> 7c9fd45 (Clase08/02)
