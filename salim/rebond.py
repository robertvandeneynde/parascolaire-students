#!coding: utf-
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
sens = 1
tosh = 5 # 10
slm = 10 # 20
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    if sens == 1:
        slm = slm + 5
    else:
        slm = slm -5
    if sens == 1:
        tosh = tosh + 5
    else:
        tosh = tosh - 5

    
    slm = slm + 10
    if tosh > 500:
        sens = - 1
    
        
    # DESSIN
    
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [tosh+100,50,200, 50]) # 115
    pygame.draw.circle(ecran, BLEU, [slm,200], 40)        # 30
    pygame.draw.circle(ecran, BLEU, [slm+100,200], 40)    # 130
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()