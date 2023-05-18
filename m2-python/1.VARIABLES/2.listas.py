


'''
tipos de datos compuestos
'''

nifs = ['3456545L', '4565768t']
print (nifs)

validos = [True, False, True, False]
print(validos)

lista_heterogenea = [1, 'texto', True, 29.9]
print(lista_heterogenea)

precios = [9.99, 23.43, 54.56]
print(precios)

emails = ['user1@gmail.com', 'user2@gmail.com', 'user3@gmail.com']
print(emails)

telefonos = ['654321123', '678654567', '654356784']
print(telefonos)

contactos = [
    emails, # 0
    telefonos # 1
]


print(emails[0]) # user1@gmail.com
print(contactos)
print(contactos[0][0]) # user1@gmail.com
print(contactos[0][1]) # user2@gmail.com
print(contactos[0][2]) # user3@gmail.com

print(contactos[0][0])
print(contactos[0][0])
print(contactos[0][0])
