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

class Perso:
    pass

chicken = Perso()
chicken.x = 450
chicken.y = 250

x = 450
y = 250
z = 0

dead = 0

decor = pygame.image.load('deco.jpg').convert_alpha()
game_over = pygame.image.load('game over.png').convert_alpha()
image_perso = pygame.image.load('Angry Chicken.png').convert_alpha()

image_perso = pygame.transform.rotozoom(image_perso, 0, 1/5)

print(image_perso.get_width(), image_perso.get_height())

import sys
sys.stdout.flush()

class Glace:
    pass

glace1 = Glace()
glace1.x = random.randrange(601)
glace1.w = 100
glace1.h = 40


glace2 = Glace()
glace2.x = random.randrange(601)
glace2.w = 80
glace2.h = 40

glace3 = Glace()
glace3.x = random.randrange(601)
glace3.w = 60
glace3.h = 40

glaces = [glace1, glace2, glace3]

glaceg = Glace()
glaceg.x = random.randrange(601)
glaceg.w = 60
glaceg.h = 40

glaces.append(glaceg)

glaceg = Glace()
glaceg.x = random.randrange(601)
glaceg.w = 60
glaceg.h = 40

glaces.append(glaceg)


clock = pygame.time.Clock()

fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
    z = z + 2
    #mouvement
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
        r = 0
        while r < len(glaces):
            glaces[r].x = random.randrange(601)
            r = r + 1
            
            
        #glace1.x = random.randrange(601)
        #glace2.x = random.randrange(601)
        #glace3.x = random.randrange(601)

    # TICK
    i = 0
    while i < len(glaces):
        if glaces[i].x <= x <= glaces[i].x + glaces[i].w and z <= y <= glaces[i].h + z:
            dead = 1
        i = i + 1
    

    # DESSIN
    ecran.fill(BLANC)
    
    ecran.blit (decor, [0, 0])
    
    pygame.draw.circle(ecran, BLEU, [x, y ], 5)
    ecran.blit(image_perso, [x - image_perso.get_width()/2, y-image_perso.get_height()/2])    
    
    i = 0
    while i < len(glaces):
        pygame.draw.rect(ecran, BLEU, [glaces[i].x, z, glaces[i].w, glaces[i].h], 1)
        i = i + 1
    
    # for g in glaces:
    #   pygame.draw.rect(ecran, BLEU, [g.x, z, g.w, g.h], 1)
    
    if dead == 1:
        ecran.blit (game_over, [0, 0])
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()