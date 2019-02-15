from __future__ import print_function, division

import pygame,random

pygame.init()

taille = [500, 550]
ecran = pygame.display.set_mode(taille)
ma_position2 = 100
ma_position = 100
sens = + 1
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
BLEUCLAIR = [51,255,153]
VERTCLAIR = [52,254,154]
score = 0
clock = pygame.time.Clock()
nbmaxbombe = 10

class Boule:
    pass
def bombe_generation():
    la_liste_de_boules = []    
    x = 20
    y = 20
    b = Boule()
    b.x = x
    b.y = y
    b.bombe = 0
    b.rayon = 15
    la_liste_de_boules.append(b)
    while y < taille [1]:
        if x < taille[0]:
            x = x + 50
        else:
            x = 20
            y = y + 50
        b = Boule()
        b.x = x
        b.y = y
        b.bombe = 0
        b.rayon = 15
        la_liste_de_boules.append(b)
    return la_liste_de_boules

v = 1
while v < nbmaxbombe:
    nbaleatoire = random.randrange(0, len(la_liste_de_boules))
    la_liste_de_boules[nbaleatoire].bombe = 1
    v = v + 1

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
            j = 0
            while j < len(la_liste_de_boules):
                if abs(event.pos[0]- la_liste_de_boules[j].x)< la_liste_de_boules[j].rayon and abs (event.pos[1]-la_liste_de_boules[j].y) < la_liste_de_boules[j].rayon :
                    if la_liste_de_boules [j].bombe == 0 :
                        score += 1
                        la_liste_de_boules.pop(j)
                j += 1
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
    while i < len(la_liste_de_boules):
        if la_liste_de_boules[i].bombe == 0:
            pygame.draw.circle(ecran, BLEUCLAIR,[la_liste_de_boules[i].x, la_liste_de_boules[i].y],  la_liste_de_boules[i].rayon)
        else:
            pygame.draw.circle(ecran, VERTCLAIR,[la_liste_de_boules[i].x, la_liste_de_boules[i].y],  la_liste_de_boules[i].rayon)
                
        i = i + 1
    print(score)

    # 20, 20 + 0 // p  = 0
    # 20, 20 + 40 // p  = 1
    # x, 20 + 80 // p  = 2
    # x, 20 + 120 // p  = 3
    # x,  20 + 160 // p  = 4
    
  

    pygame.display.flip()

    clock.tick(100)

pygame.quit()