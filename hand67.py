"""
How 67 will work?
1. Detect hands
2. Detect movement
3. 67
"""
import cv2 as cv
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
y1 = 0
y2 = 0
sixseven = False
sensibility = 15
cap = cv.VideoCapture(0)
prev_y = 0

while True:
    ret, img = cap.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)   
    results = mp_hands.Hands().process(img)

    wrist_ponts = []

    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, connections = mp_hands.HAND_CONNECTIONS)

            x = hand_landmarks.landmark[0].x
            y = hand_landmarks.landmark[0].y

            h, w, _ = img.shape
            px, py = int(x * w), int(y * h)
            wrist_ponts.append((px, py))
            cv.circle(img, (px, py), 6, (0,255,255), -1)

    if len(wrist_ponts) == 2:
        (x1, y1), (x2, y2) = wrist_ponts

        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

        if prev_y is not None:
            dy = y - prev_y

            if abs(dy) > sensibility:
                sixseven = True
            else:
                sixseven = False

        prev_y = y
        print(sixseven)
    
    cv.imshow('webcam', img)
cv.destroyAllWindows()