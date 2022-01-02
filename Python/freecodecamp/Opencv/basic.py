import cv2 as cv
import numpy as np


def main():
    img = cv.imread('Photos/cat.jpg')
    cv.imshow('Cat', img)

    # Converting to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    # Blur
    blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)

    # Edge Cascade
    canny = cv.Canny(img, 125, 175)
    cv.imshow('Canny', canny)

    # Reduce edge's img
    canny = cv.Canny(blur, 125, 175)
    cv.imshow('Canny', canny)

    # Dilating the image
    dilated = cv.dilate(canny, (7,7), iterations=3)
    cv.imshow('Dilated', dilated)

    # Eroding
    eroded = cv.erode(dilated, (3,3), iterations=1)
    cv.imshow('Eroded', eroded)

    # Resize
    resize = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
    cv.imshow('Resize', resize)

    # Cropping
    cropped = img[50:200, 200:400]
    cv.imshow('Cropped img', cropped)

    cv.waitKey(0)





if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)  # can print all array
    main()
