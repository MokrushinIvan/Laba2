import json

def a():
    with open('rt.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)

    for prod in data['products']:
        if prod['available']:
            avi = 'В наличии'
        else:
            avi = 'Нет в наличии!'
        print(f"Название: {prod['name']}")
        print(f"Цена: {prod['price']}")
        print(f"Вес: {prod['weight']}")
        print(avi)
a()

def b():
    n_prod = {}
    n_prod["name"] = input("название продукта: ")
    n_prod["price"] = input("цена продукта: ")
    n_prod["weight"] = input("вес продукта: ")
    avi = input("Есть ли он да или нет: ")
    if avi == "да":
        n_prod["available"] = True
    else:
        n_prod["available"] = False

        with open('rt2.json', mode='r', encoding='utf-8') as file:
            data2 = json.load(file)
        data2["products"].append(n_prod)
        file.close()

        with open('products.json', mode='w', encoding='utf-8') as file:
            json.dump(data2, file)
            file.close()

            with open('rt.json', mode='r', encoding='utf-8') as file:
                data2 = json.load(file)
            for prod in data2['products']:
                if prod['available']:
                    avi = 'В наличии'
                else:
                    avi = 'Нет в наличии!'
                print(f"Название: {prod['name']}")
                print(f"Цена: {prod['price']}")
                print(f"Вес: {prod['weight']}")
                print(avi)

b()

def c():
    with open('en-ru.txt', mode='r', encoding='utf-8') as file:
        dict = {}
        for line in file:
            line = line.replace('\n', ' ')
            listnew = line.split('-')
            with open('en-ru.txt', mode='a', encoding='utf-8') as file:
                dict[listnew[0]] = listnew[0]
                listkey = list(dict.keys())
                listkey.sort()
        for j in listkey:
            pr = (j, '-', dict[j])
            prk = (' '.join(pr))
            print(prk)
            with open('ru-en.txt', mode='a', encoding='utf-8') as file:
                file.write(prk + '\n')

c()