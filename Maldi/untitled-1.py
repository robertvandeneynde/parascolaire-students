
#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [600, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [252, 253, 254]
BLANC = [255, 255, 255]
ROUGE = [13, 0, 123]
VERT = [0, 22, 0]
BLEU = [0, 0, 255]

# DÉBUT
ma_position= 100

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    ecran.fill(BLANC)
    
    # DESSIN

    pygame.draw.rect(ecran, ROUGE, [100,200, 20,255])
    pygame.draw.circle(ecran, BLEU, [300,400], 4)
    pygame.draw.circle(ecran, VERT, [100,80], 55)

    pygame.display.flip()
    
    clock.tick(200) 
    
pygame.quit() 