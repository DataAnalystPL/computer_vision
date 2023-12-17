import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
subtractor = cv.createBackgroundSubtractorMOG2(20, 50)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, frame = cap.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

        if cv.waitKey(5) == ord('x'):
            break

cv.destroyAllWindows()
cap.release()