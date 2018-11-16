#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [1420,800]
ecran = pygame.display.set_mode(taille)



NOIR = (0, 0, 0)
BLANC = [255, 255, 255]
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = [0, 0, 255]

# DÉBUT
a=b=c=d=e=f=100

finbordD=1420



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
    fini+=1421
    if fin>1420:
        fin=0

    # DESSIN
    ecran.fill(NOIR)
    
    pygame.draw.rect(ecran, ROUGE, [c,d, e,f])
    pygame.draw.circle(ecran, BLEU, [b,d], e)
    pygame.draw.circle(ecran, VERT, [a, d], e)
    
    pygame.display.flip()
    
clock.tick(24)
    
pygame.quit()