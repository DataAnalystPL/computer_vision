import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    _, frame = cap.read()

    cv.imshow('Camera', frame)

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('Laplacian', laplacian)

    edges = cv.Canny(frame, 150, 150)
    cv.imshow('Canny', edges)


    if cv.waitKey(5) == ord('x'):
        break

cap.release()
cv.destroyAllWindows()