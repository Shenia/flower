from PIL import Image

im = Image.open("img/watering_can_pink.png")
pix = im.load()
original = [[0 for x in range(im.size[0])] for y in range(im.size[1])]
for x in range(im.size[0]):
    for y in range(im.size[1]):
        original[y][x] = pix[x, y]
        if pix[x, y] != (0, 0, 0, 0):
            pix[x, y] = (max(pix[x, y][0]-50, 0), max(pix[x, y][1]-50, 0), min(pix[x, y][2] + 100, 255), pix[x, y][3])
im.save('img/watering_can_purple.png')

im = Image.open("img/watering_pink.png")
pix = im.load()
original = [[0 for x in range(im.size[0])] for y in range(im.size[1])]

pink = False
red_adjust = 0
green_adjust = 0
blue_adjust = 0

for x in range(im.size[0]):
    for y in range(im.size[1]):
        original[y][x] = pix[x, y]
        if pink:
            red = pix[x, y][0] + red_adjust
            green = pix[x, y][1] + green_adjust
            blue = pix[x, y][2] + blue_adjust
            pix[x, y] = (max(red, 0), max(green, 0), max(blue, 0), pix[x, y][3])
im.save('img/watering_purple.png')
