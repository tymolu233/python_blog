from PIL import Image, ImageDraw, ImageFont
import string
import random
from io import BytesIO


def random_color():
    return random.randint(
        0, 255), random.randint(
        0, 255), random.randint(
            0, 255)


def random_code(width=200, height=40):
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', 32)
    str_all = string.ascii_letters + string.digits
    valid_code = ''
    for i in range(4):
        random_code = random.choice(str_all)
        draw.text((i * 40 + 20, 3), random_code, random_color(), font=font)
        valid_code += random_code
    for i in range(100):
        x, y = random.randint(0, width), random.randint(0, height)
        draw.point((x, y), fill=random_color())
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=random_color())
    for i in range(15):
        x1, y1 = random.randint(0, width), random.randint(0, height)
        x2, y2 = random.randint(0, width), random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=random_color())

    f = BytesIO()
    img.save(f, 'png')
    data = f.getvalue()
    print(valid_code)
    return data, valid_code
