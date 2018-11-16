# 0) importer pygame, et l'initialiser
import pygame
pygame.init()

taille = [500, 500]
ecran = pygame.display.set_mode(taille)

# INITIALISATION : création des valeurs initiales des variables 

# ajoute ici tes variables !
a=5
sens=1

# mes couleurs : [rouge, vert, Bleu] (voir Paint)
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

clock = pygame.time.Clock()

# 4) boucle principale
fini = 0
while fini == 0:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            fini = 1 
    
    # TICK : Faire quelque chose à chaque tick (60 fois par seconde)
   if sens == 1: 
       a=a+6
    else:
        a=a-6
    
    # à compléter !
    
    
    # 7) DESSIN
    ecran.fill(BLANC)
    
    # dessiner les objets, sinon, on ne verra rien
    pygame.draw.rect(ecran, ROUGE, [a +100,200, 20,40]) # coin en haut à gauche : x=100 y=200, taille 20x40
    pygame.draw.circle(ecran, BLEU, [a +10,200], 20) # centre : x=100 y=200, rayon=20
    pygame.draw.circle(ecran, VERT, [a, a], 10) # un cercle vert
    
    
    # 8) mettre à jour les dessins
    pygame.display.flip()
    
    # 9) attendre la clock avec les bons fps !
    clock.tick(60) # 60 images par secondes (frame per second / fps)
    
# 10) quitter... ça peut servir
pygame.quit()