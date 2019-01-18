from __future__ import print_function, division

import pygame

pygame.init()

taille = [1200, 900]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

x=y=a=b= 10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    pressed = pygame.key.get_pressed() # liste contenant l'état des touches du clavier
    
    # à chaque tick...
    # si Gauche est enfoncée
    if pressed[276]: # 276: touche gauche (voir le fichier pygame5 pour connaître les numéros de toutes les touches)
        x= x - 5
    
    if pressed[275]: # 275: touche droite
        x = x + 5
    
    if pressed[274]:
        y=y+5
    if pressed[273]:
        y=y-5
        
    if x>=1200:
        x=-20     
    if y>=900:
        y=-20  
        
   
        
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [x, y, a, b])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()