import csv
import os
from PIL import Image, ImageFilter


def a():

        a = ('png')
        os.mkdir('new')
        for pap in os.listdir():
            if pap.endswith(a):
                with Image.open(pap) as img:
                    img2 = img.filter(ImageFilter.CONTOUR)

                img2.save('new/' + str(pap))

a()

def b():
    ax = ('.jpg', '.png')
    os.mkdir('new2')
    for pap in os.listdir():
        if pap.endswith(ax):
            with Image.open(pap) as img:
                img2 = img.filter(ImageFilter.CONTOUR)

            img2.save('new/' + str(pap))

b()

def c():
    with open("data.csv", newline="") as file:
        read = csv.reader(file, delimiter=',')
        print("Нужно купить:")
        sum = 0
        for row in read:
            print(f"{row[0]} - {row[1]} шт. за {row[2]} руб.")
            sum += int(row[2]) * int(row[1])
    print(f"Итоговая сумма: {sum} руб.")

c()


