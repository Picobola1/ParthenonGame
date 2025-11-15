import cv2 as cv
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


cap = cv.VideoCapture(0)

while True:
    ret, img = cap.read()
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)   
    results = mp_hands.Hands().process(img)

    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, connections = mp_hands.HAND_CONNECTIONS)

    cv.imshow('webcam', img)    

cv.destroyAllWindows()