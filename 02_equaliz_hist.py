from PIL import Image, ImageDraw

def histograma(img):
    h = [0] * 256
    px = img.load()
    larg, alt = img.size
    for x in range(larg):
        for y in range(alt):
            h[px[x,y]] += 1

    return h

def plot(ls):
    plot = Image.new('L', (256,256), 200)
    draw = ImageDraw.Draw(plot)
    m = max(ls)
    for i in range(0,255):
        val = 255 - (ls[i] / m) * 255
        draw.line((i,255,i,val),0,1)
    return plot

def equalizar(img):
    h = img.histogram()

    for i in range(1,len(h)):
        h[i] = (h[i] + h[i-1])

    hmax = h[-1]
    for i in range(len(h)):
        h[i] = int(h[i] / hmax * 255)
    print(h)
    
    img = Image.eval(img, lambda L : h[L])

    return img


with Image.open("paisagem.png") as img:
    img = img.convert('L')

img1 = img.copy()
img1.paste(plot(img1.histogram()),
           (img1.width - 256,img1.height - 256))
img = equalizar(img)
img.paste(plot(img.histogram()),
           (img.width - 256,img.height - 256))

img2 = Image.new('L',(img.width *2, img.height))
img2.paste(img1)
img2.paste(img, (img.width,0))
img2.show()