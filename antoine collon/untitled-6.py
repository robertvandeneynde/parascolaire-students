import pygame

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

rouge = [255,0,0]
blanc = [255,255,255]

ma_position = 10
ta_position = 50

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    pressed = pygame.key.get_pressed() # liste contenant l'état des touches du clavier
    
    # à chaque tick...
    # si Gauche est enfoncée
    if pressed[276]: # 276: touche gauche (voir le fichier pygame5 pour connaître les numéros de toutes les touches)
        ma_position = ma_position - 5
    
    if pressed[275]: # 275: touche droite
        ma_position = ma_position + 5
    
    if pressed[274]:
        ta_position = ta_position + 5
        
    if pressed[273]:
        ta_position = ta_position - 5
    
    buttons = pygame.mouse.get_pressed() # liste contenant l'état des touches de la souris : gauche/milieu/droit
    
    if buttons[0]: # si le bouton de gauche de la souris est enfoncé
        position_souris = pygame.mouse.get_pos() # liste de taille 2 avec x,y
        ma_position = position_souris[0]
    
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [ma_position, ta_position, 20, 50])
    pygame.draw.rect(ecran, BLEU, [ma_position,ta_position, 50, 20])
    pygame.draw.circle(ecran, VERT, [150, 80], 10) 
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
