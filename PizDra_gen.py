import cv2
import random


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
            print('1 -', text[:27])
            all_text.append(text[:27])
            split_text(text[27:], all_text)
        else:
            b = text[:27].rfind(' ')
            print('2 -', text[:b])
            all_text.append(text[:b+1])
            split_text(text[b+1:], all_text)
        text = text.splitlines()
    else:
        all_text.append(text)


def main():
    all_text = []
    text = """Доброе утро! Пусть оно начнется с радости и улыбки, с вдохновения и удачи, с больших амбиций и высоких стремлений. Желаю огромного заряда бодрости, энергии и позитива на весь день!"""
    split_text(text, all_text)
    cap = cv2.VideoCapture('video.avi')
    frame_array = []
    for i in all_text:
        print(i)
    for text in all_text:
        color = get_color()
        for i in range(len(text) + 1):
            # print((text[:i]))
            # Capture frames in the video
            ret, frame = cap.read()

            # describe the type of font
            # to be used.
            font = cv2.FONT_HERSHEY_COMPLEX

            # Use putText() method for
            # inserting text on video
            cv2.rectangle(frame, (10, 20), (480, 60), color[1], -1)
            cv2.putText(frame,
                        text[:i],
                        (10, 50),
                        font, 0.8,

                        color[0],
                        2,
                        cv2.LINE_4)

            # Display the resulting frame
            cv2.imshow('video', frame)
            cv2.waitKey(60)
            i = i + 1
            frame_array.append(frame)
            # creating 'q' as the quit
            # button for the video
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    out = cv2.VideoWriter('./test.avi', cv2.VideoWriter_fourcc(*'XVID'), 10, (480, 854))
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])

    # release the cap object
    cap.release()
    # close all windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
