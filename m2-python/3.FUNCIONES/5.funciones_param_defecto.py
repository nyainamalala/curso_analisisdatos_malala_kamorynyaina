

# es muy común que las librerias paquetes
def saludar1(nombre, edad):
    pass

def saludar2(nombre='Juan', edad=30):
    print(f" Hola soy {nombre} con edad {edad}")


    saludar1() # TypeError: saludar() missing 2 required positional arguments: 'nombre' and 'age'

saludar2()
saludar2("Antonio")
Saludar2("Albert", 40)