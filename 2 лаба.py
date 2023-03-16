def a():
    a = " "
    x = str(input('введите слово'))
    while x!= 'stop':
        a = a + x + ' '
        x = str(input('введите слово'))
    print(a)
a()

def b():
    x = str(input('введите слово'))
    if x.count("ф")>0:
            print('Редкое слово,вай!')
    else:
            print('это слово не редкое')

b()

def c():
    from random import randint

    x = 0
    while x<3:
        a = int(randint(0,20))
        b = int(randint(0, 20))
        print(a,'+',b, '=')
        otv=int(input('Введите ответ'))
        if a+b!=otv:
            x=x+1

        if x == 3:
            print('игра закончена')
c()





