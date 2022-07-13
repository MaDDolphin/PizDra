import os
from math import ceil
import cv2
import numpy as np


def main():
    print(123)
    dst = "./photos/"  # Images destination
    images = os.listdir(dst)  # Get their names in a list
    length = len(images)

    result = np.zeros((400, 400, 3), np.uint8)  # Image window of size (360, 360)
    i = 1

    a = 1.0  # alpha
    b = 0.0  # beta
    img = cv2.imread(dst + images[i])
    img = cv2.resize(img, (400, 400))

    # Slide Show Loop
    while True:

        if ceil(a) == 0:
            a = 1.0
            b = 0.0
            i = (i + 1) % length  # Getting new image from directory
            img = cv2.imread(dst + images[i])
            img = cv2.resize(img, (400, 400))

        a -= 0.01
        b += 0.01

        # Image Transition from one to another
        result = cv2.addWeighted(result, a, img, b, 0)
        cv2.imshow("Slide Show", result)

        key = cv2.waitKey(1) & 0xff
        if key == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
