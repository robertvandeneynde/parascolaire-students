
#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [1200,500]
ecran = pygame.display.set_mode(taille)

NOIR = [252, 253, 254]
BLANC = [255, 255, 255]
ROUGE = [13, 142, 123]
VERT = [45, 22, 0]
BLEU = [0, 0, 255]

# DÉBUT
ma_position= 100

clock = pygame.time.Clock()

fini = 0
bleux = 100
bleuy = 100

while fini == 0:
    bleux=bleux+2
    bleuy=bleuy+5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276: # touche gauche
                bleuy = bleuy - 100
            elif event.key == 275: # touche droite
                bleux = bleux + 100
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos est une liste de taille 2 contenant le x et le y
            print("Clic en", event.pos[0], event.pos[1])
            ma_position = event.pos[0]            
    
    # TICK

    ecran.fill(BLANC)
    
    # DESSIN

    pygame.draw.rect(ecran, ROUGE, [100,200, bleuy,255])
    pygame.draw.circle(ecran, BLEU, [bleux,123],34)
    pygame.draw.circle(ecran, VERT, [bleuy,80], 55)

    pygame.display.flip()
    
    clock.tick(200) 
    
pygame.quit() 