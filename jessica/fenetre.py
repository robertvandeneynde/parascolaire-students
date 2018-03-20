#!coding: utf-8
from __future__ import print_function, division

from vec3_utils import *

print(cosd(30))

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
ROUGEPALE = [255, 125, 125]
JAUNEPALE = [224, 243, 169]
ORONGEPALE = [254, 211, 165]

score = 0
font = pygame.font.SysFont('Calibri', 25, True, True)
image_nom_joueur = font.render("Jessica", True, BLANC)
image_score = font.render("Score: " + str(score), True, BLANC)

sens = 1 # 5 == gauche, -5 == droite
sens1 = 1
snape = 100
potter = 5
granger = 800
neville = 50
draco = 50
albus = 250
clock = pygame.time.Clock()

imagen_defondo = pygame.image.load("espace.jpg").convert_alpha()
imagen_balledefeu = pygame.image.load("BalleDeFeu.png").convert_alpha()
# DÉBUT
luna = 5

t = 0
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
    t = t + 1
    potter = potter + 1
    
    if pressed[275]:
        draco = draco + 5
    if pressed[276]:
        draco = draco - 5   
        if draco >= 220 and draco <= 380:
            draco = draco - 5
    
    luna = luna + 5
    
    granger = granger - 4
    if granger == 0:
        granger = 900
    
    if snape >= 900:
        sens = 1
    if snape <= 0:
        sens = -1     
          
    if sens == 1:
        snape -=2
    else :
        snape +=2
        
        
    if neville >= 900:
        sens = 1
    if neville <= 0:
        sens = -1
        
    if sens == 1:
        neville -=5
    else:
        neville +=5
        
   
        
    #print(snape)
    
    # DESSIN
    
    ecran.fill(NOIR)
    
    ecran.blit(imagen_defondo, [0,0])
    ecran.blit(imagen_balledefeu, [0,0])

    if sens == 1:
        pygame.draw.circle(ecran, VERT, [100+snape,200], 20)
    else:
        pygame.draw.circle(ecran, VERT, [100,potter], 20)
        if potter == 600:
            potter = 200
    if sens == -1:
        pygame.draw.circle(ecran, AQUA, [luna, 80], 10)
    else:
        pygame.draw.circle(ecran, AQUA, [150, snape], 10)
    
    pygame.draw.circle(ecran, MAGENTAFONCE, [granger, 80], 15)
    
    pygame.draw.circle(ecran, HOOKER, [albus, neville], 20)
    pygame.draw.circle(ecran, [255,255,255], [draco, 50], 20)
    
    pygame.draw.circle(ecran, [255,0,0], [int(200 + 100*cosd(t)), int(200 + 100*sind(t))], 20)    
    
    if sens == 1:
        offset_y = 200
        pygame.draw.polygon(ecran, NOIR, [
            [0 + snape, 0 + offset_y],
            [-25 + snape, 25 + offset_y],
            [0 + snape, 50 + offset_y ]])
    else: 
        offset_y = 100
        pygame.draw.polygon(ecran, NOIR, [
            [0+snape,0 + offset_y],
            [25+snape, 25 + offset_y],
            [0+snape, 50 + offset_y]])
        
    ecran.blit(image_nom_joueur, [20,20])
    ecran.blit(image_score, [600,20])
    
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()



