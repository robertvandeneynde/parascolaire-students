from __future__ import print_function, division
import pygame
pygame.init()

taille = [1200, 400]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
x=0
y=0
# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    y=y+1
    a=a+2
    b=b+3
    c=c+4
    e=e+5
    d=d+6
    x=x+7
    
    if a>400:
        a=0
    if b>1200:
        b=0
    if c>400:
        c=0
    if e>1200:
        e=0
    if d>1200:
        d=0
    if y>400:
        y=0
    if x>1200:
        x=0
    # DESSIN
    ecran.fill(NOIR)
    
    pygame.draw.rect(ecran, ROUGE, [b,c, 20,40])
    pygame.draw.circle(ecran, BLEU, [e,y], 20)
    pygame.draw.circle(ecran, VERT, [d,a], x)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()