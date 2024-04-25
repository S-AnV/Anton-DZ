import cv2
import numpy as np

cap = cv2.VideoCapture('mk.mp4')

while True:
    success, img = cap.read()
    cut_eye = np.zeros(img.shape, dtype='uint8')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces_n = cv2.CascadeClassifier('faces.xml')
    eyes_n = cv2.CascadeClassifier('eye.xml')

    faces = faces_n.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)

    for (x, y, w, h) in faces:
        eyes = eyes_n.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=4)
        if len(eyes) >= 2:
            ex1, ey1, ew1, eh1 = eyes[0]
            ex2, ey2, ew2, eh2 = eyes[1]
            if faces[0][0] < ex1:
                eye = cv2.rectangle(img, (x, ey1), (x + w, ey1 + eh2), (100, 100, 100), thickness=3)
                cut_eye = eye[ey1:ey1 + eh2, x:x + w]
                cut_eye = cv2.GaussianBlur(cut_eye, (49, 49), 0)
                cut_eye = cv2.cvtColor(cut_eye, cv2.COLOR_BGR2GRAY)
                cut_eye = cv2.cvtColor(cut_eye, cv2.COLOR_GRAY2BGR)
                img[ey1:ey1 + eh2, x:x + w] = cut_eye

    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



