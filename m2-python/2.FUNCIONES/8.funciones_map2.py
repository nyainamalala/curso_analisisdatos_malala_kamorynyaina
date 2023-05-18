

prices = [10, 20, 30, 40, 50]

prices_iva = []

# Opción 1: bbucle for tradicional
for price in prices:
    price * 1.21
    prices_iva.append(price * 1.21)

print(prices_iva)

# opción 2: función map con función lambda
'''
prices = [10, 20, 30, 40, 50]
print(prices)

prices_iva = []

print(f"ANTES: {prices}")

terminar_en_punto = lambda price: price * 1.21

prices_terminados_en_punto = list(map(terminar_en_punto, prices))

print(f"DESPUES: {prices_terminados_en_punto}")
'''

# opción 2: función def

def sumarIva(price):
    return price * 1.21

print(f"El resultado es: {list(map(sumarIva, prices))}")

#opción 3: opción Lambda

sumarIva2= lambda price: price + 1.21
# lambda price: price * 1,21, prices

print(f"El resultado con Lambda es: {list(map(sumarIva2, prices))}")



# NO TIENE NADA QUE VER

