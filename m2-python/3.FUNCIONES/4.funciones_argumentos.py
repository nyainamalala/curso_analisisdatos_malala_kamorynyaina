

name = 'Juan'

print(f"Hola name")
print(f"Hola soy {name} con eda {age}")
print("Hola soy " + ". con edad " + str(age))
print("Hola soy", name, "con edad", age)

def saludar(name, age):
    return f"Hola soy {name} con edad {age}"

saludo = saludar("Mike", 35)
print(saludo)
#En JavaScript: consolo.log('Hola ${name}')