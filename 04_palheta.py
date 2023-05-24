from PIL import Image, ImageDraw

w, h = 256, 256
img = Image.new('HSV',(w,h),(0,0,0))
draw = ImageDraw.Draw(img)
num = 10
for i in range(num):
    for j in range(num):
        x = i*(w/num)
        y = j*(h/num)
        ic = int(i*255/num)
        jc = int(j*255/num)
        draw.rectangle((x,y,x+(w/num),y+(h/num)), (ic,255,255-jc))
img.show()