from __future__ import print_function, division

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)
ma_position2 = 100
ma_position = 100
sens = + 1
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

clock = pygame.time.Clock()

class Boule: 
    pass

haut_gauche = Boule()
haut_gauche.x = 20
haut_gauche.y = 20
haut_gauche.bombe = 0

haut_droite = Boule()
haut_droite.x = 20 + 30
haut_droite.y = 20
haut_droite.bombe = 1

bas_gauche = Boule()
bas_gauche.x = 20
bas_gauche.y = 20 + 30
bas_gauche.bombe = 1

bas_droite = Boule()
bas_droite.x = 20 + 30
bas_droite.y = 20 + 30
bas_droite.bombe = 0

fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276:
                ma_position2 = ma_position2 - 100
            elif event.key == 275:  # touche droite
                ma_position2 = ma_position2 + 100
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Clic en", event.pos[0], event.pos[1])
            x,y =  event.pos
            if 10 <= x <= 30:
                if 10 <= y <= 30:
                    print("yep")
            if 55 <= x <= 75:
                if 10 <= y <= 30:
                    print("yep")
    if sens == + 1:
        ma_position = ma_position + 5
    if sens == - 1:
        ma_position = ma_position - 5
    if ma_position > 700:
        sens = -1
    if ma_position < 0:
        sens = + 1
    ecran.fill(NOIR)

    # for p in range (0 , 5):
    #   for k in range(5):

    pygame.draw.circle(ecran, VERT, [haut_gauche.x , haut_gauche.y], 10)
    pygame.draw.circle(ecran, VERT, [haut_droite.x , haut_droite.y], 10)
    pygame.draw.circle(ecran, VERT, [bas_gauche.x , bas_gauche.y], 10)
    pygame.draw.circle(ecran, VERT, [bas_droite.x , bas_droite.y], 10)
        
    # 20, 20 + 0 // p  = 0
    # 20, 20 + 40 // p  = 1
    # x, 20 + 80 // p  = 2
    # x, 20 + 120 // p  = 3
    # x,  20 + 160 // p  = 4


    pygame.display.flip()

    clock.tick(100)

pygame.quit()
