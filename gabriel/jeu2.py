import pygame

pygame.init()


#variables
taille = [500, 500]
fini = 0
ecran = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
#fin des variables




#début



while fini == 0:
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            fini = 1
    
    
    
    
    
    
    
    ecran.fill(255, 255, 255)
    pygame.display.flip()
    clock.tick(60)
    
    
    
    pygame.quit()
#Le jeu est fini
