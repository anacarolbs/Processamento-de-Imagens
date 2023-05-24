from PIL import Image

with Image.open("nuvem.jpg") as img:
    R, G , B = img.split()

K = Image.new('L',img.size, 0)

new = Image.merge('RGB', (B, G, R))
new.show()