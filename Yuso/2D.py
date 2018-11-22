from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
BLEUC = [128, 191, 255]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# D�BUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, BLEUC, [190,400, 80,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, VERT, [150, 80], 50)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()