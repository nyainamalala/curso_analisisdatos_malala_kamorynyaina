

class Book:
    def __init__(self, title, num_pages):
        self.title = title
        self.num_pages = num_pages

    def __str__(self):
        return f"title={self.title}, num_pages={self.num_pages}"
    
book1 = Book('book1', 340)
print(book1)


# Otro ejemplo de str

class Author:
    def __init__(self, id, nif, email, year, city, num_book=0):
        self.id = id
        self.nif = nif
        self.email = email
        self.year = year
        self.city = city
        self.num_book = num_book
    
    def __str__(self):
        # Opción 1
        # return f"Author con id = {self.id} " \
        #   f"nif = {self.nif} " \
        #   f"email = {self.email} " \
        #   f"year = {self.year} " \
        #   f"city = {self.city} " \
        #   f"num_book = {self.num_book} " 


        # Opción 2
        return 'Hola %s %s %s' % (self.id, self.nif, self.email)
    

            
author1 = Author(1, '2322323R', 'author1@gmail.com', 2000, 'Madrid')
print(author1)