#!coding: utf-8
'''
Ceci est le code pygame de base pour afficher une fenêtre.
De courts commentaires sont écrits pour pouvoir vous lancer rapidement dans un projet.
Si vous voulez des explications progressives et plus détaillées lisez :
pygame1_dessin.py, pygame2_tick.py, pygame3_events.py et pygame4_animations.py

Les parties du code utiles à modifier sont les 4 parties INITIALISATION, ÉVÉNEMENTS, UPDATE, DESSIN
'''

# 0) importer pygame, et l'initialiser
import pygame
pygame.init()

from math import sqrt

# 1) créer un écran : 700x500 pixels pour nous !
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

# 2) INITIALISATION : création des valeurs initiales des variables
ma_position = 300
elias = 200
yo = 350
naruto = 350
e = 0
m = 400

bla = pygame.image.load('vaisseau.png').convert_alpha()
bla = pygame.transform.rotozoom(bla, 0, 1)

# ajoute ici tes variables
# mes couleurs : [Rouge, Vert, Bleu] (voir Paint)
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [135, 233, 144]
BLEU = [0, 0, 255]

# 3) faire une clock qui va gérer les fps
clock = pygame.time.Clock()

# 4) boucle principale
fini = 0
while fini == 0:
    
    # 5) ÉVÉNEMENTS : rajoutez des "elif" en dessous du "if" pour de nouveaux événements (pygame5_clavier_souris_events.py)
    for event in pygame.event.get(): # pour chaque événement qui s'est passé depuis la dernière fois
        if event.type == pygame.QUIT: # si on a cliqué sur la croix...
            fini = 1 # la boucle principale va s'arrêter
        elif event.type == pygame.KEYDOWN:
            print( "La touche numero", event.key)
            if event.key == 276:  # touche gauche
                ma_position = ma_position - 100
            elif event.key == 275:  # touche gauche
                ma_position = ma_position + 100

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Clic en", event.pos[0], event.pos[1])
                ma_position = event.pos[0]


    # 6) UPDATE : Faire quelque chose à chaque tick (60 fois par seconde)
    pressed = pygame.key.get_pressed()
    if pressed [275] :
        bla = bla +3
    if pressed [276] :
        bla = bla -3
    ma_position = ma_position + 5
    if ma_position >700:
        ma_position = 0

    elias = elias + 5

    if elias >700 :
        elias = 0
    naruto = naruto + 5
    if naruto >700:
        naruto = 0
    if m >499:
        m = 1

    if e == 1:
       m = m - 7

    dx = 350 - naruto
    dy = m- 80
    d = sqrt (dx * dx + dy * dy)
    if d < 30:
        print("boum")
        m = 400

    pressed = pygame.key.get_pressed()

    # 7) DESSIN
    
    ecran.fill(BLANC) # on remplit l'écran de BLANC
    
    # dessiner les objets, sinon, on ne verra rien
    pygame.draw.circle(ecran, VERT, [350, m], 10)
    # pygame.draw.rect(ecran, ROUGE, [350, 400, 40, 70])
    pygame.draw.circle (ecran, ROUGE, [naruto, 80], 20)
    pygame.draw.circle (ecran, BLEU, [ma_position, 80] , 20)
    pygame.draw.circle (ecran, VERT, [elias,80], 20)
    ecran.blit(bla, [250, 350])

    # 8) mettre à jour les dessins
    pygame.display.flip()
    
    # 9) attendre la clock avec les bons fps !
    clock.tick(60) # 60 images par secondes (frame per second / fps)
    
# 10) quitter... ça peut servir
pygame.quit()
