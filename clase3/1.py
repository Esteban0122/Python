#x=10
#x += 1  # x =x +1
#print(x)
#x -=1   # x = x -1
#print(x)
#x /=3  # x = x/3
#print(x)
#x *= 3  # x = x*3
#print(x)
#print(type(x))
#name = 'esteban'
#print(len(name))
#age = 23
#print(name, 'is', age , 'years old')
#print('{} is {} years old.'. format(name,age))
#print(f'{name} is {age} years old.')

#v = 5 < 3
#print(v)

#v = 3 > 1
#print (v)
#print(type(v))

#v = (not 5 < 10 ) or 3 > 5
#print(v)
#v = 3 < 5 and 2 < 8
#print(v)

#name = input('What\'s your name?')
#age = int(input(f'Hi {name}, how old are you?'))

#if  age < 18:
    #print('You\'ll not pass')
#else:
   # print('You are allowed to pass.')


#if age < 0:
    #print('Error! An age can\'t be negative')
#elif age < 18:
   # print('You shall not pass')
#else:
 #   print('You are allowed to pass')

# calculadora de area de un círculo
#import math

#print('Vamos a calcular el área de un círculo')
#radio = int(input('Ingresar un radio:'))

#if radio < 0:
 #   print('Error!! el radio ingresado es negativo')
#else: 
 #   area = math.pi*radio**2
  #  print('El área del círculo es: ', area)

#tipo_letra = input('El tipo de letra: ')
#print(tipo_letra)
#print(tipo_letra.lower())
#print(tipo_letra.upper())


# programa que indica si hay vocales

letra = input('Introduce una letra: ').lower()
if len(letra) > 1:
    print('Error!! solo introduzca una letra')
elif letra == 'a' or letra == 'e' or letra == 'i' \
 or letra == 'o' or letra =='u':
    print('Es una vocal')
else: 
    print('Es una consonante')

