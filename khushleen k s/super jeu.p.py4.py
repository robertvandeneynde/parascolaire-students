#!coding: utf-8

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
a= 350
b= 4
c= 0
sens = 1
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
     # TICK 
    if a <= 690:
        a = a-1
    if b <= 686:
        b = b+2
    if c <= 686 :
        c = c+3
    else:
            a = a +2
            
    if a < 350:
        sens = 1
    print(sens, a)
    

     # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [a,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [b,200], 20)
    pygame.draw.circle(ecran, VERT, [c, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
    
