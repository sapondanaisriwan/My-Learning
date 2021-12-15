import cv2 as cv

img = cv.imread("Photos/cat_large.jpg")
cv.imshow('Title', img)

def rescaleFrame(frame, scale=0.75): # Images, Video and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimentions = (width, height)

    # syntax resize cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    # read more https://pythonexamples.org/python-opencv-cv2-resize-image/
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

def changeRes(width, height): # Live video
    capture.set(3, width)
    capture.set(4, height)

# cv.imshow('Image', rescaleFrame(img))
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame) # display each frame of the video
    cv.imshow('Video Rezied', frame_resized) # display each frame of the video

    # 0xff คือ เลขฐาน 16
    # ord คือ การแปลง character(ตัวเดียว) ให้เป็น integer
    if cv.waitKey(20) & 0xFF == ord('q'): # stop displaying the video
        break

capture.release()
cv.destroyAllWindows()