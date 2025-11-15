import pygame
import random

pygame.init()
Width = 800
Height = 300
last_time = 0

screen = pygame.display.set_mode((Width,Height))
direction = 0
charachter = pygame.image.load("BlueDino1.png").convert()
catus = pygame.image.load("Cactus.png").convert()
scaled_charachter = pygame.transform.scale(charachter,(60,60))

Midpoint = Height/2
MidpointDino = Height/2

running = True
pygame.display.Info()

catus_x = Width
catusList = [(400,Midpoint),(600,Midpoint),(800,Midpoint)]

start_x = 50
start_y = 50
speed = 0.1


DinoMove = True
while running:
    screen.fill((48, 105, 152))
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,MidpointDino))
    screen.blit(catus, (catus_x,Midpoint))
    dinoHitBox = pygame.Rect(start_x, MidpointDino, scaled_charachter.get_width(), scaled_charachter.get_height())
   
    for i in range(len(catusList)):
        catusList[i] = (catusList[i][0] - speed, catusList[i][1])   
    
    for x,y in catusList:
        catusHitBox = pygame.Rect(x,y, catus.get_width(), catus.get_height())
        screen.blit(catus, (x,y))
        if dinoHitBox.colliderect(catusHitBox):
            print("you got hit")
    current = pygame.time.get_ticks()
    if current - last_time > 1500:
        new_x = Width + random.randint(0, 200)
        new_y = random.randint(0, Height - catus.get_height())   # 2000 ms = 2 seconds
        catusList.append((new_x,new_y))
        last_time = current
        
    catus_x -= 0.1


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if direction == 1:
        MidpointDino -= 0.3
    if direction == -1:
        MidpointDino += 0.3
    if direction == 0:
        MidpointDino = Midpoint
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