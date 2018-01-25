import pygame
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
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    pressed = pygame.key.get_pressed()
    if pressed[276]:
        x = x - 5
    if pressed[274]:
        y = y + 5 
    if pressed[275]:
        x = x + 5
    if pressed[273]:
        y = y - 5
    
    # TICK
    

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [x,y - 10 , 200, 50])
    pygame.draw.circle(ecran, BLEU, [x,y], 50)
    pygame.draw.circle(ecran, BLEU, [x, y + 5 ], 50)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
