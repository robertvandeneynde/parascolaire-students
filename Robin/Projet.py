

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)
a=50
xb=10
yb=250
sens=1
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    pressed = pygame.key.get_pressed() 
    # TICK
    if sens==1:
        a=a+5
    else:
        a=a-5
    if a>=690:
        sens=-1
    if a<=0:
        sens=1
   
    if pressed[276]: #touche fleche gauche
        xb=xb-5
    if pressed[275]: #touche fleche droite
        xb=xb+5
    if pressed[274]:
        yb=yb+5
    if pressed[273]:
        yb=yb-5
    if xb>=690:
        xb=xb-5
    if xb<=10:
        xb=xb+5 
    if yb<=10:
        yb=yb+5
    if yb>=490:
        yb=yb-5
    if xb+10>100:
        if xb<150:
            if yb+10>200:
                if yb-10<240:
                    print("contact")
        
    print(xb)
    # DESSIN
    ecran.fill(BLANC)
    pygame.draw.rect(ecran, ROUGE, [100,200,50,40])
    pygame.draw.circle(ecran, BLEU, [a,200], 20)
    pygame.draw.circle(ecran, VERT, [xb,yb], 10)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
