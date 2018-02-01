import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255] 
TAEMIN =  1 
# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    print(TAEMIN)
    TAEMIN = TAEMIN + 1 
    if TAEMIN == 150:
        TAEMIN == 0 
        


    # DESSIN
    ecran.fill(BLEU)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLANC, [255, 0], 0 )
    pygame.draw.circle(ecran, VERT, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(10)
    
pygame.quit()
