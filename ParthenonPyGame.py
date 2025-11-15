import pygame
import random
# also new
import time
#Sounds NEW STUFF
from playsound import playsound

pygame.init()
Width = 800
Height = 300
last_time = 0
Hand67 = False

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

running = True
pygame.display.Info()

catus_x = Width
catusList = [(400,Midpoint),(600,Midpoint),(800,Midpoint)]

start_x = 50
start_y = 50
speed = 0.1
lives = 3
hit_cooldown = 0.5

DinoMove = True
while running:
    if Hand67 == False:
        screen.fill((186, 149, 97))
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,MidpointDino))
    screen.blit(catus, (catus_x,Midpoint))
    
    

    
    for i in range(lives):
        screen.blit(scaled_heart, (100 + i * 40,10))
    if lives == 0:
        pygame.quit()

    dinoHitBox = pygame.Rect(start_x, MidpointDino, scaled_charachter.get_width(), scaled_charachter.get_height())
   
    for i in range(len(catusList)):
        catusList[i] = (catusList[i][0] - speed, catusList[i][1])   
    
    for x,y in catusList:
        catusHitBox = pygame.Rect(x,y, catus.get_width(), catus.get_height())
        screen.blit(catus, (x,y))
        if dinoHitBox.colliderect(catusHitBox) and lives > 0:
            print("hit")
            catusList.remove((x, y))
            lives -= 1
            

    current = pygame.time.get_ticks()
    if current - last_time > 1500:
        new_x = Width + random.randint(0, 200)
        new_y = random.randint(0, Height - catus.get_height())   # 2000 ms = 2 seconds
        catusList.append((new_x,new_y))
        last_time = current
        
    catus_x -= 0.1

    if Hand67:
        playsound('67.mp3')
        random_color = random.randint(1, 255) 
        screen.fill((random_color, random_color, random_color))
        screen.blit(Image67, (150,Midpoint))
        pygame.display.flip()
        time.sleep(5)
        pygame.display.flip()
        Hand67 = False
        pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #if direction == 1:
        #MidpointDino -= 0.3
    #if direction == -1:
        #MidpointDino += 0.3
    #if direction == 0:
        #MidpointDino = Midpoint
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 1
        if DinoMove:
            MidpointDino -= 0.3
        
        
    elif keys[pygame.K_DOWN]:
        
        direction = -1
        if DinoMove:
            MidpointDino += 0.3
    
    else:
        direction = 0
    if keys[pygame.K_a]:
        Hand67 = True
    pygame.display.flip()
pygame.quit
