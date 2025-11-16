import os
os.environ["GLOG_minloglevel"] = "3"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from absl import logging
logging.set_verbosity(logging.ERROR)
os.environ['SDL_VIDEO_WINDOW_POS'] = "100,300"   # (x , y)
import pygame
import threading
import random
import cv2 as cv
import time as time


import mediapipe as mp
import numpy as np
import sys
from playsound3 import playsound

pygame.init()
#class DummyFile(object):
    #def write(self, x): pass
    #def flush(self): pass

#stderr_original = sys.stderr
#sys.stderr = DummyFile()
Width = 500
Height = 300
last_time = 0
clock = pygame.time.Clock()
spawnTime = 0
## head
cap = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
detectedx = 0
detectedy = 0
widht = 0
height = 0
third = height // 3
screen = pygame.display.set_mode((Width, Height))
#67
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
sixseven = False
sensibility = 40
prev_y1, prev_y2 = None, None
# function from 67
def palm_up(hand):
    wrist = hand.landmark[0]
    middle_mcp = hand.landmark[9]
    return middle_mcp.y < wrist.y


directiony = 0

screen = pygame.display.set_mode((Width,Height))
direction = 0
charachter = pygame.image.load("BlueDino1.png").convert_alpha()
catus = pygame.image.load("Cactus.png").convert_alpha()
heart = pygame.image.load("Heart.png").convert_alpha()
Image67 = pygame.image.load("67.jpg").convert_alpha()
scaled_charachter = pygame.transform.scale(charachter,(60,60))
scaled_heart = pygame.transform.scale(heart,(40,40))

Midpoint = Height/2
MidpointDino = Height/2
Hand67 = False


running = True
pygame.display.Info()

catus_x = Width
catusList = [(400,Midpoint),(600,Midpoint),(800,Midpoint)]

start_x = 50
start_y = 50
speed = 100
lives = 5

meme_img_original = cv.imread('67.jpg')         # OpenCV version of the meme
meme_window_name = "6-7"
meme_start_time = None  
meme_img = cv.resize(meme_img_original, (200, 200)) 

hands = mp_hands.Hands(
    max_num_hands=2,
    model_complexity=0,             # FASTER
    min_detection_confidence=0.6,   
    min_tracking_confidence=0.6     
)
DinoMove = True
while True: 
    deltaTime = clock.tick(60) / 1000
    if sixseven == False:
        screen.fill((186, 149, 97))
    ret, img = cap.read()
    #67
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)   
    results = hands.process(img)
    width = img.shape[1]
    height = img.shape[0]
    third = height // 3

    cv.line(img, (0, third), (img.shape[1], third), (255, 0, 0), thickness=2)
    cv.line(img, (0, 2*third), (img.shape[1], 2*third), (255, 0, 0), thickness=2)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    #67 array's
    wrist_ponts = []
    palms_up_list = []

    for (x, y, w, h) in faces_react:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
        detectedx = x
        detectedy = y
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
        #print(f'sixseven= {sixseven}')
        #sixseven = False
    if detectedy < third:
        directiony = 1
    elif detectedy > 2*third:
        directiony = -1
    else:
        directiony = 0

    #print(directiony)
    #screen.fill((48, 105, 152))
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,MidpointDino))
   
    
    dinoHitBox = pygame.Rect(start_x, MidpointDino, scaled_charachter.get_width(), scaled_charachter.get_height())
    for i in range(lives):
        screen.blit(scaled_heart, (100 + i * 40,10))
    if lives == 0:
        pygame.quit()

    for i in range(len(catusList)):
        catusList[i] = (catusList[i][0] - speed * deltaTime, catusList[i][1])   
    
    for x,y in catusList:
        catusHitBox = pygame.Rect(x,y, catus.get_width(), catus.get_height())
        screen.blit(catus, (x,y))
        if dinoHitBox.colliderect(catusHitBox):
            #print("hit")
            catusList.remove((x, y))
            lives -= 1
   
    spawnTime += deltaTime
    if spawnTime > 1.5:
        new_x = Width + random.randint(0, 200)
        new_y = random.randint(0, Height - catus.get_height())   # 2000 ms = 2 seconds
        catusList.append((new_x,new_y))
        
        spawnTime = 0
        
    catus_x -= speed * deltaTime


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if directiony == 1:
        MidpointDino -= 5
    if directiony == -1:
        MidpointDino += 5

    if sixseven:
        threading.Thread(target=playsound, args=('67.mp3',), daemon=True).start()
        lives = min(lives+1, 5)
        #random_color = random.randint(1, 255) 
        #screen.fill((random_color, random_color, random_color))
        if meme_img is not None and meme_start_time is None:
            meme_start_time = time.time()
            cv.imshow(meme_window_name, meme_img)
            cv.moveWindow(meme_window_name, 0, 0)

        #screen.blit(Image67, (150,Midpoint))
        #pygame.display.flip()
        #pygame.display.flip()
        sixseven = False
        #pygame.display.flip()
    #if direction == 0:
        #MidpointDino = Midpoint
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_UP]:
        #direction = 1
        
        #MidpointDino -= 0.3
        
        
    #elif keys[pygame.K_DOWN]:
        
        #direction = -1
        
        #MidpointDino += 0.3
        
    #else:
        #direction = 0

    pygame.display.flip()
    pygame.quit
    cv.imshow('frame-1', img)
    cv.moveWindow('frame-1', 600, 100)
    if meme_start_time is not None and time.time() - meme_start_time > 3.0:
        cv.destroyWindow(meme_window_name)
        meme_start_time = None

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break

cap.release()
cv.destroyAllWindows()
