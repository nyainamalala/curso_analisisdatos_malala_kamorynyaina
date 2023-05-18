import datetime
#Por defecto input lle string
# nombre = input("Introduzca su nombre\n") # <class 'str'>

# edad = int(input("Introduce edad\n")) # <class 'int'>

# salary = float(input("Introduce salario\n")) # <class>

# apto = bool(input("Es apto o no (0 o 1)\n"))

# fecha_nacimiento_str = input("Introduce fecha nacimiento")

# fecha_nacimiento_str = input("Introduce fecha nacimiento (YYYY-MM-dd) (1990-11-03) \n")
# fecha_nacimiento = datetime.date.fromisoformat(fecha_nacimiento_str)

fecha_nacimiento_str = input("Introduce fecha nacimiento (dd/MM/YYYY) (03/01/1990) \n")
fecha_array = fecha_nacimiento_str.split("/")
year = int(fecha_array[2])
month = int(fecha_array[1])
day = int(fecha_array[0])
fecha_final = datetime.date(year, month, day)


# fecha_final = datetime.date(fecha_array[2], fecha_array[1], fecha_array[0])
# fecha_final = datetima.date(fecha_array[-1], fecha_array[-2], fecha_array[-3])

print ("fin")