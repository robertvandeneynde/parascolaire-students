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
sens = 2
posx = 100
posy = 100

class segment:
    def __init__ (self, x,y):
                self.color = ROUGE
                self.radius= 30
                self.x = 100
                self.y = 100
    def dessiner(self, ecran):
        pygame.draw.circle(ecran,self.color,[self.x,self.y],self.radius)
corps = []
corps.append (segment(0,0))
corps.append (segment(10,10))

    
    
    
    
    
    

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sens = 1
            if event.key == pygame.K_RIGHT:
                    sens = 2            
            if event.key == pygame.K_DOWN:
                    sens = 3    
            if event.key == pygame.K_UP:
                    sens = 4    
    if sens == 2:
            posx = posx +5
    if sens == 1:
                posx = posx -5    
    if sens == 3:
                posy = posy +5            
    if sens == 4:
                posy = posy -5
    if sens == 1:
        corps[0].x= posx+60
        corps[0].y= posy 
    if sens == 2:
        corps[0].x= posx-60
        corps[0].y= posy
    if sens == 3:
        corps[0].x= posx
        corps[0].y= posy-60        
    if sens == 4:
        corps[0].x= posx
        corps[0].y= posy+60        
    # TICK
    
    ecran.fill(BLANC)
    
    # DESSIN
    
    
    pygame.draw.circle(ecran, BLEU, [posx,posy], 30)
    for seg in corps:
            seg.dessiner(ecran)    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()