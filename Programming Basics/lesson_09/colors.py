# from PIL import Image
# im = Image.open('Colors.jpg')
# pixels = im.load()
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j ] = b, r, g
#
# im.show()
# #im.save('Colors2.jpg')

# from PIL import Image, ImageDraw
#
# im = Image.new("RGBA", (100, 200), (0, 255, 0, 128))
#
# draw = ImageDraw.Draw(im)
#
# draw.line((0, 0, 100, 200), fill=(255,0,0), width=1)
#
# im.show()

# from PIL import Image
# im = Image.open('Colors.jpg')
# pixels = im.load()
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         bw = (r + g + b)
#         pixels[i, j] = bw, bw, bw
#
#
# im.show()
#im.save('Colors2.jpg')
#
# from PIL import Image
# im = Image.open('Colors.jpg')
# pixels = im.load()
# x, y = im.size
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]
#         pixels[i, j] = 255 - r, 255 - g, 255 - b
#
#
# im.show()
# im.save('Colors2.jpg')

from PIL import Image, ImageFilter
im = Image.open('Colors.jpg')
pixels = im.load()
x, y = im.size

# converted_img = im.transpose(Image.FLIP_TOP_BOTTOM)
# converted_img.show()
#
# sharp_img = im.filter(ImageFilter.SHARPEN)
# im.crop((300, 300, 500, 500)).show()
# sharp_img.crop((300, 300, 500, 500)).show()

# smooth_img = im.filter(ImageFilter.SMOOTH)
# im.crop((300, 300, 500, 500)).show()
# smooth_img.crop((300, 300, 500, 500)).show()


