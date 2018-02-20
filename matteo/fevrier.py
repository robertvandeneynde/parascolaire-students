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
x = 350
y = 250
# DÉBUT

clock = pygame.time.Clock()
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    x += 5
    y += 0
    print(x,y)
    if x > 700:
        x = 0
        print("hors de l'ecran")
    
    # DESSIN
    ecran.fill(BLANC)
    
    
    pygame.draw.circle(ecran, VERT, [x, y], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()