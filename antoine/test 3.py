
     #pygame0_code_minimal.py #White #Dark #txt #download 
 
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
#debut
ma_position=150
sens=+1
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    # tick
    ma_position=ma_position+1 
    if ma_position>=700:
        sens=-1
    if ma_position<=0:
        sens=+1
        
    if sens==-1:
        ma_position -= 1
    else:
        ma_position += 1
       
        
 
    #dessin
  
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [600,300, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 40)
    pygame.draw.circle(ecran, VERT, [ma_position,80], 10)

    pygame.display.flip()
    
    clock.tick(00)
    
pygame.quit()



