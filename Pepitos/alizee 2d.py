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
    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, BLEU, [c,200,20,25])
    pygame.draw.circle(ecran, BLEU, [b,100], 15)
    pygame.draw.circle(ecran, BLEU, [a, 80], 40)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
sens=-3
