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
a=200
b=150


clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    a=a+3
    b=a+1

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran,NOIR , [10 ,456, 20,40])
                            
                       
    pygame.draw.circle(ecran, BLEU, [b,200], 20)
    pygame.draw.circle(ecran, VERT, [a, 80], 78)
    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()