'''
Ejemplo de bucle for con palabra reservada continue que salta a la siguiente iteración
'''

names = ['Patricia', 'Juan', 'Jholman', 'Edu', 'Latifa', 'Alan', 'Rafa']

for name in names:

    if name == 'Alan':
        continue
    
    print('Hola ' + name)


