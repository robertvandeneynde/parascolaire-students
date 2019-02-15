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

fini = 0
gauche = false
droite = false
haut = false
bas = false
class boule:
    pass
tete = boule()
tete.x = 350
tete.y = 250
queue = boule()
queue.x = 340
queue.y = 250
membre = [tete,queue]
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        
        # elif est un raccourci pour "if... else... if ... else..."
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276: # touche gauche
                gauche = true
            elif event.key == 275: # touche droite
                droite = true
            elif event.key == 273: # touche haut
                haut = true
            elif event.key == 274: # touche bas
                bas = true
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos est une liste de taille 2 contenant le x et le y
            # print("Clic en", event.pos[0], event.pos[1])
            # ma_position = event.pos[0]
        elif gauche == true:
            ajout = boule()
            ajout.x = tete.x + 10
            ajout.y = tete.y
            membre.insert(0,tete)
    # TICK

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.circle(ecran, VERT, [membre[0].x, membre[0].y], 15)
    pygame.draw.circle(ecran, VERT, [membre[1].x, membre[1].y], 15)
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()