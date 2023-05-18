import datetime

# modelos de datos
# MVC: Modelo Vista Controlador
# la clase e scomo un atabla de base de datos
# un objeto sería una fila de datos de unaa tabla
# modelo relacional
# modelo de objetos de Programación orientada a Objetos



# PARTE 1: lase usuario User: nif, birthday, email, phone, password


class User:

    # método constructor
    def __init__(self, id, nif, birthday, email, phone, address, password="admin"):
        self.id = id
        self.nif = nif
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.address = address # Asociación con un objeto de otra clase. One to One
        self.password = password


user1 = User('355674648y', datetime.date(1995, 1, 23), 'user1@gmail.com', '635356788')
user2 = User('678476289Z', datetime.date.fromisoformat("1995-01-03"), 'user2@gmail.com', '653627271')  # YYYY-MM-dd

print(user1.birthday)
print(user2.birthday)
print(f"{user1.id} {user1.nif} {user1.birthday} {user1.email} {user1.phone}")



# PARTE 2: Clase dirección Address: street, city, postal_code, country




class Address:
    def __init__(self, street, city, postal_code, country):
        self.street = street
        if (len(postal_code) == 5): # comprueba que la longitud del código postal es 5
            self.postal_code = postal_code
        else:
            self.postal_code = "28002"

        self.city = city
        self.postal_code = postal_code
        self.country = country


address1 = Address('Candilejas, 15', 'Madrid', '28018789', 'España')
address2 = Address('Rue Bemasoandro', 'Antananarivo', 'Tana-101', 'Madagascar')

print(address1.postal_code)
print(address2.country)





# PARTE 3: Asociación One to One entre User y Address

user3 = User(3, '534267865T', datetime.date(2000, 1, 1), 'user3@gmail.com', '343477890', address1)
print(user3.address.city)
print(user3.address.country)

# cambio de casa

user4 = User(4, '53486333D', datetime.date(2005, 1, 1), 'user4@gmail.com', '65432', address2)
print(user4.address.city)
print(user4.address.country)


corazon_maria = Address(9, 'calle corazón maría 67', '28002', 'Madrid', 'España')
