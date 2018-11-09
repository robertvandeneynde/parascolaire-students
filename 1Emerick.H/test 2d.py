#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [3840,2160]
ecran = pygame.display.set_mode(taille)

NOIR = (46, 255, 0)
BLANC = [255, 255, 255]
ROUGE = (255, 0, 0)
VERT = (46, 255, 0)
BLEU = [0, 0, 255]

# DÉBUT
a=100
b=101
c=102
d=103
e=104
f=105
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    b=b+2
    a=a+1
    f=f+3
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [c,d, e,f])
    pygame.draw.circle(ecran, BLEU, [b,d], e)
    pygame.draw.circle(ecran, VERT, [a, d], e)
    
    pygame.display.flip()
    
clock.tick(24)
    
pygame.quit()