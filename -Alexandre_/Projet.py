from __future__ import print_function, division
import random
import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
couleur[BLEU,VERT,ROUGE,ROUGE,VERT,BLANC]
# DÉBUT

clock = pygame.time.Clock()

fini = 0
gauche = False
droite = False
haut = False
bas = False
class boule:
    pass
tete = boule()
tete.x = 350
tete.y = 250
queue = boule()
queue.x = 330
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
                gauche = True
                droite = False
                haut = False
                bas = False
            elif event.key == 275: # touche droite
                gauche = False
                droite = True
                haut = False
                bas = False
            elif event.key == 273: # touche haut
                gauche = False
                droite = False
                haut = True
                bas = False
            elif event.key == 274: # touche bas
                gauche = False
                droite = False
                haut = False
                bas = True
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos est une liste de taille 2 contenant le x et le y
            # print("Clic en", event.pos[0], event.pos[1])
            # ma_position = event.pos[0]
    if gauche == True:
        ajout = boule()
        ajout.x = membre[0].x - 20
        ajout.y = membre[0].y
        membre.insert(0,ajout)
    elif droite == True:
        ajout = boule()
        ajout.x = membre[0].x + 20
        ajout.y = membre[0].y
        membre.insert(0,ajout)             
    elif haut == True:
        ajout = boule()
        ajout.x = membre[0].x 
        ajout.y = membre[0].y - 20
        membre.insert(0,ajout)             
    elif bas == True:
        ajout = boule()
        ajout.x = membre[0].x 
        ajout.y = membre[0].y + 20
        membre.insert(0,ajout) 
    if len(membre) > 6:    
        membre.pop()
    # TICK

    # DESSIN
    ecran.fill(NOIR)
    i = 0
    while i < len(membre):
        pygame.draw.circle(ecran, couleur[i], [membre[i].x, membre[i].y], 15)
        i += 1
    pygame.display.flip()
    clock.tick(5)
    
pygame.quit()