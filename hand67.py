"""
How 67 will work?
1. Detect hands
2. Detect movement
3. 67
"""
import os
import sys
#This line is for deleting anoying messages :D
class DummyFile(object):
    def write(self, x): pass
    def flush(self): pass

stderr_original = sys.stderr
sys.stderr = DummyFile()

import cv2 as cv
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

sixseven = False
sensibility = 40
cap = cv.VideoCapture(0)
prev_y1, prev_y2 = None, None

def palm_up(hand):
    wrist = hand.landmark[0]
    middle_mcp = hand.landmark[9]
    return middle_mcp.y < wrist.y

while True:
    ret, img = cap.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)   
    results = mp_hands.Hands().process(img)

    wrist_ponts = []
    palms_up_list = []

    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, connections = mp_hands.HAND_CONNECTIONS)

            x = hand_landmarks.landmark[0].x
            y = hand_landmarks.landmark[0].y

            h, w, _ = img.shape
            px, py = int(x * w), int(y * h)
            wrist_ponts.append((px, py))
            palms_up_list.append(palm_up(hand_landmarks))

            cv.circle(img, (px, py), 6, (0,255,255), -1)

    if len(wrist_ponts) == 2:
        (x1, y1), (x2, y2) = wrist_ponts

        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

        if prev_y1 is not None and prev_y2 is not None:
            dy1 = y1 - prev_y1
            dy2 = y2 - prev_y2

            if abs(dy1) > sensibility or abs(dy2) > sensibility:
                sixseven = True

        prev_y1, prev_y2 = y1, y2
        print(f'sixseven= {sixseven}')
        sixseven = False
    
    cv.imshow('webcam', img)
cv.destroyAllWindows()