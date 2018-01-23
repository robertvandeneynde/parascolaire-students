# 0) importer pygame, fatalement
import pygame

# 1) initialiser pygame
pygame.init()

# d??finir des couleurs : [Rouge, Vert, Bleu] (voir paint)
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

class Personnage:
    pass
Lucien = Personnage ()
ma_position = 100
sens = 1
print (Lucien)
taille = [700, 500]
ecran = pygame.display.set_mode(taille)


# 3) faire une clock qui va g??rer les fps
clock = pygame.time.Clock()



# 4) boucle principale
fini = 0
while fini == 0:



    # 5) lire les ??v??nements qui se sont pass??s depuis la derni??re fois
    for event in pygame.event.get():
        # si on a cliqu?? sur la croix...
        if event.type == pygame.QUIT:
            fini = 1 # la boucle principale va s'arr??ter



    # 6) UPDATE : Faire quelque chose ?? chaque instant/image
    if sens == 1 :
        ma_position = ma_position + 1
    else :
        ma_position = ma_position -1

    if ma_position >=700 :
        sens = -1
    if ma_position <= 0 :
        sens = 1



        pygame.draw.rect(ecran , ROUGE, [200,10,100,200])

     # 7) DESSIN : on remplit l'??cran de BLANC
    ecran.fill(BLANC)

    # 8) on dessine quelque chose, sinon, on ne verra rien

    pygame.draw.circle(ecran, BLEU, [100,200], 20) # centre : x=100 y=200, rayon=20
    pygame.draw.circle(ecran, VERT, [ma_position, 20], 10) # un cercle vert qui bouge
    pygame.draw.rect(ecran , NOIR, [200,10,100,200], 30)




    # 9) mettre ?? jour
    pygame.display.flip()



    # 10) attendre la clock avec les bons fps !
    clock.tick(200) # 60 images par secondes (frame per second / fps)



# 11) quitter... ??a peut servir
pygame.quit()
