# Como clonar un repositorio:
# git clone url     genera una carperta con el nomnbre respectivo(name)
# cd "name"
# git status
# git commit
#...


# bucles y colecciones II

# Factorial de un numero con un contador que va en aumento ademas
# se pregunta si deseamos continuar o no con el cálculo

# while True:
#     num = int(input('Ingrese un numero: '))
#     if num < 0:
#         print('Error! Ingrese un numero positivo')
#     else:
#         cont = 1
#         factorial = cont
#         while num > cont:
#             cont += 1
#             factorial = factorial*cont
#     print(f'{num}! = {factorial}')

#     while True:
#         answer = input('Have you finish ? (y/n)')
#         if answer != 'y' and answer != 'n':
#             print('Error! The value must be y or n')
#         else:
#             break
    
#     if answer == 'y':
#         break
#     else:
#         factorial =1

# For

# range(x)     devuelve  una lista desde 0 hasta antes de x
# range(x, y)   devuleve una lista desde x hasta antes de y
# range(x, y , z)  devuelve una lista de x hasta y de z en z

# for var in range(3, 10, 2):
#     print(var, end =' ')
# print()

# for var in range(3,7):
#     print(var, end=' ')
# print()

# for var in range(10, 2, -1):
#     print(var, end =' ')
# print()

#   COLECCIONES
# LISTAS

lista= [1, 2, 0.5, 7, 'esteban', True, 10]
# print(lista)
# print(type(lista))
# print(len(lista))
# print(lista[4])  # siempre se cuenta desde el cero
# print(lista[3:6])   # imprime una sublista desde el orden 3 hasta el 6
# print(lista[3:6:2])   # imprime una sublista del 3 hasta el 6 de 2 en 2
# elemento = lista[-1]   # se empieza a contar desde el final 
# print(elemento)

# lista2 = lista[-1:-5:-1]   # recorre desde el orden -1 hasta el -5 de 1 en 1
# print(lista2)
    
# lista.append('hola')
# print(lista)
# lista.pop(3)
# print(lista)
# lista[3] = 'anthony'   # reeplazar por el orden 3 la palabra anthony
#print(lista)

# TUPLAS

tupla = (8, 2.0, True, 'esteban', 11, 22, 1, 1, 1)
for value in tupla:
    print(value, end=' ')
print()
# tupla[0] = 2
# print(tupla)

# print(tupla.count(2.0))  # imprime el orden del parametro
# lista = list(tupla)
# print(lista)
# lista = tuple(lista)
# print(lista)

# CONJUNTOS

# conjunto = set()
# conjunto = {1,2,3,1,2,4,5,5,5}
# print(conjunto)
# conjunto.add(6)    # se agrega un elemento al conjunto
# print(conjunto)
# conjunto.discard(1)  # se elimina el numero 1
# print(conjunto)
# conjunto.remove(1)
# print(conjunto)

# Operaciones con Conjuntos

# A= set()
# A={1, 2, 3, 4, 5, 5}
# B = set()
# B= {4, 5, 8, 11}

# C= A|B  # union
# print(C)

# C = A&B  # interseccion
# print(C)

# C= A^B  # dif. simétrica
# print(C)

# C= A -B  # dif 
# print(C)

# print(A.isdisjoint(B))   # para ver si hay interseccion
# print(A.issubset(B))   # para ver si B es subconjunto de A
# print(A.issuperset(B))   # para ver si A contiene a B

# DICCIONARIOS
# key     value
# clave1: valor1
# clave2: valor2
# clave3: valor3
# clave4: valor4
# ejemplo  pag    informacion

dic = {'anthony':'Luzquiños', 'Alvaro': 'Plasencia', 'Ruben': 'Ricapa', 'Esteban':'Figueroa'}
# print(dic)
# keys= list(dic.keys())
# values = list(dic.values())
# print(keys)
# print(values)

# for var in dic:
#     print(var, end= ' ')
#     print(dic[var])
# for x, key in enumerate(dic):
#     print(x, key)

# dic['Carlos'] = 'Bazan'
# print(dic)
# dic.pop('Alvaro')
# print(dic)

# Tarea, simular una agenda, que tenga agregar contacto, elimnina y muestrar contacto.