result=None 

numero_x=10
numero_y=1
try:

    result=numero_x/ numero_y
    print(f'el resultado de la division es: {result}')
except ZeroDivisionError as e:
 print(f'La excepcion es la equivalente: {e}')
finally:
 print('Nuestro programa ha finalizado')