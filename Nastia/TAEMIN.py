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
TAEMIN =  0
SUHO = 0 

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    TAEMIN = TAEMIN + 5
    if TAEMIN >= 300:
        TAEMIN = 0
        
    SUHO = SUHO + 0
    if SUHO >= 500: 
        SUHO = 0 

    # DESSIN
    ecran.fill(BLEU)
    
    pygame.draw.rect(ecran, ROUGE, [100,SUHO, 20,40])
    pygame.draw.circle(ecran, [100, 150 ,0], [200, 70], 20 )
    pygame.draw.circle(ecran, [0,255,0], [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(1)
    
pygame.quit()
