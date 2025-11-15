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
scaled_charachter = pygame.transform.scale(charachter,(70,70))

Midpoint = Height/2
MidpointDino = Height/2

running = True
pygame.display.Info()

catus_x = Width
catusList = [400,600,800]
start_x = 50
start_y = 50
speed = 0.1


while running:
    screen.fill((48, 105, 152))
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,MidpointDino))
    screen.blit(catus, (catus_x,Midpoint))
    dinoHitBox = pygame.Rect(start_x, MidpointDino, scaled_charachter.get_width(), scaled_charachter.get_height())
   
    for i in range(len(catusList)):
        catusList[i] -= speed   
    
    for x in catusList:
        catusHitBox = pygame.Rect(x, Midpoint, catus.get_width(), catus.get_height())
        screen.blit(catus, (x, Midpoint))
        if dinoHitBox.colliderect(catusHitBox):
            print("you got hit")
    current = pygame.time.get_ticks()
    if current - last_time > 1500:   # 2000 ms = 2 seconds
        catusList.append(Width + random.randint(0, 200))
        last_time = current
        

    #collison = dinoHitBox.colliderect(catusHitBox)
    #if collison:
        #print("DINO TOUCHED CATUS")
    #print(direction)
    catus_x -= 0.1


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 1
        MidpointDino -= 0.3
    elif keys[pygame.K_DOWN]:
        direction = -1
        MidpointDino += 0.3
    else:
        direction = 0
    pygame.display.flip()
pygame.quit
