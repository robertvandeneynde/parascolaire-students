import pygame,random
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT

clock = pygame.time.Clock()

fini = 0
vertx=150
bleux=100
bleuy=200
while fini == 0:
    bleux=bleux+3
    bleuy=bleuy+3
    if bleux >= 700  or bleuy >=500:
        bleux=random.randint(0,700)
        bleuy=random.randint(0,500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276:
                vertx = vertx - 10
            elif event.key == 275:
                vertx = vertx + 10        
    # TICK
    

    # DESSIN
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, ROUGE, [100,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [bleux,bleuy], 20)
    pygame.draw.circle(ecran, VERT, [vertx, 80], 10)
    

    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()