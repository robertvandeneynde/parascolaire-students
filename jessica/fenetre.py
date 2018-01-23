#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
AQUA = [127, 255, 212]
MEDIUMBLUE = [0, 0, 205]
MA_POSITION = 100


clock = pygame.time.Clock()

# DÉBUT



fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 80
    
    # TICK
    
    MA_POSITION = MA_POSITION + 5
    if MA_POSITION == 700:
                           MA_POSITION = 0
          
    print(MA_POSITION)
    
    # DESSIN
    
    ecran.fill(NOIR)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, VERT, [100,200], 20)
    pygame.draw.circle(ecran, AQUA, [150, 80], 10)
    pygame.draw.circle(ecran, MEDIUMBLUE, [MA_POSITION, 80], 15)
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()