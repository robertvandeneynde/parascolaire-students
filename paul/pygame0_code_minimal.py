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

my_position = 210
sense = 1

clock = pygame.time.Clock()

fini = 0
while fini == 0:

    if sense == 1:
        my_position = my_position+1

    if sense == -1:
        my_position = my_position-1

    if my_position < 0:
        sense = 1

    if my_position > 700:
        sense = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    

    # DESSIN
    ecran.fill(BLANC)

    if sense == 1:
        pygame.draw.polygon(ecran, NOIR, [[400,250], [300,200], [300,300]])

    if sense == -1:
        pygame.draw.polygon(ecran, NOIR, [[300,250], [400,200], [400,300]])

    pygame.draw.rect(ecran, ROUGE, [100,200, 32,100])
    pygame.draw.circle(ecran, BLEU, [100,200], 50)
    pygame.draw.circle(ecran, VERT, [my_position, 80], 16)

    pygame.display.flip()
    
    clock.tick(300)
    
pygame.quit()
