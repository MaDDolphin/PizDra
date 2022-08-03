import os
from os.path import isfile, join
import cv2
import shutil
import time
import random


def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: int(x[5:-4]))

    for i in range(len(files)):
        filename = pathIn + files[i]
        # reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        # inserting the frames into an image array

        for i in range(0, 25):
            frame_array.append(img)
            i = i + 1

    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'XVID'), fps, size)

    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])

    out.release()


def bg_photo_name_gen(tmp_path):
    os.mkdir(tmp_path)
    for i in range(0, 20):  # 6280+1
        shutil.copyfile('./scrap_data/bg/' + str(random.randint(0, 6280)) + '.jpg',
                        tmp_path + '/frame' + str(i) + '.jpg')


def bg_gen(date):
    pathIn = './temp/' + date + '/'
    bg_photo_name_gen(pathIn)
    pathOut = './temp/' + date + '.avi'
    fps = 25
    convert_frames_to_video(pathIn, pathOut, fps)


def get_color():
    colors = [
        ['#ccd5ae', '#fefae0'],
        ['#ffafcc', '#a2d2ff'],
        ['#bc6c25', '#bc6c25'],
        ['#264653', '#e9c46a'],
        ['#023047', '#219ebc'],
        ['#8338ec', '#3a86ff'],
        ['#fcbf49', '#f77f00'],
        ['#f1faee', '#a8dadc'],
        ['#f6bd60', '#f7ede2'],
        ['#ef233c', '#8d99ae'],
        ['#ffb4a2', '#ffcdb2'],
        ['#9b5de5', '#00bbf9'],
        ['#023e8a', '#0077b6'],
        ['#a3b18a', '#588157'],
        ['#d6ccc2', '#f5ebe0'],
        ['#bb3e03', '#ca6702']
    ]
    cn = random.randint(0, len(colors) - 1)
    color = []

    c1 = colors[cn][0].lstrip('#')
    color.append(tuple(int(c1[i:i + 2], 16) for i in (0, 2, 4)))

    c2 = colors[cn][1].lstrip('#')
    color.append(tuple(int(c2[i:i + 2], 16) for i in (0, 2, 4)))

    return color


def split_text(text, all_text):
    if len(text) > 28:
        a = text.find(' ')
        if a > 27 or a < 1:
            all_text.append(text[:27])
            split_text(text[27:], all_text)
        else:
            b = text[:27].rfind(' ')
            all_text.append(text[:b + 1])
            split_text(text[b + 1:], all_text)
        text = text.splitlines()
    else:
        all_text.append(text)


def main():
    date = str(round(time.time() * 1000))  # уникальный ключ видео
    bg_gen(date)

    all_text = []
    text = """Доброе утро! Пусть оно начнется с радости и улыбки, с вдохновения и удачи, с больших амбиций и высоких стремлений. Желаю огромного заряда бодрости, энергии и позитива на весь день!"""
    split_text(text, all_text)
    cap = cv2.VideoCapture('./temp/' + date + '.avi')

    frame_array = []

    for text in all_text:
        color = get_color()
        for i in range(len(text) + 1):
            # Capture frames in the video
            ret, frame = cap.read()

            font = cv2.FONT_HERSHEY_COMPLEX

            cv2.rectangle(frame, (10, 20), (480, 60), color[1], -1)
            cv2.putText(frame, text[:i], (10, 50), font, 0.8, color[0], 2, cv2.LINE_4)
            cv2.waitKey(60)
            i = i + 1
            frame_array.append(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    out = cv2.VideoWriter('./temp/no_sound'+date+'.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (480, 854))

    for i in range(len(frame_array)):
        out.write(frame_array[i])

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
