from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(size, text):
    img = Image.new('RGB', (600, 50), "yellow")
    draw = ImageDraw.Draw(img)
    draw.text((size[0], size[1]), text, font = fnt, fill="black")
    return img

frames = []

def roll(text):
    for i in range(len(text)+1):
        new_frame = create_image_with_text((0,0), text[:i])
        frames.append(new_frame)
# <<< ========== Customize font and text below ============== >>>>
fnt = ImageFont.truetype("arial", 36)
all_text = """ Pythonprogramming
Brought you this code
This text was made
with PIL and Python""".splitlines()
[roll(text) for text in all_text]
# <<< ======================================================== >>>
frames[0].save('banner1.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=80, loop=0)