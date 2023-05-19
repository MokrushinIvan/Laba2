from tkinter import *

def a():
    class icecream:
        def __init__(self, ice_name, type, flavors):
            self.ice_name = ice_name
            self.type = type
            self.flavors = flavors

        def disp_flavors(self):
            print("Есть вот такие сорта мороженого:")
            for flavor in self.flavors:
                print(f"мороженое {flavor}")

    icecreamstand = icecream("Славица", "Мороженое",
                                           ["шоколадное", "ванильное", "клубничное"])
    icecreamstand.disp_flavors()

a()

def b():
    flavors = ["шоколадное", "ванильное", "клубничное", "мятное"]
    dictionary = {"Мягкое": flavors, "Стаканчик": flavors, "На палочке": flavors}

    class icecream:
        def __init__(self, ice_name, type, flavors, location, time):
            self.ice_name = ice_name
            self.type = type
            self.flavors = flavors
            self.location = location
            self.time = time


        def disp_flavors(self):
            print("Есть вот такие сорта мороженого:")
            for flavor in self.flavors:
                print(f"мороженое {flavor}")

        def disp_location(self):
            print (f'{self.ice_name} - {self.location}:  находиться на сенной площади')

        def disp_time(self):
            print (f'{self.ice_name} - {self.time}: работает с 10:00 до 22:00')

        def add_flavor(self,):
            (kol) = input("сколько вкусов хотите добавить? ")
            while int(kol) > 0:
                n = input("введите мороженое: ")
                flavors.append(n)
                kol = int(kol) - 1


        def del_flover(self,):
            kol = input("сколько вкусов хотите убрать? ")
            while int(kol) > 0:
                flavors.remove(input("введите мороженое:"))


        def check_flavor(self):
            w = (input("Введите мороженное для проверки:") in flavors)
            if w == True:
                print("В наличии")
            else:
                print("нету")

        def stick(self):
            print("У нас есть мороженое на палочке")
            r = input("Хотите ли мороженное на палочке?")
            if r == 'да':
                print('отличный выбор')
            else:
                print('-')
        def soft(self):
            print("У нас есть мягкое мороженое")
            r = input("Хотите ли мягкое мороженное ?")
            if r == 'да':
                print('отличный выбор')
            else:
                print('-')
        def cup(self):
            print("У нас мороженое в стаканчике")
            r = input("Хотите ли мороженное в стаканчике?")
            if r == 'да':
                print('отличный выбор')
            else:
                print('-')
    icecreamstand = icecream("Славица", "Мороженое",
                         ["шоколадное", "ванильное", "клубничное", "мятное"], 'Расположение', 'Время')
    icecreamstand.disp_flavors()
    icecreamstand.disp_location()
    icecreamstand.disp_time()
    icecreamstand.add_flavor()
    icecreamstand.del_flover()
    icecreamstand.check_flavor()
    icecreamstand.cup()
    icecreamstand.soft()
    icecreamstand.stick()

b()

def c():
    class icecream:
        def __init__(self, ice_name, type, flavors):
            self.ice_name = ice_name
            self.type = type
            self.flavors = flavors

        def disp_flavors(self):
            print("Есть вот такие сорта мороженого:")
            for flavor in self.flavors:
                print(f"мороженое {flavor}")

        def frame(self):
            root = Tk()
            root.geometry("200x200")
            root.resizable(False, False)
            root.title("Мороженое")
            title = Label(font=30)
            for f in self.flavors:
                item = Label(text = f, font=30)
                item.pack()
            title.pack()
            root.mainloop()

    icecreamstand = icecream("Славица", "Мороженое",
                             ["шоколадное", "ванильное", "клубничное", "Мятное"])
    icecreamstand.disp_flavors()
    icecreamstand.frame()

c()
