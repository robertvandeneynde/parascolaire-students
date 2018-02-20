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

Xplayer = 350
Yplayer = 250
Sizeplayer = 10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1

    # TICK

    pressed = pygame.key.get_pressed()  # liste contenant l'état des touches du clavier

    # à chaque tick...
    # si Gauche est enfoncée
    if pressed[276]:
        Xplayer -= 5
        if Xplayer < Sizeplayer:
            Xplayer = Sizeplayer
    if pressed[275]:
        Xplayer += 5
        if Xplayer > 700 - Sizeplayer:
            Xplayer = 700 - Sizeplayer
    if pressed[274]:
        Yplayer += 5
        if Yplayer > 500 - Sizeplayer:
            Yplayer = 500 - Sizeplayer
    if pressed[273]:
        Yplayer -=5
        if Yplayer < Sizeplayer:
            Yplayer = Sizeplayer

    buttons = pygame.mouse.get_pressed()  # liste contenant l'état des touches de la souris : gauche/milieu/droit

    if buttons[0]:  # si le bouton de gauche de la souris est enfoncé
        position_souris = pygame.mouse.get_pos()  # liste de taille 2 avec x,y
        Xplayer = position_souris[0]
        if Xplayer < Sizeplayer:
            Xplayer = Sizeplayer
        if Xplayer > 700 - Sizeplayer:
            Xplayer = 700 - Sizeplayer
        Yplayer = position_souris[1]
    if Yplayer < Sizeplayer:
        Yplayer = Sizeplayer
    if Yplayer > 500 - Sizeplayer:
        Yplayer = 500 - Sizeplayer

    # DESSIN
    ecran.fill(NOIR)

    pygame.draw.circle(ecran, BLEU, [Xplayer, Yplayer], Sizeplayer)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()