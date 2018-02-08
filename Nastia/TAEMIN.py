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
EXO = 2
# DÉBUT

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    TAEMIN = TAEMIN + 5
    if TAEMIN >= 255 :
        TAEMIN = 0 
     
    EXO = EXO + 10
    if EXO >= 255 :
        EXO = 0
    
    couleur_variable = [TAEMIN,500 ,0 ]
    couleur_variable_2 = [ 100,EXO ,0] 
    # DESSIN
    ecran.fill(BLEU)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, couleur_variable_2, [200, 70], 20 )
    pygame.draw.circle(ecran, couleur_variable, [150, 80], 10)
    
    pygame.display.flip()
    
    clock.tick(10)
    
pygame.quit()
