#bucles
 #while 6 > 5:
#    print('Hello world')
num= int(input('Ingresa un numero entero para calcular\
    su factorial: '))
factorial = num
aux = num
while num > 1:
    num -= 1
    factorial = factorial*num

print(f'{aux}! = {factorial}')

#while True:
 #   num = int(input("Ingresa un numero entero para calcular su factorial: "))
  #  if num < 0:
   #     print("Error! El numero debe ser positivo o cero")
    #elif num == 0:
     #   print("0! = 1")
      #  break
    #else:
     #   factorial = num
      #  aux = num

       # while num > 1:
        #    num -= 1
         #   factorial = factorial*num

        #print(f'{aux}! = {factorial}')
        #break

# vamos a usar la funcion range
# te devuelve una lista de valores segun el parametro

#for x in range(2,5):
 #   print(x, end = " ")
#print()

#for x in range(7):
 #   print(x, end =" ")
#print()

#for x in range(0,7):
 #   print(x)
 
#for x in range(0,10,2):
 #   print(x)

#for x in range(10, 0, -1):
 #   print(x, end = " ")

#name = 'esteban'
#for char in name:
 #   print(char)

#  Colecciones
#  En python no existen los vectores pero si existen las listas\
#  donde se pueden guardar cualquier tipo de datos es decir se \
#  pueden guardar numeros, caracteres, listas, flotantes, enteros etc.

# Listas
#lista = [1, 2, True, 3.0, 'esteban', [0, 1, 2.0]]
# print(lista)
#for x in lista:
   # print(x, end = " ")
#print (lista[3])
#print(lista[0:3])
#print(list[0:5,2]) corregir

# lista.append ('hola') # agrega un elemento a la lsita
# print(lista)
# lista.pop(1) # elimina un elemento de la lista en la posicion 1
# print(lista)
# print(len(lista))
# print(lista[-2:-8:-1])