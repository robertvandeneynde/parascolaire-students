from __future__ import print_function, division

import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

noir = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# état des joueurs
etatRobin = 1
etatGuilhaime = 1
etatMatteo = 1
# état des munitions
munitionsMax = 6
munition = munitionsMax
# DÉBUT
clock = pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 25)

fini = 0
while fini == 0:
    #event
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.pos est une liste de taille 2 contenant le x et le y
            #print("Clic en", event.pos[0], event.pos[1])
            x = event.pos[0]
            y = event.pos[1]
            if munition>0 :
                if 200 <= x <= 300: # le clic touche robin
                    if 200 <= y <= 300 :
                        #print("robin disparait")
                        etatRobin = 0
                if 450 <= x <= 550 :
                    if 300<=y<=400 :
                        etatGuilhaime=0
                if 200<=x<=300 :
                    if 300<=y<=400 :
                        etatMatteo=0
                munition = munition-1       
        elif event.type == pygame.KEYDOWN :
            if event.key== pygame.K_SPACE :
                munition = munitionsMax
            
              
    position_souris = pygame.mouse.get_pos() # liste de taille 2 avec x,y 
    
    # TICK
    x = position_souris[0]
    y = position_souris[1]
    
    # DESSIN
    image_nom_joueur = font.render("Robin", True, noir)
    image_nom_joueurr = font.render("Mattéo", True, noir)
    image_nom_joueurrr = font.render("Guilhaime", True, noir)
    image_munitions = font.render(str(munition), True, noir)
    ecran.fill(BLANC)
    
    # si le carré est rouge le personnage est vivant sinon il est mort
    if etatRobin == 1 :
        pygame.draw.rect(ecran, ROUGE, [200,200, 50,50]) #robin
    else : 
        pygame.draw.rect(ecran, noir, [200,200, 50,50]) #robin mort
    if etatGuilhaime == 1 :
        pygame.draw.rect(ecran, ROUGE, [450,350, 50,50]) #guilhaime
    else :
        pygame.draw.rect(ecran, noir, [450,350, 50,50]) #guilhaime mort
    if etatMatteo ==1 :
        pygame.draw.rect(ecran, ROUGE, [200,300, 50,50]) #matteo
    else :
        pygame.draw.rect(ecran, noir, [200,300, 50,50]) #matteo mort
    pygame.draw.rect(ecran, ROUGE, [x-50,y-5, 20,10])
    pygame.draw.circle(ecran, BLEU, [x,y],10)
    pygame.draw.rect(ecran, ROUGE, [x+30,y-5, 20,10])
    pygame.draw.rect(ecran, ROUGE, [x-3,y-50, 10,20])
    pygame.draw.rect(ecran, ROUGE, [x-3,y+25, 10,20])
    ecran.blit(image_nom_joueur, [200,180])
    ecran.blit(image_nom_joueurr, [190,280])
    ecran.blit(image_nom_joueurrr, [425,330])
    ecran.blit(image_nom_joueurrr, [425,330])
    ecran.blit(image_munitions, [10,450])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()