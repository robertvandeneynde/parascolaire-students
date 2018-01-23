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
tosh = 5
slm = 10
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    tosh = tosh + 5
    slm = slm + 3
    ecran.fill(BLANC)
    
    # DESSIN
    
    pygame.draw.rect(ecran, ROUGE, [slm,100,200, 40])
    pygame.draw.circle(ecran, BLEU, [slm,200], 40)
    pygame.draw.circle(ecran, BLEU, [slm,200], 40)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()