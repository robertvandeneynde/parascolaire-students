#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

XD_X = 100
XD_Y = 100
NOIR_X = 100
NOIR_Y = 45

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
VERT = [159, 200, 52]
NOIR = [0, 0, 0]
BLEU = [0, 0, 255]

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1

            if XD_X > 700:
                XD_X = 700

            if XD_Y >700:
                XD_Y = 700

    
    pressed = pygame.key.get_pressed()


    if pressed[276]:
        XD_X = XD_X - 4
    
    if pressed[275]:
        XD_X = XD_X + 4
    
    if pressed[274]: 
        XD_Y = XD_Y + 4
        
    if pressed[273]:
        XD_Y = XD_Y - 4
        
    if XD_X <= 0:
        XD_X=0
    
    if XD_X >= 660:
        XD_X=660
    
    if XD_Y <= 0 :
        XD_Y = 0 
    
    if XD_Y >= 450 :
        XD_Y = 450
        
    if XD_X - NOIR_X <= 40 :
        print("BOOOOOM")
    
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, VERT , [XD_X,XD_Y,40,50])

    pygame.draw.rect(ecran, NOIR , [NOIR_X,NOIR_Y,30,25])
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()