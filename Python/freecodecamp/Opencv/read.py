import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', img)  # show the image (title, path)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame) # display each frame of the video

    # 0xff คือ เลขฐาน 16
    # ord คือ การแปลง character(ตัวเดียว) ให้เป็น integer
    if cv.waitKey(20) & 0xFF == ord('d'): # stop displaying the video
        break

capture.release()
cv.destroyAllWindows()
