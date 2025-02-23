result=None 

numero_x=10
numero_y=1 
try: 

 numero_x=int(input('Ingresa un numero para x: '))
numero_y=int(input('Ingresa un numero para y: '))

result=numero_x/ numero_y
print(f' El resultado de la división es:{result}')
except ZeroDivisionError as e:
print(f' La excepcion es la equivalente:{e}')
except ValueError as e:
print(f' La excepcion ValueError genero el siguiente mensaje:{e}')
except Exception as e:
print(f' La excepcion Exception generó el siguiente mensaje:{e}')
finally:
print('Nuestro programa ha finalizado')
    
    