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

#haut_gauche = Boule()
#haut_gauche.x = 20
#haut_gauche.y = 20
#haut_gauche.bombe = 0
#haut_gauche.rayon = 10

#haut_droite = Boule()
#haut_droite.x = 20 + 30
#haut_droite.y = 20
#haut_droite.bombe = 1
#haut_droite.rayon = 10

#bas_gauche = Boule()
#bas_gauche.x = 20
#bas_gauche.y = 20 + 30
#bas_gauche.bombe = 1
#bas_gauche.rayon = 10

#bas_droite = Boule()
#bas_droite.x = 20 + 30
#bas_droite.y = 20 + 30
#bas_droite.bombe = 0
#bas_droite.rayon = 10

#boules = []
#boules.append(haut_gauche)
#boules.append(haut_droite)
#boules.append(bas_gauche)
#boules.append(bas_droite)
## debut boucle
   ## modification x et Y
   ## affichage
x = 0
y = 0
while x <200 or y <200 :
    if x < 200:
     x = x + 50
    else:
      x = 0

      y = y + 50
    b = Boule()
    b.x = x
    b.y = y
    b.bombe = 1
    b.rayon = 10
    boules.append(b)

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

            if haut_gauche.x - haut_gauche.rayon <= x <= haut_gauche.x + haut_gauche.rayon:
                if haut_gauche.y - haut_gauche.rayon <= y <= haut_gauche.y + haut_gauche.rayon:
                    print("yep","0")

            if bas_gauche.x - bas_gauche.rayon <= x <= bas_gauche.x + bas_gauche.rayon:
                if bas_gauche.y - bas_gauche.rayon <= y <= bas_gauche.y + bas_gauche.rayon:
                    print("yep","1")

            if bas_droite.x - bas_droite.rayon <= x <= bas_droite.x + bas_droite.rayon:
                if bas_droite.y - bas_droite.rayon <= y <= bas_droite.y + bas_droite.rayon: 
                    print("yep","2")

            if haut_droite.x - haut_droite.rayon <= x <= haut_droite.x + haut_droite.rayon:
                if haut_droite.y - haut_droite.rayon <= y <= haut_droite.y + haut_droite.rayon:            
                    print("yep","3")
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

    i = 0
    while i < len(boules):
        pygame.draw.circle(ecran, VERT, [boules[i].x, boules[i].y], boules[i].rayon)
        i = i + 1

    # 20, 20 + 0 // p  = 0
    # 20, 20 + 40 // p  = 1
    # x, 20 + 80 // p  = 2
    # x, 20 + 120 // p  = 3
    # x,  20 + 160 // p  = 4


    pygame.display.flip()

    clock.tick(100)

pygame.quit()