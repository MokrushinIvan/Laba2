def a():
    try:
        a = int(input("Введите число:"))
    except ValueError:
        print("Введено не число!")
    else:
        if a % 3 == 0:
            print(f"{a} делится на 3")
        elif a == 0:
            print("Введен 0!")
        else:
            print(f"{a} не делится на 3")
a()

def b():
    try:
        a = int(input("Введите число:"))
        b = 100 / a
    except ValueError:
        print("Введено не число!")
    except ZeroDivisionError:
        print("Введен 0!")
    else:
        print(f"100 : {a} = {b}")
b()

def c():
    a = input("Введите дату:")
    a = a.split(".")
    if int(a[0]) * int(a[1]) == int(a[2][2 : 4]):
        print("Дата магическая!")
    else:
        print("Дата не магическая")

c()

def z4():
    a = input("Введите номер:")
    x = 0
    y = 0
    if len(a) % 2 == 0:
        for i in a[0:int(len(a) / 2)]:
            x = x + int(i)
        for i in a[int(len(a) / 2):int(len(a)) + 1]:
            y = y + int(i)
        if x == y:
            print("Билет счастливый!")
        else:
            print("Билет не  счастливый!")
    else:
        print("Количество цифр нечётно!")