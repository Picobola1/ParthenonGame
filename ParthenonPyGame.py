import pygame

pygame.init()
Width = 640
Height = 640

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
    ##this is while the game is going so infinte loop
    screen.blit(scaled_charachter, (start_x,Midpoint))
    print(direction)
    start_x += speed

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = -1
            elif event.key == pygame.K_DOWN:
                direction = 1
        ## if not up or down
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                direction = 0
    pygame.display.flip()
pygame.quit
