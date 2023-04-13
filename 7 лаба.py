from PIL import Image, ImageDraw, ImageFont

def a():

    img = Image.open("dr.jpg")
    imgcrop = img.crop((0, 150, 170, 300))
    imgcrop.save("dr-crop.jpg", quality=95)
    imgcrop.show()

a()

def b():

    praz = {"День рождения" : " dr.jpg ", "Новый год" : "ng.jpg", "Пасха" : "pacxa.jpg", "23 февраля" : "23f.jpg", "8 марта" : "8m.jpg"}

    a = input("Введите название праздника:")
    if a in praz:
        img = Image.open(praz[a])
        img.show()
    else:
        print('ошибка')
b()

def c():

    a = input('Введите имя:')
    text = f"{a},Поздравляю!"

    img = Image.open("dr.jpg")

    fon = ImageFont.truetype('arial_bold.ttf', 30)
    draw = ImageDraw.Draw(img)
    draw.text((150,600), text, fill='red' ,font=fon,)
    img.save('podpis.jpg')
    img.show()



c()








