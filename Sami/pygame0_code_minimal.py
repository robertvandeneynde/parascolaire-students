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

image_balle = pygame.image.load('BalleDeFeu.png').convert_alpha()


# DÉBUT
pos = 500
s = 1

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    if s == 1:
        pos = pos + 10
    else:
        pos = pos - 10
    
    if pos >= 700:
        s = -1
    
    if pos <=0:
        s = 1     
    
   
    # DESSIN
    ecran.fill(NOIR)
    #Dessin du contour
    pygame.draw.rect(ecran, NOIR, [0,490, 750,10])
    pygame.draw.rect(ecran, NOIR, [0,0, 750,10])
    pygame.draw.rect(ecran, NOIR, [690,0, 200,750])
    pygame.draw.rect(ecran, NOIR, [0,0, 10,500])
    ##
    pygame.draw.polygon(ecran, ROUGE, [[pos,250], [350,200], [350,300]])
    pygame.draw.circle(ecran, VERT, [pos, 250], 10)
  
    pygame.draw.circle(ecran, BLEU, [100, 350], 10)
    ecran.blit(image_balle, [0, 0])
    pygame.display.flip()
    clock.tick(60)
    #miss a ete ici :)
pygame.quit()
