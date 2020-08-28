import pygame
from pygame import display, event

pygame.init()

win = display.set_mode((512, 512))
display.set_caption("SpaceWars")

x, y = 50, 50
width, height = 40, 60
velocity = 50

running = True
while running:
    pygame.time.delay(50)

    for evnt in event.get():
        if evnt.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > velocity:
        x -= velocity
    
    if keys[pygame.K_RIGHT] and x < 512 - width - velocity:
        x += velocity
    
    if keys[pygame.K_UP] and y > velocity:
        y -= velocity
    
    if keys[pygame.K_DOWN] and y < 512 - height - velocity:
        y += velocity
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    display.update()

pygame.quit()
