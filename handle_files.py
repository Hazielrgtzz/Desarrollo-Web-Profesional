#new_file = open C:\Archivo\ Archivo.txt
#new_file.write("Hello world\n")
#new_file.write("Hola mundo\n")
#new_file.write("Hola UTVT\n")
#new_file.close()

path= 'C:\Archivo\Archivo.txt'
new_file =open(path, 'r')
data = new_file.readlines()
print(data)
one_line = new_file.readline()
print(one_line)
print(one_line)

#for line in data:
# print(line)

except Exception as e:
print (e)