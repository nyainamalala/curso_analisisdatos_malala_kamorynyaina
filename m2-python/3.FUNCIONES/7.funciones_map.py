

names = ['persona1', 'persona2', 'persona3', 'persona4']

# for name  in names:
#    print(names)

print(f"ANTES: {names}-")

terminarEnPunto = lambda name : name + '.'
namesEdited = list(map(terminarEnPunto, names))
print(f"DESPUES:{namesEdited}")

names
print(f"DESPUES: ")


nombre_terminados_en_punto = list(map(nombre_terminar_en_punto, names))
print(f"DESPUES: {nombres_terminados_en_punto}")