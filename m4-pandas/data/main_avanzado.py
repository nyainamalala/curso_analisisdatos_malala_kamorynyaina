


city_from = input("Introduce la ciudad origen")
city_to = input("Introduce la ciudad origen")
passengers = read_int("passengers")
price = read_float("price")

travel = travel(None, ciy_from, city_to, passengers, price)

database.save(travel)
