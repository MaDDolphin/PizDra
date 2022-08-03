import os
from os.path import isfile, join
import cv2


def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    # for sorting the file names properly
    files.sort(key=lambda x: int(x[5:-4]))
    for i in range(len(files)):
        filename = pathIn + files[i]
        # reading each files
        font = cv2.FONT_HERSHEY_COMPLEX
        img = cv2.imread(filename)
        cv2.putText(img,
                    'ass',
                    (10, 50),
                    font, 0.8,
                    (0,0,150),
                    2,
                    cv2.LINE_4)
        height, width, layers = img.shape
        size = (width, height)
        print(filename)
        # inserting the frames into an image array
        for i in range(0, 25):
            frame_array.append(img)
            i = i+1
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'XVID'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()


def main():
    pathIn = './scrap_data/bg/'
    pathOut = 'video.avi'
    fps = 25
    convert_frames_to_video(pathIn, pathOut, fps)


if __name__ == "__main__":
    main()
