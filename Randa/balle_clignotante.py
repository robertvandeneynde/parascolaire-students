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
ORANGE  = [255, 128, 64]  
DEAN = 0
POSITION = 0
# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    print(DEAN)
    
    DEAN = DEAN + 2
    if DEAN >255:
        print("coucou")
        DEAN = 2
        
    print(POSITION)
    
    POSITION = POSITION + 2
    if POSITION >700:
        POSITION = 0
    
    
        
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [50,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, [DEAN,DEAN,DEAN], [POSITION, 80], 10)
    # pygame.draw.circle(ecran, ORANGE, [150+20, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
    
      