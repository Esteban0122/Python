# Repaso de Tuplas, Conjuntos y Diccionarios

# TUPLAS:

#tupla = (1.0, 2, 'esteban', True, 10, 11, 11, 11)    # El True se reconoce como el 1
# print(tupla)

# for var in tupla:
#     print(var, end =' ')
# print()
# print(tupla.count(11))   # cuenta los elementos 11 repetidos

# print(tupla)
# lista = list(tupla)
# print(lista)
# tupl = tuple(lista)
# print(tupl)



# CONJUNTOS
# A = set()
# A = {1, 1, 2, 3, 4, 4, 5, 5 ,5}
# print(type(A))
# print(A)
# A.add(6)
# print(A)
# A.discard(2)
# print(A)
# A.discard(2)    # Esta funcion saca al 2 pero ya se descartó y no se muestra nada 
# print(A)
# A.remove(2)    #Esta funcion saca un elemento pero si ya no está sale error
# print(A)

#Operaciones con conjuntos

# A = set()
# A = {1,2,3,4,5}
# B = set()
# B = {4,5}

# C = A|B  # Union
# print(C)
# C = A&B   # interseccion
# print(C)


# print(A.isdisjoint(B))
# print(A.issubset(B))
# print(A.issuperset(B))




#DICCIONARIOS
# per = {
#     48147571:['Esteban', 'Figueroa',23], 
#     41313651:['Jose', 'Armando', 42]}
# print(per)

# per[76120560] = ['Juan','Campos', 50]
# print(per)

# for position, key in enumerate(per):
#     print(position +1, key)





# FUNCIONES
#Es un bloque de codigo que se puede reutilizar en cualquier lugar.
# variable = 27

# def saludar(nombre, edad):          # las variables deben estar dentro de la funcion porque tienen alcance local
#     global variable
#     variable +=2
#     print(f'Hola {nombre} tienes {edad} años')
#     print(variable)

# def salir():
#     print('Nos vemos')


# saludar('Esteban', 23)
# salir()

#Nota:
#las variables deben definirse dentro de una funcion ya que son locales, para evitar ese 
# problema se soluciona con global.
#solo las variables deben definirse con global si no estan definidos dentro de una funcion
# en cambio los objetos (listas, conjuntos) si se pueden definir fuera de la funcion
# ya que lo hacen por referencia.








