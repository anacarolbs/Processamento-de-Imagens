from PIL import Image, ImageFilter

with Image.open("cores.jpg") as img:
    img = img.convert('YCbCr')
    Y, Cb, Cr = img.split()

    Cb = Cb.filter(ImageFilter.BoxBlur(5))
    Cr = Cr.filter(ImageFilter.BoxBlur(5))

new = Image.merge('YCbCr', (Y, Cb, Cr))
new.show()