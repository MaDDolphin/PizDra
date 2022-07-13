from PIL import Image, ImageDraw, ImageFont

c = 0
inc = 10


def create_image_with_text(text):
    global c, inc
    img = Image.open("1.jpg")
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=fnt, fill='#ffffff')
    c += inc
    return img


# Create the frames
frames = []


def roll(text):
    global c
    for i in range(len(text) + 1):
        new_frame = create_image_with_text(text[:i])
        frames.append(new_frame)
    c = 0


fnt = ImageFont.truetype("impact", 35)
all_text = """ С добрым утром, улыбайся,
Пусть удачным будет день!
Каждым мигом наслаждайся,
Пусть уйдет печали тень!
Солнце пусть тебя согреет,
Кофеек пускай взбодрит,
Сердце пусть от счастья млеет,
А в душе лишь мир царит!""".splitlines()
[roll(text) for text in all_text]

# Save into a GIF file that loops forever
frames[0].save('banner_c.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=80, loop=0)
print("Done")
