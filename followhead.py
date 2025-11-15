import cv2 as cv
import numpy as np

"""
Face and hand detection
"""

cap = cv.VideoCapture(0)
haar_face = cv.CascadeClassifier('haar_face.xml')
widht = 0
height = 0
third = height // 3

directiony = 0

while True: 
    ret, img = cap.read()

    width = img.shape[1]
    height = img.shape[0]
    third = height // 3

    cv.line(img, (0, third), (img.shape[1], third), (255, 0, 0), thickness=2)
    cv.line(img, (0, 2*third), (img.shape[1], 2*third), (255, 0, 0), thickness=2)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_react = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces_react:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        detectedx = x
        detectedy = y
    
    if detectedy < third:
        directiony = 1
    elif detectedy > 2*third:
        directiony = -1
    else:
        directiony = 0

    print(directiony)

    cv.imshow('frame-1', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break

cap.release()
cv.destroyAllWindows()