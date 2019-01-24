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

class Joueur:
    pass

# état des joueurs
robin = Joueur()
robin.etat = 1
robin.x = 200
robin.y = 200

guilhaime = Joueur()
guilhaime.etat = 1
guilhaime.x = 450
guilhaime.y = 350

matteo = Joueur()
matteo.etat = 1
matteo.x = 200
matteo.y = 300

sadek = Joueur()
sadek.etat = 1
sadek.x = 400
sadek.y = 300

liste_ennemis = [robin, guilhaime, matteo, sadek]
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
            if munition > 0:
                if robin.x <= x <= robin.x + 50: # le clic touche robin
                    if robin.y <= y <= robin.y + 50:
                        #print("robin disparait")
                        liste_ennemis[0].etat  = 0
                        
                if 450 <= x <= 500 :
                    if 350 <= y <= 400 :
                        liste_ennemis[1].etat = 0 
                        
                if 200<=x<=250 :
                    if 300<=y<=350 :
                        liste_ennemis[2].etat = 0
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
    image_nom_joueurrr = font.render("Sadek", True, noir)
    
    image_munitions = font.render(str(munition), True, noir)
    ecran.fill(BLANC)
    
    # si le carré est rouge le personnage est vivant sinon il est mort
    i = 0
    while i < len(liste_ennemis):
        if liste_ennemis[i].etat == 1:
            pygame.draw.rect(ecran, ROUGE, [liste_ennemis[i].x, liste_ennemis[i].y, 50,50]) #robin
        else : 
            pygame.draw.rect(ecran, noir, [liste_ennemis[i].x, liste_ennemis[i].y, 50,50]) #robin mort
        i = i+1  
    
    pygame.draw.rect(ecran, ROUGE, [x-50,y-5, 20,10])
    pygame.draw.circle(ecran, BLEU, [x,y],10)
    pygame.draw.rect(ecran, ROUGE, [x+30,y-5, 20,10])
    pygame.draw.rect(ecran, ROUGE, [x-3,y-50, 10,20])
    pygame.draw.rect(ecran, ROUGE, [x-3,y+25, 10,20])
    
    ecran.blit(image_nom_joueur, [robin.x,robin.y-20])
    ecran.blit(image_nom_joueurr, [matteo.x,matteo.y-20])
    ecran.blit(image_nom_joueurrr, [guilhaime.x,guilhaime.y-20])
    
    ecran.blit(image_munitions, [10,450])
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()