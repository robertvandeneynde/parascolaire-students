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

clock = pygame.time.Clock()
x = 200
y = 100
change = 0
bouge = 0
fini = 0
ma_position = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
     
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [200,100, 40,80])
    pygame.draw.circle(ecran, BLEU, [x,100], 20)
    pygame.draw.circle(ecran, VERT, [150, 80], 10)
    if change == 0:
        pygame.draw.polygon(ecran, ROUGE, [[x , y ], [x + 50, y],  [x +50 , y+ 50][x,y +50 ]])
        x += 1
        y += 1
    else:
        pygame.draw.polygon(ecran, VERT, [[x + 100 - 50, 80 + 50 - 50],  [x + 0 - 50, 80 + 0 - 50],  [x+ 0 - 50, 80 + 100 - 50]])
        change = 0
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
# exercice 12