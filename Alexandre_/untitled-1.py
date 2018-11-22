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

# DÉBUT

clock = pygame.time.Clock()
image_perso = pygame.image.load('SOV.png').convert_alpha()
image_perso2 = pygame.image.load('AEB.png').convert_alpha()
maposition = 10
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276: # touche gauch
                maposition = maposition - 100
            elif event.key == 275: # touche droite
                maposition = maposition + 100
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # event.pos est une liste de taille 2 contenant le x et le y
                print("Clic en", event.pos[0], event.pos[1])
                maposition = event.pos[0]         
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20)
    pygame.draw.circle(ecran, VERT, [150, 80], 10)
    ecran.blit(image_perso, [maposition, 200])
    ecran.blit(image_perso2, [10,300])
    pygame.display.flip()
    image_perso_petite = pygame.transform.smoothscale(image_perso, [400,600])    
    print("Taille :", image_perso.get_width(), image_perso.get_height())
    clock.tick(60)
    
pygame.quit()