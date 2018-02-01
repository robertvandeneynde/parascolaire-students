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
z = 30
x_rouge = 250
clock = pygame.time.Clock()

fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
    z = z + 2 
    pressed = pygame.key.get_pressed()
    if pressed[276]:
        x = x - 5
    if pressed[274]:
        y = y + 5 
    if pressed[275]:
        x = x + 5
    if pressed[273]:
        y = y - 5
    if x > 650 :
        x = 650
    if x < 50:
        x = 50
    if y > 500:
        y = 450
    if z >= 510:
        z = 0
        x_rouge = 100
        
    # TICK.
    

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.circle(ecran, BLEU, [x, y + 150 ], 50)
    pygame.draw.rect(ecran, ROUGE, [x_rouge,z, 100,40])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
