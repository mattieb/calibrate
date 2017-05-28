import Image
import ImageDraw

image = Image.new('RGB', (640, 360))

draw = ImageDraw.Draw(image)

draw.rectangle(((0, 0), (639, 359)), 'rgb(100%, 100%, 100%)')

colors = ('red', 'green', 'blue')

for n in range(21):
    x1 = 10 + n * 30
    x2 = x1 + 19 

    draw.rectangle(((x1, 0), (x2, 119)), colors[n % 3])
    draw.rectangle(((x1, 120), (x2, 239)), colors[(n + 1) % 3])
    draw.rectangle(((x1, 240), (x2, 359)), colors[(n + 2) % 3])

image.save('fringe.png', 'PNG')

# ex:et:sw=4:ts=4
