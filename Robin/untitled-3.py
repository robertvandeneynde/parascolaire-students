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
x=0
y=0
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    # TICK
    x=x+5
    y=y+2
    if y>230:
        x=x-5
        y=y-2
    if x>180:
        x=x-5
        y=y-2

    # DESSIN
    ecran.fill(BLANC)
    pygame.draw.circle(ecran, BLEU, [x,y], 20)
    pygame.draw.rect(ecran, ROUGE, [0,250, 700,50]) 
    pygame.draw.rect(ecran, VERT, [200,0,50,500])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()