import numpy as np
import cv2
import os
import glob
import time


def capture_image():
    cam = cv2.VideoCapture(0)
    s, frame = cam.read()
    print(s)
    if s:
        if not os.path.isdir('static'):  # checks to see if there is a static directory if there isn't it creates it
            os.mkdir('static')
        else:  # removes any png images that are in the static directory if the directory exists
            for filename in glob.glob(os.path.join('static', '*.png')):
                os.remove(filename)

        imgname = os.path.join('static', str(time.time()) + '.png')  # sets the imagename to a file based off the time.

        cv2.imwrite(imgname, frame)

    else:
        imgname = None

    return imgname
