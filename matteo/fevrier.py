#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [204, 255, 0]
BLEU = [0, 105, 255]

# DÉBUT

x = 350
y = 250

px = 5
py = 5

DROITE = 275
GAUCHE = 276

clock = pygame.time.Clock()
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key, "e")     
    
    pressed = pygame.key.get_pressed()
    
    # TICK
    x += 5
    y += 0
    if pressed[275]:
        px += 3
    py += 1
    #print(x,y)
    if x > 700:
        x = 0
        print("hors de l'ecran")
    
    # DESSIN
    ecran.fill(BLANC)
    
    
    pygame.draw.rect(ecran, BLEU, [90, 200, x, y])    
    pygame.draw.circle(ecran, VERT, [px,py], 20)
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()