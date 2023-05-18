
class Traveldatabase:
    def __init__(self):
        self.travels = []

    def find_all(self): # SELECT * FROM travels
        return self.travels.copy()
        # return list(self.travels)


'''
 # SELECT * FROM travels WHERE id = x
    def find_by_id(self, id):
        id = [1, 2, 3, 4, 5]
        for Id in id:
            if id == 6:
                return
            print('Hola my id is' + id)

        # iterar sobre los viajes
        # encontrar el viaje por id
        #devolver el viaje encontrado
        '''


 # SELECT * FROM travels
 # WHERE city_from = "" AND city_to = ""
    '''def find_all_by_city(self, city_from, city_to):
        city_from = ['Madrid', 'Paris', 'London', 'Tamatave', 'Diego']
        for travel in city_from:
            if city_from == 'Tamatave':
                return
            
        city_to = ['Tana', 'Brest', 'Italia', 'Tulear', 'Sevilla']
        for travel in city_to:
            if city_to == 'Brest':
                continue
        
            print('Hola, su destinación es ' + city_from)
            print('Hola, su viaje de vuelta es ' + city_to)'''

#  in self    for travel.travels


# class Traveldatabase:
    def __init__(self):
        self.travels = []

    def find_all(self): # SELECT * FROM travels
        for travel in self.travels
        return self.travels.copy()
    
        # return list(self.travels

# SELECT * FROM travels WHERE id = id_travel
    def find_by_id(self, id_travel):
        # iterar sobre los viajes
        for travel in self.travels:
            if travel.id == id_travel:
                return travel1
            
        return None
    
# SELECT * FROM travels
# WHERE city_from = "" And city_to =""
    def find_all_by_city(self, city_from, city_to):
        filtered_travels = [] # cuando creas [] crees una lista

        for travel in self.travels: 
            if travel.city_from == city_from and travel.city_to == city_to:
                filtered_travels.append(travel)
        return filtered_travels
    
    def save(self, travel):
        # buscar en travels cuál es el id más alto
        id_maximo = 0
        for current_travel in sel.travels:
            if current_travel.id > id_maximo:
                id_maximo = current_travel.id

        # generar el nuevo id sumando 1 al id más alto
        travel.id = id_maximo + 1

        # guardar en la lista
        self.travels.append(travel)