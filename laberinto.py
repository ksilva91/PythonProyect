import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

pygame.init()

# set up the window
WHITE = (255, 255, 255)
DISPLAYSURF = pygame.display.set_mode((430, 430), 0, 32)
pygame.display.set_caption('Laberinto')
background=pygame.image.load('NewMaze.gif')

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
