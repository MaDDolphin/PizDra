from PIL import Image, ImageDraw, ImageFont


def create_image_with_text(size, text):
    img = Image.new('RGB', (600, 50), '#3E8989')
    draw = ImageDraw.Draw(img)
    draw.fontmode = "1"
    draw.text((size[0], size[1]), text, font=fnt, fill="#2CDA9D")
    return img


frames = []


def roll(text):
    for i in range(len(text) + 1):
        new_frame = create_image_with_text((0, 0), text[:i])
        frames.append(new_frame)

text = """ С добрым утром, улыбайся,
Пусть удачным будет день!
Каждым мигом наслаждайся,
Пусть уйдет печали тень!

Солнце пусть тебя согреет,
Кофеек пускай взбодрит,
Сердце пусть от счастья млеет,
А в душе лишь мир царит!
"""
# <<< ========== Customize font and text below ============== >>>>
fnt = ImageFont.truetype("impact", 36)
all_text = text.splitlines()
[roll(text) for text in all_text]
# <<< ======================================================== >>>
frames[0].save('banner.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=80, loop=0)
