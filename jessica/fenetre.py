#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [900, 600]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
AQUA = [127, 255, 212]
MEDIUMBLUE = [0, 0, 205]
JAUNE = [225, 225, 0]
MAGENTAFONCE = [128, 0, 128]
HOOKER = [27, 79, 8]


sens = 1 # 5 == gauche, -5 == droite
snape = 100
potter = 5
granger = 800
neville = 50
clock = pygame.time.Clock()

# DÉBUT
weasley = 10
luna = 5

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
    
    pressed = pygame.key.get_pressed()
    
    # TICK
    potter = potter + 1
    
    if pressed[275]:
        neville = neville + 5
    if pressed[276]:
        neville = neville - 5   
        if neville >= 220 and neville <= 380:
            neville = neville - 5
    
    luna = luna + 5
    
    granger = granger - 10
    if granger == 0:
        granger = 900
    
    if pressed[275]:
        weasley = weasley + 5
        if weasley >= 220 and weasley <= 380:
             weasley = weasley + 5        
    if pressed[276]:
        weasley = weasley - 5
        
    
    if snape >= 900:
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
    pygame.draw.rect (ecran, NOIR, [15, 15, ecran.get_width() -30,  ecran.get_height() -30 ])
   
    
    if sens == -1:
        pygame.draw.rect(ecran, ROUGE, [potter,200, 20,40])
    
    pygame.draw.rect(ecran, JAUNE, [100+weasley,400, 20,40])
    
    if sens == 1:
        pygame.draw.circle(ecran, VERT, [100+snape,200], 20)
    else:
        pygame.draw.circle(ecran, VERT, [100+luna,200], 20)
        
    if sens == -1:
        pygame.draw.circle(ecran, AQUA, [luna, 80], 10)
    else:
        pygame.draw.circle(ecran, AQUA, [150, 120], 10)
    
    pygame.draw.circle(ecran, MAGENTAFONCE, [granger, 80], 15)
    
    pygame.draw.circle(ecran, HOOKER, [neville, 300], 20)
    
    if sens == 1:
        offset_y = 200
        pygame.draw.polygon(ecran, BLANC, [
            [0 + snape, 0 + offset_y],
            [-25 + snape, 25 + offset_y],
            [0 + snape, 50 + offset_y ]])
    else: 
        offset_y = 100
        pygame.draw.polygon(ecran, BLANC, [
            [0+snape,0 + offset_y],
            [25+snape, 25 + offset_y],
            [0+snape, 50 + offset_y]])
        
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()



