def a():

    k = input('Выберите число: ')
    k = int(k)
    l = [1, 2, 3, 4, 5, ]
    if k in l:
        print('Вы угадали число!')
    else:
        print("Такого числа нет!")

a()

def b():

    a = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
    b = int(input())
    print('Выходные:', a[:-b-1:-1])
    print('Рабочие дни:', a[:-b])

b()

def c():
a = [1,2,3,4,5,5,6,6,7]
print(*filter(lambda x : a.count(x) > 1, a))
c()