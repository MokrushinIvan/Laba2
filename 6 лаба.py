from PIL import Image

def a():
    filename = "karac.png"
    with Image.open(filename) as img:
        img.load()

    img.show()
    wid, hei = img.size

    forma = img.format

    mode = img.mode

    print("Ширина:", wid)
    print("Высота:", hei)
    print("Формат:", forma)
    print("Модель:", mode)

a()

def b():
    filename = "karac1.png"
    with Image.open(filename) as img:
        img.load()

    img = img.resize((img.width // 3, img.height // 3))
    img.show()
    img.save("C:\Users\user\PycharmProjects\karac23.png")
    img1 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img1.show()
    img.save("C:\Users\user\PycharmProjects\karac32.png")
b()

def r():
    for i in range(1, 6):
        img = Image.open(f"{i}.png")
        img = img.filter(ImageFilter.CONTOUR)
        pap_name = f"pap_{i}.png"
        img.save(f"pap/{pap_name}")
r()

def c():
    fon = Image.open("fon.jpg")
    mark = Image.open("karac.png")

    fon.paste(mark,(300,100))
    fon.save("raf.jpg", quality = 95)


c()

def d():
    fon = Image.open("fon.jpg")
    mark = Image.open("karac.png")

    width, height = fon.size
    widm, heim = mark.size
    if width < widm // 4 or widm > width // 4:
        widm = int(width // 4)
        heim = int(widm * heim / mark.width)
        mark = mark.resize((widm, heim))

    pos = (width - widm, height - height)
    fon.paste(mark, pos, mark)
    fon.save("raf.jpg")
d()