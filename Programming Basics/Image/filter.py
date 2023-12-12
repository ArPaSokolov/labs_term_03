from PIL import Image, ImageFilter

im1 = Image.open('Colors.jpg')
im2 = Image.new("RGB", im1.size)
pixels1 = im1.load()
pixels2 = im2.load()

for i in range(10, im1.width):
    for j in range(im1.height):
        r = pixels1[i - 20, j][0]
        g = pixels1[i, j][1]
        b = pixels1[i, j][2]
        # Применяем фильтр
        pixels2[i, j] = r, 0, b

im2.filter(ImageFilter.BLUR).show()