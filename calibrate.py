import Image
import ImageDraw

image = Image.new('RGB', (640, 480))

draw = ImageDraw.Draw(image)

draw.rectangle(((0, 240), (639, 479)), 'rgb(100%, 100%, 100%)')

for level in range(1, 11):
    left = (level - 1) * 62 + 19
    right = left + 43

    draw.rectangle(((left, 19), (right, 110)),
            fill='rgb(%d%%, %d%%, %d%%)' % (level, level, level))

    level += 10
    draw.rectangle(((left, 129), (right, 220)),
            fill='rgb(%d%%, %d%%, %d%%)' % (level, level, level))

    level += 69
    draw.rectangle(((left, 259), (right, 350)),
            fill='rgb(%d%%, %d%%, %d%%)' % (level, level, level))

    level += 10
    draw.rectangle(((left, 369), (right, 460)),
            fill='rgb(%d%%, %d%%, %d%%)' % (level, level, level))

image.save('calibrate.png', 'PNG')

# ex:et:sw=4:ts=4
