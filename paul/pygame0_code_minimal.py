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

my_position = 210
ma_position = 100
ma_hauteur = 200
sense = 1

clock = pygame.time.Clock()

fini = 0
while fini == 0:

    if sense == 1:
        my_position = my_position+1

    if sense == -1:
        my_position = my_position-1

    if my_position < 0:
        sense = 1

    if my_position > 700:
        sense = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

            pressed = pygame.key.get_pressed()  # liste contenant l'état des touches du clavier

            # à chaque tick...
            # si Gauche est enfoncée
            if pressed[276]:
                ma_position -= 5
            if pressed[275]:
                ma_position += 5
            if pressed[274]:
                ma_hauteur += 5
            if pressed[273]:
                ma_hauteur -= 5

            buttons = pygame.mouse.get_pressed()  # liste contenant l'état des touches de la souris : gauche/milieu/droit

            if buttons[0]:  # si le bouton de gauche de la souris est enfoncé
                position_souris = pygame.mouse.get_pos()  # liste de taille 2 avec x,y
                ma_position = position_souris[0]

    #DESSIN

    ecran.fill(BLANC)

    if sense == 1:
        pygame.draw.polygon(ecran, VERT, [[475,250], [375,200], [375,300]])
        pygame.draw.polygon(ecran, ROUGE, [[my_position+50, 450], [my_position-50, 400], [my_position-50, 500]])
        pygame.draw.polygon(ecran, NOIR, [[225, 250], [325, 200], [325, 300]])

    if sense == -1:
        pygame.draw.polygon(ecran, VERT, [[225,250], [325,200], [325,300]])
        pygame.draw.polygon(ecran, ROUGE, [[my_position-50, 450], [my_position+50, 400], [my_position+50, 500]])
        pygame.draw.polygon(ecran, NOIR, [[475, 250], [375, 200], [375, 300]])

    pygame.draw.rect(ecran, ROUGE, [100,200, 32,100])
    pygame.draw.circle(ecran, BLEU, [ma_position, ma_hauteur], 50)
    pygame.draw.circle(ecran, VERT, [my_position, 80], 16)

    pygame.display.flip()
    
    clock.tick(300)
    
pygame.quit()
