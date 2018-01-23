import pygame
pygame.init()

taille = [800, 500]
ecran = pygame.display.set_mode(taille)


NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
BLEU = [0, 0, 255]
CYAN = [24, 156, 171]

X = 100
Y = 100


clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    ecran.fill(BLANC)
    
    pygame.draw.circle(ecran, CYAN, [X,Y], 50)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()