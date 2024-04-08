import numpy as np
import cv2
import os

front_cascade = cv2.CascadeClassifier('cascades/cascade_front.xml')
side_cascade = cv2.CascadeClassifier('cascades/cascade_side.xml')
back_cascade = cv2.CascadeClassifier('cascades/cascade_back.xml')

cap = cv2.VideoCapture(0)

face_count = 0

while True:
    ret, img = cap.read()
    if ret == True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face_front = front_cascade.detectMultiScale(gray, 1.3, 5)
        face_side = side_cascade.detectMultiScale(gray, 1.3, 5)
        face_back = back_cascade.detectMultiScale(gray, 1.3, 5)

        skip = False

        if len(face_front) > 0:
            for (x, y, w, h) in face_front:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                skip = True

        if len(face_side) > 0 and not skip:
            for (x, y, w, h) in face_side:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]
                skip = True

        if len(face_back) > 0 and not skip:
            for (x, y, w, h) in face_back:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]

        face_count = len(face_front) + len(face_side) + len(face_back)
        cv2.putText(img, f'Faces: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
