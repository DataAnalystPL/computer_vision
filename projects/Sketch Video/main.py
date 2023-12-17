import cv2 as cv

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    _, frame = cap.read()

    cv.imshow('Camera', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    invert_image = 255 - gray
    blurred = cv.GaussianBlur(invert_image,(21,21),0)
    inv_blurred = 255 - blurred

    sketch_video = cv.divide(gray, inv_blurred, scale=265.0)
    cv.imshow('sketch_video', sketch_video)


    if cv.waitKey(5) == ord('x'):
        break

cap.release()
cv.destroyAllWindows()