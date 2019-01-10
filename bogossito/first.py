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
a=100
x=350
y=255

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1 
        
    position_souris = pygame.mouse.get_pos() # liste de taille 2 avec x,y 
    # TICK
    x = position_souris[0]
    y=position_souris[1]
    
    # DESSIN
    ecran.fill(BLANC)
    pygame.draw.rect(ecran, ROUGE, [x-50,y-5, 20,10])
    pygame.draw.circle(ecran, BLEU, [x,y],10)
    pygame.draw.rect(ecran, ROUGE, [x+30,y-5, 20,10])
    pygame.draw.rect(ecran, ROUGE, [x-3,y-50, 10,20])
    pygame.draw.rect(ecran, ROUGE, [x-3,y+25, 10,20])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()