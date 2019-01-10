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
x=0
y=0
pos_x_rect=0
pos_y_rect=0
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 275:
                x=x-100
            if event.key == 273:
                y=y-50

    # TICK
    x=x+3
    y=y+2
    pos_x_rect = pos_x_rect+2
    if y>230:
        y=230
    if x >= pos_x_rect -20:
        x = pos_x_rect-20
           
    # DESSIN
    ecran.fill(BLANC)
    pygame.draw.circle(ecran, BLEU, [x,y], 20)
    pygame.draw.rect(ecran, ROUGE, [0,250, 700,50]) 
    pygame.draw.rect(ecran, VERT, [pos_x_rect,pos_y_rect,50,500])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()