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

class Player:
    pass

player = Player()
player.x = 350
player.y = 250
player.size = 10

class Mob:
    pass

kh = Mob()
kh.x = 695
kh.y = 495
kh.length = 15

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
        player.x -= 5
        if player.x < player.size:
            player.x = player.size
    if pressed[275]:
        player.x += 5
        if player.x > 700 - player.size:
            player.x = 700 - player.size
    if pressed[274]:
        player.y += 5
        if player.y > 500 - player.size:
            player.y = 500 - player.size
    if pressed[273]:
        player.y -=5
        if player.y < player.size:
            player.y = player.size

    buttons = pygame.mouse.get_pressed()  # liste contenant l'état des touches de la souris : gauche/milieu/droit

    if buttons[0]:  # si le bouton de gauche de la souris est enfoncé
        position_souris = pygame.mouse.get_pos()  # liste de taille 2 avec x,y
        player.x = position_souris[0]
        if player.x < player.size:
            player.x = player.size
        if player.x > 700 - player.size:
            player.x = 700 - player.size
        player.y = position_souris[1]
        if player.y < player.size:
            player.y = player.size
        if player.y > 500 - player.size:
            player.y = 500 - player.size

    # DESSIN
    ecran.fill(NOIR)

    pygame.draw.circle(ecran, BLEU, [player.x, player.y], player.size)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()