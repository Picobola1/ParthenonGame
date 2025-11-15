import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)

while True:
    _, img = cap.read()

    cv.imshow('webcam', img)