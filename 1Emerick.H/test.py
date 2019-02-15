
from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

a=b=c=d=e= 10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    pressed = pygame.key.get_pressed() 
    
   
    if pressed[276]: 
        a =a-5
    if pressed[275]:
        a= a+5
    if a>= 0:
        a=715
    elif a<=700:
        a=-15
  

    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [a, 20, 100, 200])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()