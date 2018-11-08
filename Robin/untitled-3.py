#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()
a=100

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
    while (a<650) :
        pygame.draw.circle(ecran, NOIR, [150,80], 10)
        a = a+1
   
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, NOIR, [150,80], 10)
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.rect(ecran, VERT, [150,150, 40,60])
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()