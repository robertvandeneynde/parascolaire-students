
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
TAEMIN = 1
XBV = 500
# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
  
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
                  print("La touche numero", event.key)
                  if event.key == 276: # touche gauche
                      ma_position = ma_position - 100
                  elif event.key == 275: # touche droite
                      ma_position = ma_position + 100    
  
    # TICK
    print(TAEMIN)
    TAEMIN = TAEMIN + 1
    if TAEMIN > 700:
        TAEMIN = 0
        
    print(XBV)
    XBV = XBV - 5
    if XBV < 0 :
        XBV = 500
        
        
    # DESSIN
    ecran.fill(NOIR)
    
    pygame.draw.rect(ecran, ROUGE, [TAEMIN,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,XBV], 20)
    pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()

