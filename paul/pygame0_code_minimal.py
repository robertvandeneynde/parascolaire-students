#!coding: utf-8
from __future__ import print_function, division

import pygame
import random

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

livecount = 100

# DÉBUT

clock = pygame.time.Clock()

countspawn = 0

class Player:
    pass

player = Player()
player.x = 350
player.y = 250
player.size = 10

class Mob:
    pass

gérard = Mob()
gérard.x  = 680
gérard.y = 480
gérard.size = 20

mobs = []
mobs.append(gérard)

m = Mob()
m.x  = 680-2*100
m.y = 480
m.size = 20
mobs.append(m)

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

            
    countspawn += 1
    if countspawn == 2*60:
        countspawn = 0
        aleax = random.randint(0, 700 - m.size)
        aleay = random.randint(0, 500 - m.size)
        m = Mob()
        m.x  = aleax
        m.y = aleay
        m.size = 20
        mobs.append(m)

    i = 0
    while i < len(mobs):
        if mobs[i].x + 10 > player.x:
            mobs[i].x -= 1
        if mobs[i].x + 10 < player.x:
            mobs[i].x += 1
        if mobs[i].y + 10 > player.y:
            mobs[i].y -= 1
        if mobs[i].y + 10 < player.y:
            mobs[i].y += 1
        i += 1

    i = 0
    while i < len(mobs):
        dx = mobs[i].x + 10 - player.x
        dy = mobs[i].y + 10 - player.y

        if dx ** 2 + dy ** 2 < (mobs[i].size/2 + player.size) ** 2:
            livecount -= 1
            print(livecount)
            if livecount == 0:
                fini = 1
        i += 1

    a = random.randint(0, len(mobs)-1)
    b = random.randint(0, len(mobs)-1)

    if a != b:
        abx = mobs[a].x + mobs[b].x
        aby = mobs[a].y + mobs[b].y

        if abx ** 2 + aby ** 2 < (mobs[a].size/2 + mobs[b].size/2) ** 2:
            del mobs[a]
            del mobs[b]


    # DESSIN
    ecran.fill(NOIR)

    pygame.draw.circle(ecran, BLEU, [player.x, player.y], player.size)
    
    #pygame.draw.rect(ecran, ROUGE, [gérard.x, gérard.y, gérard.size, gérard.size])
    #pygame.draw.rect(ecran, ROUGE, [mobs[1].x, mobs[1].y, mobs[1].size, mobs[1].size])
    #pygame.draw.rect(ecran, ROUGE, [m.x, m.y, m.size, m.size])

    i = 0
    while i < len(mobs):
        pygame.draw.rect(ecran, ROUGE, [mobs[i].x, mobs[i].y, mobs[i].size, mobs[i].size])
        i += 1

    pygame.display.flip()

    clock.tick(60)

pygame.quit()