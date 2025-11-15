import pygame
import random
import cv2 as cv
import numpy as np
import time
from playsound import playsound

pygame.init()
Width = 800
Height = 300
last_time = 0
## head
cap = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
detectedx = 0
detectedy = 0
widht = 0
height = 0
third = height // 3

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
speed = 3
lives = 3


DinoMove = True
while True: 
    if Hand67 == False:
        screen.fill((186, 149, 97))
    ret, img = cap.read()

    width = img.shape[1]
    height = img.shape[0]
    third = height // 3

    cv.line(img, (0, third), (img.shape[1], third), (255, 0, 0), thickness=2)
    cv.line(img, (0, 2*third), (img.shape[1], 2*third), (255, 0, 0), thickness=2)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    

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
    #screen.fill((48, 105, 152))
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,MidpointDino))
    screen.blit(catus, (catus_x,Midpoint))
    dinoHitBox = pygame.Rect(start_x, MidpointDino, scaled_charachter.get_width(), scaled_charachter.get_height())
    for i in range(lives):
        screen.blit(scaled_heart, (100 + i * 40,10))
    if lives == 0:
        pygame.quit()

    for i in range(len(catusList)):
        catusList[i] = (catusList[i][0] - speed, catusList[i][1])   
    
    for x,y in catusList:
        catusHitBox = pygame.Rect(x,y, catus.get_width(), catus.get_height())
        screen.blit(catus, (x,y))
        if dinoHitBox.colliderect(catusHitBox):
            print("hit")
            catusList.remove((x, y))
            lives -= 1
    current = pygame.time.get_ticks()
    if current - last_time > 1500:
        new_x = Width + random.randint(0, 200)
        new_y = random.randint(0, Height - catus.get_height())   # 2000 ms = 2 seconds
        catusList.append((new_x,new_y))
        last_time = current
        
    catus_x -= 3


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if directiony == 1:
        MidpointDino -= 5
    if directiony == -1:
        MidpointDino += 5
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

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    if not ret:
        break

cap.release()
cv.destroyAllWindows()

    
