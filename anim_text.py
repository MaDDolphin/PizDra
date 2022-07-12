from PIL import Image, ImageDraw, ImageFont

frames = []


def create_image_with_text(size, text, fnt):
    color = [
        ['#ccd5ae', '#fefae0'],
        ['#ffafcc', '#a2d2ff'],
        ['#bc6c25', '#bc6c25'],
        ['#264653', '#e9c46a'],
        ['#023047', '#219ebc'],
        ['#8338ec', '#3a86ff'],
        ['#fcbf49', '#f77f00'],
        ['#f1faee', '#a8dadc'],
        ['#f6bd60', 'f7ede2'],
        ['#ef233c', '#8d99ae'],
        ['#ffb4a2', '#ffcdb2'],
        ['#9b5de5', '#00bbf9'],
        ['#023e8a', '#0077b6'],
        ['#a3b18a', '#588157'],
        ['#d6ccc2', '#f5ebe0'],
        ['#bb3e03', '#ca6702']
    ]
    img = Image.new('RGB', (600, 50), '#ffbe0b')
    draw = ImageDraw.Draw(img)
    draw.fontmode = "1"
    draw.text((size[0], size[1]), text, font=fnt, fill="#fb5607")
    return img


def roll(text, fnt):
    for i in range(len(text) + 1):
        new_frame = create_image_with_text((0, 0), text[:i], fnt)
        frames.append(new_frame)


def main():
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
    [roll(text, fnt) for text in all_text]
    # <<< ======================================================== >>>
    frames[0].save('banner.gif', format='GIF',
                   append_images=frames[1:], save_all=True, duration=80, loop=0)


if __name__ == "__main__":
    main()