import pygame

pygame.init()
Width = 800
Height = 300

screen = pygame.display.set_mode((Width,Height))
direction = 0
charachter = pygame.image.load("BlueDino1.png").convert()
catus = pygame.image.load("Cactus.png").convert()
scaled_charachter = pygame.transform.scale(charachter,(100,100))

Midpoint = Height/2
MidpointDino = Height/2

running = True
pygame.display.Info()

catus_x = 500
start_x = 50
start_y = 50
speed = 0.1
while running:
    screen.fill((48, 105, 152))
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,MidpointDino))
    screen.blit(catus, (catus_x,Midpoint))
    dinoHitBox = pygame.Rect(start_x, MidpointDino, scaled_charachter.get_width(), scaled_charachter.get_height())
    catusHitBox = pygame.Rect(catus_x, Midpoint, catus.get_width(), catus.get_height())

    collison = dinoHitBox.colliderect(catusHitBox)
    if collison:
        print("DINO TOUCHED CATUS")
    #print(direction)
    catus_x -= 0.1


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 1
        MidpointDino -= 0.5
    elif keys[pygame.K_DOWN]:
        direction = -1
        MidpointDino += 0.5
    else:
        direction = 0
    pygame.display.flip()
pygame.quit
