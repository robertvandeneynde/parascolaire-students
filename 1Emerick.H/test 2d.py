#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [3840, 2160]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = (255, 0, 0)
VERT = [0,255, 0]
BLEU = [0, 0, 255]

# DÉBUT
a=100
b=110
c=120
d=140
e=144
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    a=a+1
    b=b+2
    c=c+3
    d=d+1
    e=e+1

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [c,d, e,40])
    pygame.draw.circle(ecran, BLEU, [b,d], e)
    pygame.draw.circle(ecran, VERT, [a, d], e)
    
    pygame.display.flip()
    
clock.tick(60)
    
pygame.quit()