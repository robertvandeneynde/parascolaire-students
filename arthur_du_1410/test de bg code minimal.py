#!coding: utf-8
from __future__ import print_function, division
"""
Ceci est le code pygame de base pour afficher une fenêtre.
De courts commentaires sont écrits pour pouvoir vous lancer rapidement dans un projet.
Si vous voulez des explications progressives et plus détaillées lisez :
[pygame1_dessin.py](), [pygame2_tick.py](), [pygame3_events.py]() et [pygame4_animations.py]()

Les parties du code utiles à modifier sont les 4 parties suivantes :
INITIALISATION, ÉVÉNEMENTS, UPDATE, DESSIN
"""

# 0) importer pygame, et l'initialiser
import pygame
pygame.init()

# 1) créer un écran : je choisis 700x500 pixels
taille = [700, 500]
ecran = pygame.display.set_mode(taille)

# 2) INITIALISATION : création des valeurs initiales des variables 

# ajoute ici tes variables !
ma_position = 100
sens = + 1
# mes couleurs : [Rouge, Vert, Bleu] (voir Paint)
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
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
    
    # 6) UPDATE : Faire quelque chose à chaque tick (60 fois par seconde)
    if sens == + 1:
            ma_position = ma_position + 1
    if sens == - 1:
        ma_position = ma_position - 1
    if ma_position > 700:
        sens = -1
    if ma_position < 0 :
        sens = + 1
    # à compléter !
    # 7) DESSIN
    
    ecran.fill(BLANC) # on remplit l'écran de BLANC
    
    # dessiner les objets, sinon, on ne verra rien
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40]) # coin en haut à gauche : x=100 y=200, taille 20x40
    pygame.draw.circle(ecran, BLEU, [100,200], 20) # centre : x=100 y=200, rayon=20
    pygame.draw.circle(ecran, VERT, [ma_position, 80], 10) # un cercle vert
    pygame.draw.polygon(ecran, ROUGE, [[0,50], [100,0], [100,100]])
    # 8) mettre à jour les dessins
    pygame.display.flip()
    
    # 9) attendre la clock avec les bons fps !
    clock.tick(150) # 60 images par secondes (frame per second / fps)
    
# 10) quitter... ça peut servir
pygame.quit()