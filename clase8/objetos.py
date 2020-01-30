# Es un paradigma que trata de imitar el comportamiento del mundo real.
# Clase: es un modelo, molde o plantilla.
# Ejemplar de Clase, Objeto o Instancia: es una clase en particular 
# con caracteristicas y funciones(metodos).
# Modularizacion: Es cuando se pueden separar varias clases de manera 
# independiente.

# Clase:
#     -> Son abstracciones de las cosas de la vida cotidiana.
#     -> Moldes o plantillas para crear objetos.

# Objeto:
#     -> Un ejemplar de una clase en particular.
#     -> Una instancia de una clase.


#.................



# class Person():
#     name = 'Anthony'
#     age = 23
    
# person_1 = Person()
# print(person_1.name)

#...............................

# class Person():
#     def __init__(self, name, last_name, age):    # Constructor inicializa todos los parametros de la Clase,
#         #Atributos
#         self.name = name              # Self indica las caracteristicas de un objeto.
#         self.last_name = last_name
#         self.age = age                

    
#     def greet(self):
#         return  'Hi! My name is ' + self.name +' ' + self.last_name + ', I\'m ' + str(self.age) + 'years old.'



# person_1 = Person('Anthony','Luzquiños', 23)
# person_2 = Person('Ruben','Ricapa', 15)

# print(person_1.greet())
# print(person_2.greet())


#.................................

## CREAR CLASE CARRO:

# class Carro():
#     def __init__(self, marca, año, color):
#         self.marca = marca
#         self.año = año
#         self.color = color


#     def encender(self):
#         print('¿Usted desea enceder el auto?')
#         opcion = input('Escribir yes o no : ')
#         print()
#         if opcion == 'yes':
#             print('El auto se ha encendido')
#         else:
#             print('El auto está apagado!')

    
#     def acelerar(self):
#         print('¿Desea acelerar?')
#         print()
#         a = input('Presione A para ir acelerando: ')
#         v=0
#         while a == 'A':
#             v +=10
#             print(f'La aceleración es: {v}')



# carro_1 = Carro('Tesla', 2018, 'negro')


# print(carro_1.encender())
# print(carro_1.acelerar())


# por terminar......






#.........................................

## Otro ejemplo
  # En clase (ver repositorio)


# class Car():

#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
#         self.speed = 0
#         self.status = 'off'
    
#     def turn_on(self):
#         if self.status == 'on': 
#             print('The car is already turned on.')
#         else:
#             self.status = 'on'
#             print('The car is now turned on.')
    
#     def acelerate(self):
#         if self.status == 'on':
#             self.speed += 10
#             print('Now, the speed is:', self.speed)
#         else:
#             print('The car is turn off, you must turn on it')
    
#     def brake(self):
#         if self.speed == 0:
#             print('The car is already stopped')
#         else:
#             self.speed = 0
#             print('Now, the car has stopped')
    
#     def turn_off(self):
#         if self.status == 'off': 
#             print('The car is already turned off.')
#         else:
#             self.status = 'off'
#             print('The car is now turned off.')

#     def __str__(self):
#         return 'Modelo: '+self.model+'\nMarca: '+self.brand

# car_1 = Car('Grand Prix', 'Pontiac')

# print(car_1)
# car_1.turn_on()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.acelerate()
# car_1.brake()
# car_1.turn_off()


# ............................
# PASO POR REFRENCIA Y POR VALOR:

#PASO POR REFRENCIA (OBJETOS)
# lista =[1,2,3]
# lista2 = lista
# lista2.append(4)
# print(lista)


# # PASO POR VALOR (VARIABLES)
# a = 4
# b = a
# b +=1
# print(b)
# print(a)








