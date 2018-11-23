
#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

XD_X = 100
XD_Y = 100
NOIR_X = 325
NOIR_Y = 250
SCORE = 1 
WIN = 0
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
VERT = [159, 200, 52]
NOIR = [0, 0, 0]
BLEU = [0, 0, 255]
JAUNE = [255,215,0]

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    pressed = pygame.key.get_pressed()
    if pressed[276]: #gauche
        XD_X = XD_X - 4
    if pressed[275]: #droite
        XD_X = XD_X + 4
    if pressed[274]: #bas
        XD_Y = XD_Y + 4
    if pressed[273]: #haut
        XD_Y = XD_Y - 4
        
    if XD_X <= 0: #bordure gauche
        XD_X=0
    if XD_X >= 660: #bordure droite
        XD_X=660
    if XD_Y <= 0 : #bordure haut
        XD_Y = 0
    if XD_Y >= 450 : #bordure bas
        XD_Y = 450
        
    if  NOIR_X - 40 <= XD_X <= NOIR_X +30 and -50 <= XD_Y - NOIR_Y <= 25:
        if WIN == 0 :
                 SCORE = SCORE + 1
        if SCORE <= 1000  and WIN == 0 :
           print(SCORE)
    if SCORE >= 1000 and WIN == 0 :
        # PAsse gagne de 0 a 1 et tu va prin gg wp
        WIN = 1 
        print ("gg wp")
    ecran.fill(NOIR)
    pygame.draw.rect(ecran, BLANC , [50,50,600,400])
    pygame.draw.rect(ecran, VERT , [XD_X,XD_Y,40,50])
    pygame.draw.rect(ecran, JAUNE , [NOIR_X,NOIR_Y,30,25])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
