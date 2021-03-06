from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

ma_position = 10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    pressed = pygame.key.get_pressed() # liste contenant l'�tat des touches du clavier
    
    # � chaque tick...
    # si Gauche est enfonc�e
    if pressed[276]: # 276: touche gauche (voir le fichier pygame5 pour conna�tre les num�ros de toutes les touches)
        ma_position = ma_position - 5
    
    if pressed[275]: # 275: touche droite
        ma_position = ma_position + 5
    
    buttons = pygame.mouse.get_pressed() # liste contenant l'�tat des touches de la souris : gauche/milieu/droit
    
    if buttons[0]: # si le bouton de gauche de la souris est enfonc�
        position_souris = pygame.mouse.get_pos() # liste de taille 2 avec x,y
        ma_position = position_souris[0]
    
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [ma_position, 20, 100, 200])
    
    pygame.display.flip()
    
    clock.tick(60)
import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

ma_position = 10

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        
        # elif est un raccourci pour "if... else... if ... else..."
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276: # touche gauche
                ma_position = ma_position - 100
            elif event.key == 275: # touche droite
                ma_position = ma_position + 100
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos est une liste de taille 2 contenant le x et le y
            print("Clic en", event.pos[0], event.pos[1])
            ma_position = event.pos[0]
    
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [ma_position, 20, 100, 200])
    
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()