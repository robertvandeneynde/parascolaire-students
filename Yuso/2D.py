from __future__ import print_function, division

import pygame
pygame.init()

def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
BLEUC = [128, 191, 255]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
VIOLET = [128,0,255]
# DÉBUT
pos = 100

posb = 100


clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    pos = pos + 1
    print(pos)
    
    posb = pos + 2
    
    if pos > 700:
        pos=0
    if posb > 700:
        posb= 0
    

    # DESSIN
    ecran.fill(NOIR)
    
    pygame.draw.rect(ecran, BLEUC, [350,0, 80,40])
    pygame.draw.circle(ecran, BLEU, [500,posb], 20)
    pygame.draw.circle(ecran, VERT, [pos, 250], 50)
    
    pygame.display.flip()

    clock.tick(60)
    
pygame.quit() 