import cv2 as cv


def main():
    img = cv.imread('Photos/cats.jpg')
    cv.imshow('Cats', img)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    canny = cv.Canny(img, 125, 175)
    cv.imshow('Canny', canny)

    contours, hierarchies = cv.findContours(canny, cv.RETR_ LIST, cv.CHAIN APPROX_NONE)

    cv.waitKey(0)



if __name__ == '__main__':
    main()