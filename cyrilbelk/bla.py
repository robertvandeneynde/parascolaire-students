#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [254, 108, 210]
VERT = [200, 108, 0]
BLEU = [0, 0, 85]

# DÉBUT

bla=700
sens = -1
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    if sens == 1 :
        bla = bla + 10
    else:
        bla = bla - 10
    if bla == 0:
        sens = 1
    if bla >= 700:
         bla = 0
         
    ecran.fill(BLANC)    
    # DESSIN
    
    pygame.draw.rect(ecran, ROUGE, [bla,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()