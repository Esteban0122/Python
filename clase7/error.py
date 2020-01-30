# Excepciones
# MANEJO DE ERRORES
# number = int(input('Type of number: '))
# print(number)

# while True:
#     try:
#      number = int(input('Type a number: '))
#     except ValueError:
#      print('The number you\´ve just typed is not an integer.')
#     else:
#         print(number)
#         break           # rompe el bucle
#     finally:
#         print('I\´m being always executed.')
#     # El finally tiene una jerarquía mayor al break.



# Implementar un algoritmo  que calcule el área de un triángulo
# usando Herón.
# import math
# print('Cálculo del área de un Triángulo según Herón')
# print('Ingresar tres lados de un triángulo: ')


# def area(a,b,c):
#     if a > 0 and b > 0 and c > 0:
#        s = (a + b +c)/2
#        A = math.sqrt(s*(s-a)*(s-b*(s-c)))
#        print(f'El área del triángulo es {A}')
#     else:
#         print('Uno de los lados es negativo, vuelva a ingresar los lados')


# while True:
#     try:
#         a = int(input('lado a = '))
#         b = int(input('lado b = '))
#         c = int(input('lado c = '))
#     except ValueError:
#         print('El número ingresado no en entero.')
#     else:
#         area(a,b,c)
#         break









# Otra forma de calcular:
# AREA DE UN TRIANGULO SEGUN HERON


# import math

# # Error codes:
# # 1 -> correct number
# # 2 -> it's not a number
# # 3 -> the number is less than 0 or 0


# def positive_number(number):

#     if number <= 0:
#         return 3
#     else: 
#         return 1


# def validate_number(possible_number):

#     try:
#         possible_number = float(possible_number)
#     except ValueError:
#         return 2
#     else:
#         return positive_number(possible_number)


# def validate_triangle(triangle):

#     # if math.fabs(triangle[0] - triangle[1]) < triangle[2] \
#     #     and triangle[2] < triangle[0] + triangle[1]:

#     #     if math.fabs(triangle[1] - triangle[2]) < triangle[0] \
#     #         and triangle[0] < triangle[1] + triangle[2]:

#     #         if math.fabs(triangle[0] - triangle[2]) < triangle[1] \
#     #             and triangle[1] < triangle[0] + triangle[2]:

#     #             return True
    
#     p = 0

#     for i in range(0, 3):
#         p += triangle[i]

#     p /= 2

#     if triangle[0] < p and triangle[1] < p and triangle[2] < p:
#         return True

#     return False


# def heron():
    
#     triangle = [0]*3 # triangle = [0, 0, 0]
#     validator = ''
#     p = 0
#     aux = 0

#     while True:
#         for index in range(0, len(triangle)):
#             while True:
#                 triangle[index] = input('Type a number: ')
#                 validator = validate_number(triangle[index])

#                 if validator == 1:
#                     triangle[index] = float(triangle[index])
#                     break
#                 elif validator == 2:
#                     print('The value you\'ve just typed is not an number')
#                 else:
#                     print('The number is negative or 0.')
        
#         result = validate_triangle(triangle)

#         if result:

#             for i in range(0, 3):
#                 p += triangle[i]

#             p /= 2
#             aux = p

#             for i in range(0, 3):
#                 p *= (aux - triangle[i])

#             return math.sqrt(p)
#         else:
#             print('It isn\'t a triangle.\nTry again: ')


# print(f'The triangle\'s area is: {heron():.5f}u².')


