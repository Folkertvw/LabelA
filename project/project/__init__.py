import psycopg2
import sys
import pprint
from pyramid.config import Configurator


class User:
    id = 0
    wishlist = []
    name = ""

    def __init__(self, id, wishlist, name):
        self.id = id
        self.wishlist = wishlist
        self.name = name

    def addToWishList(self, product):
        self.wishlist.append(product)

    def deleteFromWishList(self, id):
        self.wishlist.pop(id)


    def chooseDeliveryDay(self):
        print('\nOn which day would you like to take delivery of your products?')
        chosenDay = int(input('Monday = 1, Tuesday = 2, Wednesday = 3, Thursday = 4, Friday = 5, Saturday = 6, Sunday = 7'))
        if (chosenDay == 0 or chosenDay == 1 or chosenDay == 2 or chosenDay == 3 or chosenDay == 4 or chosenDay == 5 or chosenDay == 6 or chosenDay == 7):
            return chosenDay
        else:
            print('Whoops, that did not go as planned, please try again')
            return self.chooseDeliveryDay()

    def order(self):
        orderday = self.chooseDeliveryDay()
        print("\nUw bestelde producten:")
        for product in self.wishlist:
            print(product.name)
        print("Bestelling voltooid")


class Product:
    id = 0
    name = ""
    price = 0

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


def datacon():
    #Connectie string
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='mercedes'"

    #Connectie naar datbabase
    conn = psycopg2.connect(conn_string)

    #Cursort, gebruiken voor het uitvoeren van queries
    cursor = conn.cursor()

    # Voer query uit
    print("Gegevens uit PostgreSQL database:")
    cursor.execute("SELECT model.model_id, model.model, tyre_name, tyre_id FROM model JOIN car ON(model.model_id = car.model_id) JOIN tyre ON(car.car_id = tyre.car_id)")

    #Haal gegevens op uit de database
    records = cursor.fetchall()

    # Print gegevens
    pprint.pprint(records)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    datacon()

    #Instanties van producten
    product1 = Product(1, 'Mercedes e220', 49999)
    product2 = Product(2, 'V12 vantage', 399999)
    product3 = Product(3, 'Mitsubishi Carisma', 39999)
    product4 = Product(4, 'BMW 3serie', 35999)

    #Instaties van users/klanten
    user1 = User(1, [product1, product2], 'Bertje')
    user2 = User(2, [product3, product4], 'Frankie')

    #Product 3 wordt toegevoegd aan wishlist van user1, product 1 wordt toegevoegd aan whishlist van user2
    user1.addToWishList(product3)
    user2.addToWishList(product1)

    #Print huidige wishlist van user 1
    print('\nUser 1:')
    for car in user1.wishlist:
        print(car.name)

    #Print huidige wishlist van user 2
    print('\nUser 2:')
    for car in user2.wishlist:
        print(car.name)

    #Print huidige wishlist van user 1
    print('\nUser 1:')
    user1.deleteFromWishList(1)
    for car in user1.wishlist:
        print(car.name)

    #Print order van user 1
    user1.order()

    return config.make_wsgi_app()



