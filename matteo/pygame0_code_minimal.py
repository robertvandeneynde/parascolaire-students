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
a = 5
sens = 1
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    if sens == 1:
        a -= 5
    else:
        a += 5
                    
    print(a)
    if a > 700:
        sens = 1
    else:    
        if a < 0:
            sens = -1

    
    ecran.fill(BLANC)
    
    # DESSIN
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [20,200], 20)
    pygame.draw.circle(ecran, VERT, [a, 80], 50)
    pygame.draw.rect(ecran, ROUGE, [400, 80, 50, 20])
    pygame.draw.polygon(ecran, ROUGE, [[a,50], [a+100,0], [a+100,100]])
    
    pygame.display.flip()
    
    clock.tick(60) # 60 images par sec, 60 fps
    
pygame.quit()

