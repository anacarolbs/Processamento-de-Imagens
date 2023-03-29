from PIL import Image, ImageDraw

def id(L):
    return L

def inv(L):
    return 255 - L

def soma(L):
    return L + 100

def mult(L):
    return L * 2 - 100

def pot(L):
    return ((L / 255 ) ** 2) * 255

def plot(f):
    plot = Image.new('L', (256,256), 200)
    draw = ImageDraw.Draw(plot)
    for i in range(0,255):
        draw.line((i,255,i,255 - f(i)),0,1)
    plot.show()

with Image.open("doge.jpg") as img:
    img = img.convert('L')

plot(pot)
img = Image.eval(img, pot)
img.show()
