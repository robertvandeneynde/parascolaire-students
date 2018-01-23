#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 700]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
sens=0
pos=0
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    if pos == 700:
        sens = 1
    if pos ==0:
                        sens = 0
    if sens == 0:
        pos = pos + 10
    if sens == 1:
                pos = pos -10
                
    
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, VERT, [pos, pos], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()