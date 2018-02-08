import pygame
import random
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
x = 450
y = 250
z = 30

class Glace:
    pass


glace1 = Glace()
glace1.x = random.randrange(601)
glace1.w = 100

glace2 = Glace()
glace2.x = random.randrange(601)
glace2.w = 80

glace3 = Glace()
glace3.x = random.randrange(601)
glace3.w = 60

clock = pygame.time.Clock()

fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
    z = z + 2
    #
    pressed = pygame.key.get_pressed()
    if pressed[276]:
        x = x - 3
    if pressed[274]:
        y = y + 3 
    if pressed[275]:
        x = x + 3
    if pressed[273]:
        y = y - 3
        #colision
    if x > 650 :
        x = 650
    if x < 50:
        x = 50
    if y > 450:
        y = 450
    if y < 50:
        y = 50
        
    if z >= 510:  
        z = 0
        glace1.x = random.randrange(601)
        glace2.x = random.randrange(601)
        glace3.x = random.randrange(601)

    # TICK.
    

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.circle(ecran, BLEU, [x, y ], 50)
    pygame.draw.rect(ecran, BLEU,[glace1.x, z, glace1.w,40])
    pygame.draw.rect(ecran, BLEU,[glace2.x, z, glace2.w,40])
    pygame.draw.rect(ecran, BLEU,[glace3.x, z, glace3.w,40])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()