from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 700]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT
ma_position=100
sens=1
clock = pygame.time.Clock()

HAUT = 273
BAS = 274
GAUCHE = 275
DROITE = 276

fini = 0
while fini == 0: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
        elif event.type == pygame.KEYDOWN:
            if event.key == DROITE:
                ma_position=ma_position - 100
            elif event.type == GAUCHE:
                ma_postion=ma_position + 100        
            elif event.type == HAUT:
                ma_position=ma_position - 100
            elif event.type == BAS:
                ma_position=ma_position + 100
    pressed = pygame.key.get_pressed()
    
    
    # TICK
    if sens == +1 :
        ma_position=ma_position+5
    if sens == -1 : 
        ma_position -= 5
    if ma_position>700:
        sens = -1
    if ma_position < 0:
        sens = +1
    
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [100,ma_position, 60,40])
    pygame.draw.circle(ecran, BLEU, [ma_position,200], 20)
    pygame.draw.circle(ecran, VERT, [150, ma_position], 10)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()