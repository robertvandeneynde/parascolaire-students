# mes couleurs : [Rouge, Vert, Bleu] (voir Paint)
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
sens = 1
ma_position = 100
# 3) faire une clock qui va g�rer les fps
clock = pygame.time.Clock()

# 4) boucle principale
fini = 0
while fini == 0:
    
    # 5) �V�NEMENTS : rajoutez des "elif" en dessous du "if" pour de nouveaux �v�nements (pygame5_clavier_souris_events.py)
    for event in pygame.event.get(): # pour chaque �v�nement qui s'est pass� depuis la derni�re fois
        if event.type == pygame.QUIT: # si on a cliqu� sur la croix...
            fini = 1 # la boucle principale va s'arr�ter
    
    # 6) TICK : Faire quelque chose � chaque tick (60 fois par seconde)
    if sens == sens +1:
        ma_position == ma_position +1
    if sens == sens -1
    ma_position == ma_position -1
    # � compl�ter !
    
    # 7) DESSIN
    
    ecran.fill(BLANC) # on remplit l'�cran de BLANC
    
    # dessiner les objets, sinon, on ne verra rien
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40]) # coin en haut � gauche : x=100 y=200, taille 20x40
    pygame.draw.circle(ecran, BLEU, [100,200], 20) # centre : x=100 y=200, rayon=20
    pygame.draw.circle(ecran, VERT, [150, 80], 10) # un cercle vert
    
    # 8) mettre � jour les dessins
    pygame.display.flip()
    
    # 9) attendre la clock avec les bons fps !
    clock.tick(60) # 60 images par secondes (frame per second / fps)
    
# 10) quitter... �a peut servir
pygame.quit()