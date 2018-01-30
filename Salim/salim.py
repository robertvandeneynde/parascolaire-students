from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

ma_position = 100
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
ROSE= pygame.Color("#ff9900") 

# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
    
    # TICK
    ma_position = ma_position  + 1

    # DESSIN
    
    ecran.fill(VERT)
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,ma_position], 20)
    pygame.draw.circle (ecran, ROSE, [200, 100], 50 ) 
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()