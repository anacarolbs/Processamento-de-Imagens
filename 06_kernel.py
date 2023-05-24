from PIL import Image


def kernel(img, kern):
    orig = img.load()
    saida = img.copy()
    dest = saida.load()

    for x in range(1,img.width-1):
        for y in range(1, img.height-1):
            v = [orig[x-1,y-1], orig[x,y-1], orig[x+1,y-1],
                 orig[x-1,y], orig[x,y], orig[x+1,y],
                 orig[x-1,y+1], orig[x,y+1], orig[x+1,y+1]]
            r = 0
            for i in range(len(v)):
                r = int(r + (v[i] * kern[i]))
            dest[x,y] = r
    
    return saida

def minimo(img):
    orig = img.load()
    saida = img.copy()
    dest = saida.load()

    for x in range(1,img.width-1):
        for y in range(1, img.height-1):
            v = [orig[x-1,y-1], orig[x,y-1], orig[x+1,y-1],
                 orig[x-1,y], orig[x,y], orig[x+1,y],
                 orig[x-1,y+1], orig[x,y+1], orig[x+1,y+1]]

            dest[x,y] = min(v)
    
    return saida
            

with Image.open('zap.png') as img:
    img = img.convert('L')

k = [ 0, 1, 0,
      1, -4, 1,
      0, 1, 0]

k1 = [-1, -1, -1,
      -1, 9, -1,
      -1, -1, -1]
img.show()
minimo(img).show()
kernel(img,k).show()
kernel(img,k1).show()

