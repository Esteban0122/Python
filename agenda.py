# Diccionario que hace de agenda
dic = {'Anthony': ['Luzquiños', '976015297', 'ALuzquiños@uni.pe'],
        'Ruben':  ['Ricapa', '879046582', 'rubenillo@uni.pe']}


#Nombre : [Apellidos, numero, correo]
def mostrar_contacto():
    print('Contactos: ')
    for position, key in enumerate(dic):
        print(position +1, key, dic[key])


def agregar_contacto(nombre):
    apellido = input('Ingresa apellido: ')
    cel = input('Ingresa un numero: ')
    correo = input('Ingresa correo: ')
    dic[nombre] = [apellido, cel, correo]
    #mostrar_contacto()


def buscar_contacto(nombre):
    if nombre in dic:
        print('Contacto encontrado: ')
        print(nombre, dic[nombre])
    else:
        print('No existe el contacto')
    
    print()


def eliminar_contacto(nombre):
    dic.pop(nombre)
    #mostrar_contacto()


#mostrar_contacto()
#agregar_contacto('Adan')
#mostrar_contacto()
#buscar_contacto('Ruben')

# mostrar_contacto()
# eliminar_contacto('Anthony')


# ACTIVIDAD:
#Generar un menú con las funciones antes programadas y que termine cuando
# ingresas un cero.

print('Menú de Contactos')
print()

numero = int(input('Elija un número: '))

while True:
    if numero == 1:

        
