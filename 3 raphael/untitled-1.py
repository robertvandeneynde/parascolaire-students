from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

x= 10
y=10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key) 
    
    pressed = pygame.key.get_pressed() # liste contenant l'état des touches du clavier
    
    # à chaque tick...
    # si Gauche est enfoncée
    if pressed[276]: # 276: touche gauche (voir le fichier pygame5 pour connaître les numéros de toutes les touches)
        x= x - 5
    
    if pressed[275]: # 275: touche droite
        x = x + 5
    
    if pressed[274]:
        y=y+5
        
            
    

    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [x, y, 100, 200])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()