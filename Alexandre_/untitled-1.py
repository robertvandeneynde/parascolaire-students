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
x = 200
y = 100
change = 2
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    if change % 2 == 0:
        if x < 700:
            x += 1
        elif x > 700:
            x -= 1
            change += 1
    elif change % 2 == 1:        
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1
            change += 1
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [x,y, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()