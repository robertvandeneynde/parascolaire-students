a=100
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

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [180,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [200,500], 90)
    pygame.draw.circle(ecran, VERT, [140, 60], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
