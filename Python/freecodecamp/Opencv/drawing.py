import cv2 as cv
import numpy as np


def main():
    # create array with 0 inside
    blank = np.zeros((500, 500, 3), dtype='uint8')  # (y axis, x-axis)

    # put the color green at x:200-300 y:300-400
    blank[200:300, 300:400] = 0, 255, 0

    # 2. Draw a Rectangle
    # (img, pos1, pos2, color, thickness)
    cv.rectangle(blank, (0, 0), (250, 250), (0, 0, 255), thickness=cv.FILLED)
    cv.imshow('Green', blank)

    # 3. Draw a circle
    # เอาแกน x และแกิน y มาจาก บรรทัด 10 แล้วหาร 2
    cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
    cv.imshow('Circle', blank)

    # 4. Draw a line
    # origin(0, 0) to center
    cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
    cv.imshow('Line', blank)

    # 5. Write text
    cv.putText(blank, 'Hello', (250, 250), cv.FONT_HERSHEY_TRIPLEX,1.0, (0, 255, 0), thickness=2)
    cv.imshow('Text', blank)


if __name__ == '__main__':
    main()
    cv.waitKey(0)
