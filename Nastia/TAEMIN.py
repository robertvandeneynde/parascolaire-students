import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255] 

# D�BUT
TAEMIN =  0
SUHO = 0 
TEN = 0
TEN_HAUTEUR = 200

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK
    TAEMIN = TAEMIN + 5
    if TAEMIN >= 700:
        TAEMIN = 0
        
    SUHO = SUHO + 5
    if SUHO >= 500: 
        SUHO = 0 
        
    TEN = TEN + 5
    if TEN >= 700:
        TEN = 0 
    
    TEN_HAUTEUR += 5
    if TEN_HAUTEUR >= 500:
        TEN_HAUTEUR = 0

    # DESSIN
    ecran.fill(BLEU)
    
    pygame.draw.rect(ecran, ROUGE, [100,SUHO, 20,40])
    pygame.draw.circle(ecran, [100, 150, 0], [TAEMIN, 70], 20 )
    pygame.draw.rect(ecran, ROUGE, [TEN,TEN_HAUTEUR, 30,60])
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
