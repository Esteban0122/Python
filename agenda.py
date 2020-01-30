# # Activity:
# # 1. Generate a menu with the functions programmed before and it ends when the 
# # user types a 0.
# # 2. DOCUMENT THE FUNCTIONS WE HAVE HERE.





# # Diccionario que hace de agenda
# dic = {'Anthony': ['Luzquiños', '976015297', 'ALuzquiños@uni.pe'],
#         'Ruben':  ['Ricapa', '879046582', 'rubenillo@uni.pe']}


# #Nombre : [Apellidos, numero, correo]
# def mostrar_contacto():
#     print('Contactos: ')
#     for position, key in enumerate(dic):
#         print(position +1, key, dic[key])


# def agregar_contacto(nombre):
#     apellido = input('Ingresa apellido: ')
#     cel = input('Ingresa un numero: ')
#     correo = input('Ingresa correo: ')
#     dic[nombre] = [apellido, cel, correo]
#     #mostrar_contacto()


# def buscar_contacto(nombre):
#     if nombre in dic:
#         print('Contacto encontrado: ')
#         print(nombre, dic[nombre])
#     else:
#         print('No existe el contacto')
    
#     print()


# def eliminar_contacto(nombre):
#     dic.pop(nombre)
#     #mostrar_contacto()


# #mostrar_contacto()
# #agregar_contacto('Adan')
# #mostrar_contacto()
# #buscar_contacto('Ruben')

# # mostrar_contacto()
# # eliminar_contacto('Anthony')









# # ACTIVIDAD:
# #Generar un menú con las funciones antes programadas y que termine cuando
# # ingresas un cero.

# # Dictionary that represents an agenda

# dic = {
#     'Anthony': ['Luzquiños', '936962826', 'sluzquinosa@uni.pe'],
#     'Rubén': ['Ricapa', '987654321', 'rubenillo@uni.pe']
# }

# # Codes
# # 1 -> valid number
# # 2 -> it doesn't begin with 9, but it has 9 numbers
# # 3 -> it begins with 9, but it doesn't have 9 numbers

# def nine_numbers(number):

#     '''
#         DOCUMENTACIÓN DE LA FUNCIÓN
#     '''
#     number = str(number)
#     if len(number) == 9 and number[0] == '9':
#         return 1 # accepted
#     elif len(number) == 9 and number[0] != '9':
#         return 2
#     elif len(number) != 9 and number[0] == '9':
#         return 3
#     else:
#         return 4


# def verify():

#     while True:
#         try:
#             number = int(input('Type a cellphone number: '))
#         except ValueError:
#             print('That\'s not a valid cellphone number.')
#         else:
#             code_validation = nine_numbers(number)
#             if code_validation == 1:
#                 return number
#             elif code_validation == 2:
#                 print('Error! The cellphone must begin with nine')
#             elif code_validation == 3:
#                 print('Error! The number must have 9 digits.')
#             else:
#                 print('Error! The number you\'ve just typed neither has 9 '
#                         + 'digits nor begin with nine.')


# def show_contacts():

#     print('Contact list:')
#     for position, key in enumerate(dic):
#         print(position + 1, key, dic[key])
#     print()


# def add_contact(name):

#     lastname = input('Lastname: ')
#     cell = verify()
#     mail = input('Email: ')
#     dic[name] = [lastname, cell, mail]
#     show_contacts()


# def search_contact(name):

#     if name in dic:
#         print('Contact found:')
#         print(nombre, dic[nombre])
#     else:
#         print('The searched contact does not exist')
#     print()


# def delete_contact(name):
    
#     dic.pop(name)
#     show_contacts()

# contact_name = input('Type a name: ')
# add_contact(contact_name)

        
