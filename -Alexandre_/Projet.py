#!coding:utf-8
from __future__ import print_function, division
import random
import pygame
pygame.init()

def print(*a, **b):
    import sys
    import builtins
    builtins.print(*a, **b)
    sys.stdout.flush()

taille = [800, 600]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
couleur = [BLEU,VERT,ROUGE,ROUGE,VERT,BLANC]

# DÉBUT
clock = pygame.time.Clock()
le_serpent = pygame.image.load('le serpent.png').convert_alpha() # Téléchargez l'image ici
t = 0    
step = 20
fini = 0
gauche = False
droite = False
haut = False
bas = False
class boule:
    pass
tete = boule()
tete.x = 340
tete.y = 240
queue = boule()
queue.x = 320
queue.y = 240
membre = [tete,queue]
Nbsegments = 6
piece = boule()
piece.y = random.randint(0,30)*20
piece.x = random.randint(0,40)*20
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
    if gauche == True:  # if gauche: marche aussi
        ajout = boule()
        ajout.x = membre[0].x - step
        ajout.y = membre[0].y
        membre.insert(0,ajout)
    elif droite == True:
        ajout = boule()
        ajout.x = membre[0].x + step
        ajout.y = membre[0].y
        membre.insert(0,ajout)             
    elif haut == True:
        ajout = boule()
        ajout.x = membre[0].x 
        ajout.y = membre[0].y - step
        membre.insert(0,ajout)             
    elif bas == True:
        ajout = boule()
        ajout.x = membre[0].x 
        ajout.y = membre[0].y + step
        membre.insert(0,ajout) 
    if len(membre) > Nbsegments:    
        membre.pop()
    if membre[0].x == piece.x and membre[0].y == piece.y:
        piece.x = random.randint(0,40)*20
        piece.y = random.randint(0,30)*20
        Nbsegments += 1
    # print("blabla")
    print(len(membre), membre[0].x, membre[0].y, membre[1].x, membre[1].y)
    t = 1
    d = False
    while t < len(membre): 
        if membre[0].x == membre[t].x:
            if membre[0].y == membre[t].y:
                d = True
        t += 1
        
    # TICK

    # DESSIN
    ecran.fill(NOIR)
    if d == True:
        print("Vous êtes mort")
        fini = 1
    else:
        i = 0
        while i < len(membre):
            if i == 0:
                ecran.blit(le_serpent, [membre[0].x-10, membre[0].y-10])
                # pygame.draw.circle(ecran, ROUGE, [membre[i].x, membre[i].y], 15)
            else:    
                pygame.draw.circle(ecran, couleur[i%len(couleur)], [membre[i].x, membre[i].y], 15)
            i += 1
        pygame.draw.circle(ecran, ROUGE, [piece.x , piece.y], 5)
    pygame.display.flip()
    clock.tick(5)

print("score:",len(membre)-2)

pygame.quit()