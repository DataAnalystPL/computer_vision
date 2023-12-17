import cv2 as cv
import pathlib

cascade_path = pathlib.Path(cv.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

clf = cv.CascadeClassifier(str(cascade_path))


cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    _, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=7,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)

    cv.imshow("Faces", frame)

    if cv.waitKey(5) == ord('x'):
        break

cap.release()
cv.destroyAllWindows()
   