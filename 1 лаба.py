def a():
    parol = input('Введите пароль: ')

    is_numeric = False
    is_lower = False
    is_upper = False
    is_spc = False

    for char in parol:
        if char.isnumeric():
            is_numeric = True
        elif char.islower():
            is_lower = True
        elif char.isupper():
            is_upper = True
        elif char in "%#$@":
            in_spc = True

    if len(parol) > 4 and is_numeric and is_upper and is_spc and is_lower:
        print('Замечательный пароль!')
    else:
        print('Пароль не подходит!')
a()

def b():
    god = int(input('Введите год: '))

    if god % 400 == 0:
        print('Високосный')
    elif god % 100 == 0:
        print('Не високосный')
    elif god % 4 == 0:
        print('Високосный')
    else:
        print('Не високосный')
b()

def c():
    mv = int(input('Введите ваше место'))

    if mv % 2 == 0 and mv <= 36:
        print('Ваше место верхнее в основном отделе')
    elif mv % 2 != 0 and mv <= 35:
        print('Ваше место нижнее в основном отделе')
    elif mv % 2 == 0 and mv > 36:
        print('Ваше место верхнее сбоку')
    else:
        print('Ваше место нижнее сбоку')
c()

def g():
    a, b = input('Введите первый цвет'), input('Введите второй цвет')

    if a != 'красный' and a != 'синий' and a != 'желтый':
        print('Ошибка в цвете')
    elif b != 'красный' and b != 'синий' and b != 'желтый':
        print('Ошибка в цвете')
    elif a == 'красный' and b == 'синий':
        print('Получился феолетовый')
    elif b == 'красный' and a == 'синий':
        print('Получился феолетовый')
    elif a == 'красный' and b == 'желтый':
        print('Получился оранжевый')
    elif b == 'красный' and a == 'желтый':
        print('Получился оранжевый')
    elif a == 'синий' and b == 'желтый':
        print('Получился зеленый')
    elif b == 'синий' and a == 'желтый':
        print('Получился зеленый')
    elif a == 'синий' and b == 'синий':
        print('Получиться синий')
    elif a == 'красный' and b == 'крвсный':
        print('Получиться красный')
    elif a == 'желтый' and b == 'желтый':
        print('Получиться желтый')
g()

def f():
    print(' '.join([input('Ведите слово') for i in range(int(input('Введите количество слов ')))]))
f()