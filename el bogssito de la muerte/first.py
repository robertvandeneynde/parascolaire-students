import pygame
import random
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

noir = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

class Ennemi:
    pass

def Move(ennemis, vitesse):
    if ennemis.etat==1 :
        ennemis.x = ennemis.x+vitesse
# fond d'écran
image = pygame.image.load("thumb.jpg").convert_alpha()
image = pygame.transform.smoothscale(image, taille)
# état des joueurs
robin = Ennemi()
robin.etat = 1
robin.x = 200
robin.xx = 250
robin.y = 200
robin.yy = 250
robin.l = 50
robin.h = 50
robin.nom = "Robiche"

guilhaime = Ennemi()
guilhaime.etat = 1
guilhaime.x = 450
guilhaime.xx = 500
guilhaime.y = 350
guilhaime.yy = 400
guilhaime.l = 50
guilhaime.h = 50
guilhaime.nom = "guilhem le caillou"
matteo = Ennemi()
matteo.etat = 1
matteo.x = 250
matteo.xx = 350
matteo.y = 300
matteo.yy = 350
matteo.l = 100
matteo.h = 50
matteo.nom = "Mattégro"
print(len(matteo.nom))

sadek = Ennemi()
sadek.etat = 1
sadek.x = 400
sadek.xx = 450
sadek.y = 60
sadek.yy= 110
sadek.l = 50
sadek.h = 50
sadek.nom = "sadekonpas"

florent = Ennemi()
florent.etat = 1
florent.x = 50
florent.xx = 100
florent.y = 350
florent.yy = 450
florent.l = 50
florent.h = 100
florent.nom = "fliflou le méga géant"

liste_ennemis = [robin, guilhaime, matteo, sadek, florent]
# état des munitions
munitionsMax = 7
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
                i = 0
                while i < len(liste_ennemis):
                    if liste_ennemis[i].x <= x <= liste_ennemis[i].x + liste_ennemis[i].l : # le clic touche 
                        if liste_ennemis[i].y <= y <= liste_ennemis[i].y + liste_ennemis[i].h :
                            liste_ennemis[i].etat  = 0
                    i = i + 1  
                        
                munition = munition-1       
        
        elif event.type == pygame.KEYDOWN :
            if event.key== pygame.K_SPACE :
                munition = munitionsMax
            
    # mouvement des ennemis
    i=0
    while i < len(liste_ennemis) :
        Move(liste_ennemis[i], i+0.5)
        i = i+1
    
    #endgame
    i = 0
    while i< len(liste_ennemis) :
        if liste_ennemis[i].x == 750 :
            if liste_ennemis[i].etat == 1 :
                fini = 1
        i=i+1
    
    position_souris = pygame.mouse.get_pos() # liste de taille 2 avec x,y 
    
    # TICK
    x = position_souris[0]
    y = position_souris[1]
    
    # DESSIN
    
        
    image_nom_joueur = font.render("Robiche", True, noir)
    image_nom_joueurr = font.render("Mattégro", True, noir)
    image_nom_joueurrrr = font.render("sadekonpas", True, noir)
    image_nom_joueurrr = font.render("guilhem le caillou", True, noir)
    image_nom_joueurrrrr = font.render("fliflou le méga géant", True, noir)
    image_nom_dieu = font.render("loic dieu", True, noir)
    
    image_munitions = font.render(str(munition), True, noir)
    ecran.fill(BLANC)
    ecran.blit(image,[0, 0] )
    
    # si le carré est rouge le personnage est vivant sinon il est mort
    for e in liste_ennemis:
        if e.etat == 1:
            pygame.draw.rect(ecran, BLEU, [e.x, e.y, e.l,e.h]) #robin
        else : 
            pygame.draw.rect(ecran, noir, [e.x, e.y, e.l, e.h]) #robin mort 
    #dieu
    pygame.draw.rect(ecran, BLEU, [400,250, 50,50])
    # viseur 
    pygame.draw.rect(ecran, ROUGE, [x-50,y-5, 20,10])
    pygame.draw.circle(ecran, BLEU, [x,y],10)
    pygame.draw.rect(ecran, ROUGE, [x+30,y-5, 20,10])
    pygame.draw.rect(ecran, ROUGE, [x-3,y-50, 10,20])
    pygame.draw.rect(ecran, ROUGE, [x-5,y+25, 10,20])
    
    for e in liste_ennemis:
        image_nom_joueur = font.render(e.nom, True, noir)
        #image_nom_joueur.width, image_nom_joueur.height
        ecran.blit(image_nom_joueur, [e.x, e.y-20])
        
    # ecran.blit(image_nom_joueur, [robin.x,robin.y-20])
    # ecran.blit(image_nom_joueurr, [matteo.x,matteo.y-20])
    # ecran.blit(image_nom_joueurrr, [guilhaime.x-50,guilhaime.y-20])
    # ecran.blit(image_nom_joueurrrr, [sadek.x-30,sadek.y-20])
    # ecran.blit(image_nom_joueurrrrr, [florent.x-50,florent.y-30])
    
    
    ecran.blit(image_nom_dieu, [400, 230])
    
    ecran.blit(image_munitions, [10,450])
    
    pygame.display.flip()
    
    clock.tick(60)

    
  
fini = 0
while fini == 0:
    #event
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    ecran.fill(ROUGE)
    image_noob = font.render("U ARE NOOOOOB", True, noir)
    ecran.blit(image_noob, [320, 200])
    pygame.display.flip()
    clock.tick(1)
    

pygame.quit()