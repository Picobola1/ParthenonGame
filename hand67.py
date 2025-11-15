"""
Six Seven
"""

import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)

while True:
    _, img = cap.read()
    if not ret:
        break

    cv.imshow("camera", img)