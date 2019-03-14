from __future__ import print_function, division

def print(*args, **kwargs):
    import builtins
    import sys
    builtins.print(*args, **kwargs)
    sys.stdout.flush()    

def xy_to_i(x, y):
    return x + y * 10

import pygame, random
random.seed()

pygame.init()

taille_fenetre = [500, 550]
taille = [500, 500]
ecran = pygame.display.set_mode(taille_fenetre)
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
font = pygame.font.SysFont('Calibri', 25)

class Boule:
    pass

# def generate_boule():

la_liste_de_boules = []    
x = 20
y = 20

while y < taille[1]:
    b = Boule()
    b.x = x
    b.y = y
    b.bombe = 0
    b.rayon = 15
    b.numero = 0
    la_liste_de_boules.append(b)
    
    if x + 50 < taille[0]:
        x = x + 50
    else:
        x = 20
        y = y + 50    

v = 0
while v < nbmaxbombe:
    nbaleatoire = random.randrange(0, len(la_liste_de_boules))
    la_liste_de_boules[nbaleatoire].bombe = 1
    v = v + 1

# pour chaque bombe:
  # pour chaque boule voisine:
    # faire +1 au numero
i = 0
while i < len(la_liste_de_boules):
    if la_liste_de_boules[i].bombe == 1:
        print("j'ai trouvé une bombe")
    
    i = i + 1
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
            # event.pos est une liste de taille 2
            # le premier element (event.pos[0]) est la position en x DU CLIC
            # le deuxieme element (event.pos[1]) est la position en y DU CLIC
            souris_x = event.pos[0]
            souris_y = event.pos[1]
            j = 0
            while j < len(la_liste_de_boules):
                # si le clic de souris touche la boule j
                if abs(souris_x - la_liste_de_boules[j].x) < la_liste_de_boules[j].rayon and abs(souris_y - la_liste_de_boules[j].y) < la_liste_de_boules[j].rayon:
                    if la_liste_de_boules[j].bombe == 0:  # si la boule j n'est pas une bombe
                        score += 1
                        la_liste_de_boules.pop(j)
                    else: 
                        # c'est une bombe  
                        print("GAME OVER")
                        la_liste_de_boules.clear()
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
            pygame.draw.circle(ecran, BLEU, [la_liste_de_boules[i].x, la_liste_de_boules[i].y],  la_liste_de_boules[i].rayon)
        else:
            pygame.draw.circle(ecran, ROUGE, [la_liste_de_boules[i].x, la_liste_de_boules[i].y],  la_liste_de_boules[i].rayon)
        n = la_liste_de_boules[i].numero
        r = la_liste_de_boules[i].rayon
        image_numero = font.render(str(n), True, BLANC)
        ecran.blit(image_numero, [la_liste_de_boules[i].x - r/2, la_liste_de_boules[i].y - r/2])
                
        i = i + 1
    # print(score)
    image_score = font.render("Score: " + str(score), True, BLANC)
    ecran.blit(image_score, [20,500])
    
    

    # 20, 20 + 0 // p  = 0
    # 20, 20 + 40 // p  = 1
    # x, 20 + 80 // p  = 2
    # x, 20 + 120 // p  = 3
    # x,  20 + 160 // p  = 4
    
  

    pygame.display.flip()

    clock.tick(100)

pygame.quit()