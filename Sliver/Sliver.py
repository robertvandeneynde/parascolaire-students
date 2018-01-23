import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

class perso:
    def __init__(self,X, Y, couleur):
        self.X = X
        self.Y = Y
        self.couleur = couleur   
    
    def dessiner(self,ecran):
        pygame.draw.circle(ecran, self.couleur, [self.X, self.Y], 10)
    

# DÉBUT

clock = pygame.time.Clock()

nom_perso = perso(0,0,NOIR)

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
    pressed = pygame.key.get_pressed()


    # TICK
    
    ecran.fill(BLANC)
    
    # DESSIN
    nom_perso.dessiner(ecran)
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()