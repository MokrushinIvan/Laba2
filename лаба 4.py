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

def g():

    user1 = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Федоров']
    user2 = ['Морозов', 'Волков', 'Лебедев', 'Иванов', 'Егоров', 'Павлов', 'Козлов', 'Иванов', 'Николаев']
    print(user1)
    print(user2)
    user1.sort()
    user2.reverse()
    users1 = user1.copy()
    users2 = user2.copy()
    del user1[5:11:1]
    del users1[0:5:1]
    del user2[5:11:1]
    del users2[0:5:1]
    sport1 = user1 + users1
    sport2 = user2 + users2
    sport2.sort()
    sp1 = tuple(sport1)
    sp2 = tuple(sport2)
    p = 'Иванов'
    n = 0
    for i in sp2:
        if i == p:
            n = n + 1
    print('команда: ', sp2, 'кол-во участников: ', len(sp2), ' Количество участников с фамилией Иванов ', n)


g()