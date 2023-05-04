def a():
    class rest:
        def __init__(self, rest_name, type ):
            self.rest_name = rest_name
            self.type = type

        def desc_rest(self):
            print(f"{self.rest_name} - {self.type} Японская кухня")

        def open_rest(self):
            print(f"{self.rest_name}, данный ресторан открыт!")

    newrest = rest("Какое-нибудь название", " тип кухни:")
    print(newrest.rest_name)
    print(newrest.type)

    newrest.desc_rest()
    newrest.open_rest()
a()

def b():
    class rest:
        def __init__(self, rest_name, type ):
            self.rest_name = rest_name
            self.type = type

        def desc_rest(self):
            print(f"{self.rest_name} - {self.type} Японская кухня")

        def open_rest(self):
            print(f"{self.rest_name}, данный ресторан открыт!")

    rest1 = rest('Какое-нибудь название','Японская кухня')
    rest2 = rest('Какое-нибудь название2','Немецкая кухня')
    rest3 = rest('Какое-нибудь название3','Русская кухня')

    rest1.desc_rest()
    rest2.desc_rest()
    rest3.desc_rest()



b()

def c():
    class rest:
        def __init__(self, rest_name, type, rating ):
            self.rest_name = rest_name
            self.type = type
            self.rating = rating

        def desc_rest(self):
            print(f"{self.rest_name} - {self.type} Японская кухня")
            print(f'Рейтинг ресторана: {self.rating}')

        def open_rest(self):
            print(f"{self.rest_name}, данный ресторан открыт!")

        def rating_set(self, new_rating):
            self.rating = new_rating

    newrest = rest("Какое-нибудь название", " тип кухни", 3.3)
    newrest.desc_rest()
    newrest.rating_set(4)
    newrest.desc_rest()

c()