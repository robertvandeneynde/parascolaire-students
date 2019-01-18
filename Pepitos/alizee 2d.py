import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT
a=100
clock = pygame.time.Clock()
b=100
c=100
fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    a=a+2
    b=b+3
    c=c+1
    if a > 250:
        a=-2
    if b > 250:
        b=-3
    if c > 665:
        c=c+2
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, BLEU, [c,200,30,15])
    pygame.draw.circle(ecran, BLEU, [100,b], 15)
    pygame.draw.circle(ecran, BLEU, [80,a], 40)
    
    pygame.display.flip()
    
    clock.tick(80)
    
pygame.quit()
sens=6
