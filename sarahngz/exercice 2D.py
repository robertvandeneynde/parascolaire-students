#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
BRUN = [85, 56, 45]
SARAH = [52, 218, 201]
CACTUS = [215, 36, 215]

# DÉBUT
a=100
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, CACTUS, [a,400, 60,100])
    pygame.draw.circle(ecran,SARAH, [100,300], 40)
    pygame.draw.circle(ecran, BRUN, [a, 50], 9)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
