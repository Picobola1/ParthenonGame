import pygame

pygame.init()
Width = 800
Height = 300

screen = pygame.display.set_mode((Width,Height))
direction = 0
charachter = pygame.image.load("BlueDino1.png").convert()
scaled_charachter = pygame.transform.scale(charachter,(100,100))

Midpoint = Height/2

running = True
pygame.display.Info()

start_x = 50
start_y = 50
speed = 0.1
while running:
    screen.fill((68,243,109))
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,Midpoint))
    #print(direction)
   


    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 1
        Midpoint -= 0.5
    elif keys[pygame.K_DOWN]:
        direction = -1
        Midpoint += 0.5
    else:
        direction = 0
    pygame.display.flip()
pygame.quit
