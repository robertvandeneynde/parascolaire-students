#!coding: utf-8
from __future__ import print_function, division

import pygame
pygame.init()

taille = [8192,4320]
ecran = pygame.display.set_mode(taille)



NOIR = (0, 0, 0)
BLANC = [255, 255, 255]
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = [0, 0, 255]

# DÉBUT
a=b=c=d=e=f=100


clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    a=a+2
    b=b+4
    c=c+6
    d=d+4
  
    
    if a>=8300:
        a=-50        
    if b>=8300:
        b=-50
    if c>=8300:
        c=-50
    if d>=4400:
       d=-50
        
        


    # DESSIN
    ecran.fill(NOIR)
    
    pygame.draw.rect(ecran, ROUGE, [int(c),int(d), int(e),int(f)])
    pygame.draw.circle(ecran, BLEU, [int(b),int(d)], int(e))
    pygame.draw.circle(ecran, VERT, [int(d),int(a)], int(e))
    

    
    pygame.display.flip()
    
    clock.tick(1000)
    
pygame.quit()