#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [1200,900]
ecran = pygame.display.set_mode(taille)



NOIR = (0, 0, 0)
BLANC = [255, 255, 255]
ROUGE = (163, 163, 163)
VERT = (200, 200, 200)
BLEU = [100, 100, 100]

# DÉBUT
a=b=c=d=e=f=100


clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    a=a+0.02
    b=b+0.04
    c=c+0.06
    d=d+0.04
  
    
    if a>=1200:
        a=-50        
    if b>=1200:
        b=-50
    if c>=1200:
        c=-50
    if d>=900:
       d=-50
        
        


    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [int(c),int(d), int(e),int(f)])
    pygame.draw.circle(ecran, BLEU, [int(b),int(d)], int(e))
    pygame.draw.circle(ecran, VERT, [int(d),int(a)], int(e))
    

    
    pygame.display.flip()
    
    clock.tick(1440)
    
pygame.quit()