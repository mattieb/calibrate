import Image
import ImageDraw

image = Image.new('RGB', (640, 360))

draw = ImageDraw.Draw(image)

for y in range(9):

    y1 = y * 40
    y2 = y1 + 19
    y3 = y2 + 1
    y4 = y3 + 19

    for x in range(8):

        x1 = x * 80
        x2 = x1 + 39
        x3 = x2 + 1
        x4 = x3 + 39

        print x1, y1, x2, y2, 'blue'
        print x3, y1, x4, y2, 'white'
        print x1, y3, x2, y4, 'magenta'
        print x3, y3, x4, y4, 'cyan'

        draw.rectangle(((x1, y1), (x2, y2)), 'rgb(0%, 0%, 75%)')
        draw.rectangle(((x3, y1), (x4, y2)), 'rgb(75%, 75%, 75%)')
        draw.rectangle(((x1, y3), (x2, y4)), 'rgb(75%, 0%, 75%)')
        draw.rectangle(((x3, y3), (x4, y4)), 'rgb(0%, 75%, 75%)')

image.save('colortint.png', 'PNG')

# ex:et:sw=4:ts=4
