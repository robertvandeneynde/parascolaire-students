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
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    a = a+1
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [300,200, 15,40])
    pygame.draw.circle(ecran, BLEU, [100,150], 20)
    pygame.draw.circle(ecran, VERT, [a, 90], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
