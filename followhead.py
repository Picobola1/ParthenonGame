"""
Face Detection
"""
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Detects face and draws a rectangle
while True: 
    ret, img = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces_react:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    cv.imshow('frame-1', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()