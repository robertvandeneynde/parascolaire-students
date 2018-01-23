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
AQUA = [127, 255, 212]
MEDIUMBLUE = [0, 0, 205]

sens = 1 # 5 == gauche, -5 == droite
snape = 100
clock = pygame.time.Clock()

# DÉBUT
taille = 0.2
weasley = 0.1

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 80
            # elif est un raccourci pour "if... else... if ... else..."
        elif event.type == pygame.KEYDOWN:
                    print("La touche numero", event.key)  
                    if event.key == 276:
                        snape = snape - 100
                    elif event.key == 275:
                        snape = snape + 100
                        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Clic en", event.pos[0], event.pos[1])
            
            snape = event.pos[0]             
     
    # TICK
    if snape >= 700:
        sens = 1
    if snape <= 0:
        sens = -1     

          
    if sens == 1:
        snape -=5
    else :
        snape +=5
        
    #print(snape)
    
    # DESSIN
    
    ecran.fill(BLANC)
    if sens == -1:
        pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.rect(ecran, ROUGE, [100,400, 20,40])
    if sens == 1:
        pygame.draw.circle(ecran, VERT, [100+snape,200], 20)
    if sens == -1:
        pygame.draw.circle(ecran, AQUA, [150, 80], 10)
    pygame.draw.circle(ecran, MEDIUMBLUE, [snape, 80], 15)
    if sens == 1:
        pygame.draw.polygon(ecran, ROUGE, [
            [0+snape, 50*taille],
            [100*taille+snape, 0],
            [100*taille+snape, 100*taille]])
    else: 
        pygame.draw.polygon(ecran, ROUGE, [
            [200*taille+snape, 50*taille],
            [100*taille+snape, 0],
            [100*taille+snape, 100*taille]])
        
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()



