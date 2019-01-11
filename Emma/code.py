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
a = 100
b = 100
c = 100
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    a = a+1
    b = b+2
    c = c+3
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [500,b,15,40])
    pygame.draw.circle(ecran, ROUGE, [c,300,], 35)
    pygame.draw.circle(ecran, ROUGE, [90, a], 25)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
