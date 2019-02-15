from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

noir = [0, 0, 0]
blanc = [255, 255, 255]
rouge = [255, 0, 0]
vert = [0, 255, 0]
bleu = [0, 0, 255]

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1  
            
    if pressed[276]: 
        x= x - 5
    if pressed[275]: 
        x = x + 5
    if pressed[274]:
        y=y+5        
    if pressed[273]:
        y=y-5 
        
    if x>=700:
        x=-20 
    elif x<=-20:
        x=700  
        
    if y>=500:
        y=-20
    elif y<=-20:
        y=500
    
    print (a,b,x,y)
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [x, y, a, b])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()