from __future__ import print_function, division

import pygame
pygame.init()
a=100
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    a=a+5
    if a==700:
        a=a-5
    while 0<a<700:
        a=a-5
        if a==0:
            a=a+5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, VERT, [a, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()