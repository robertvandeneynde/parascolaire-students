
     #pygame0_code_minimal.py #White #Dark #txt #download 
 
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
#debut
ma_position=[150,80]
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    # tick
    
    #dessin
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [600,300, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 40)
    pygame.draw.circle(ecran, VERT, [150,80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()



