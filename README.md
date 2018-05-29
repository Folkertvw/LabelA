# LabelA Assesment
Dit assesment is gemaakt in opdracht voor LabelA.
De gekozen programmeertaal is Python, in combinatie met het [pyramid framework](https://trypyramid.com/).
Dit project is opgezet in JetBrains PyCharm 2018, met behulp van een Pyramid project.
De datbase in PostgreSQL wordt in de applicatie niet gebruikt, maar is een indicatie van hoe ik deze zou opzetten.
Deze kan worden geimporteerd in PostgreSQL doormiddel van de restore optie en hier 'LabelA' bestand te selecteren, die te vinden is in de map 'database'.

### Installatie en setup
Om dit programma te runnen is python een vereiste, daarnaast dient de gebruiker een aantal packages te installeren:
* `pip install pyramid pyramid==1.9.2"`
* `pip install psycopg2`
* `pip install pyramid_jinja2`

Nadat de packages zijn geïnstalleerd kan het programma worden gerunt in bijvoorbeeld PyCharm, door `__init__.py` in de map 'project > project' uit te voeren.

### Functionaliteit
De klant (in deze toepassing een instantie van de class User, drie parameters: id, whishlist en name) kan producten aan zijn wishlist toevoegen doormiddel van de method: 'addToWishList'. Deze methode heeft één paramater: 'product'. De klant kan producten verwijderen met de methode 'deleteFromWishList', ook deze methode heeft één parameter, 'id'. Het verwijderen van een product gaat doormiddel van de id.
De methode 'chooseDeliveryDay' geeft de klant de mogelijkheid om een bezorgdag uit te kiezen, de dag wordt gekozen door middel van een getal, 1 = maandag, 2 = dinsdag etc. De methode 'order' geeft een overzicht van de bestele producten.
De class 'Product' heeft drie paramters: id, name en price. Doormiddel van instaties van de class product kunnen producten worden toegevoegd in de 'wishlist[]' van instanties van de class User.
Met behulp van de volgende for loop worden het winkelmandje van de klant getoond:
    `for car in user1.wishlist:
        print(car.name)`
        
Met `user1.deleteFromWishList(1)` wordt het tweede element in de array wishlist verwijderd. 
`user1.order()` toond de definitieve bestelling.