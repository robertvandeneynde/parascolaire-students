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
TAEMIN =  700
SUHO = 0 
TEN = 0
TEN_HAUTEUR = 200
KAI = 350
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276: # touche gauche
                KAI = KAI - 10
            elif event.key == 275: # touche droite
                KAI = KAI + 10   
    
    
    # TICK
    TAEMIN = TAEMIN - 5
    if TAEMIN >= 700:
        TAEMIN = 0
    if TAEMIN <= 0:
        TAEMIN = 700
        
    SUHO = SUHO - 5
    if SUHO >= 500: 
        SUHO = 0 
    if SUHO <= 0:
        SUHO = 500
        
    TEN = TEN + 5
    if TEN >= 700:
        TEN = 0 
    
    TEN_HAUTEUR += 5
    if TEN_HAUTEUR >= 500:
        TEN_HAUTEUR = 0

    # DESSIN
    ecran.fill(BLEU)
    
    pygame.draw.rect(ecran, ROUGE, [KAI,SUHO, 20,40])
    pygame.draw.circle(ecran, [100, 150, 0], [TAEMIN, 70], 20 )
    pygame.draw.rect(ecran, ROUGE, [TEN,TEN_HAUTEUR, 30,60])
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
