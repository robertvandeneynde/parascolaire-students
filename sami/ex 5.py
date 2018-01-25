#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

BLANC = [255, 255, 255]
NOIR = [0, 0, 0]
NOIRE = NOIR
BLANC_CREME = [255, 228, 196]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
ROSE = [253, 108, 158]	
n = [0,0,0]

# DEBUT
lol = 500
s = 1
centre = 350
print("coucou")
image_perso = pygame.image.load('caca.png').convert_alpha()
image_perso_petit = pygame.transform.rotozoom(image_perso, 0, 0.5)

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    
    if s == 1:
        lol = lol + 10
    else:
        lol = lol - 10
    
    if lol >= 700:
        s = -1
    
    if lol <=0:
        s = 1 
    
    # DESSIN
    
    ecran.fill(BLANC)

    pygame.draw.polygon(ecran, ROUGE, [[310,230], [330,390], [350,230]])
    
    if lol > 280 and lol < 420:
        pygame.draw.circle(ecran, NOIRE, [350,200], 40)
    else:
        pygame.draw.circle(ecran, ROSE, [350,200], 40)        
    
    if lol > 300 and lol < 400:
        pygame.draw.circle(ecran, NOIRE, [310,200], 40)
    else:
        pygame.draw.circle(ecran, BLANC_CREME, [310,200], 40)  
  
    if s == 1:
        pygame.draw.circle(ecran, ROUGE, [lol,80], 10)    
    else:
        pygame.draw.circle(ecran, VERT, [lol, 80], 10)
    
    if s == 1:
        pygame.draw.rect(ecran, ROUGE, [100,30, 40,20])
    else:
        pygame.draw.rect(ecran, VERT, [560,30, 40,20])
    
    ecran.blit(image_perso_petit, [250, 200])
    
    pygame.display.flip()
    clock.tick(60)
     
    
pygame.quit()