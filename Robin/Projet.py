
import pygame
pygame.init()
taille = [700, 500]
ecran = pygame.display.set_mode(taille)
a=50
xb=10
yb=500
dxb=0
dyb=0
sens=1
isVersHaut=0
isVersBas=0
direction=0
xBlocRouge=100
yBlocRouge=450
largeurXBlocRouge=50
largeurYBlocRouge=40
compteurSaut=0
saut=0
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT
clock = pygame.time.Clock()
fini = 0
while fini == 0: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    pressed = pygame.key.get_pressed() 
    
    # TICK
    if sens==1:
        a=a+5
    else:
        a=a-5
    
    if a>=690:
        sens=-1
        
    if a<=0:
        sens=1
    dxb = 0
    if pressed[pygame.K_LEFT]: #touche fleche gauche
        dxb = dxb - 5
        direction = 0
        
    if pressed[pygame.K_RIGHT]: #touche fleche droite
        dxb = dxb + 5
        direction = 1  
        
    if pressed[pygame.K_SPACE]:
        saut = 1
        direction = 3
    dyb=0
    if saut==1:
        compteurSaut=compteurSaut+1
        if compteurSaut<20:
            dyb=-4
        else:
            dyb=4
            if yb>=490:
                compteurSaut = 0
                saut = 0                
            if yb+5 >= yBlocRouge - 8:
                if xb + 10 <= xBlocRouge:
                    if xb - 10 >= xBlocRouge + largeurXBlocRouge:
                        compteurSaut = 0
                        saut = 0
    if(yb+4<=yBlocRouge and xb+10>=xBlocRouge and xb-10<=xBlocRouge+largeurXBlocRouge):
        isVersHaut=1
        isVersBas=0
    else : 
        isVersHaut=0
    
    if (xb+10>=xBlocRouge
        and xb-10<=xBlocRouge+largeurXBlocRouge
        and yb+10>=yBlocRouge
        and yb-10<=yBlocRouge+largeurYBlocRouge):
        if direction==0:
            if(isVersHaut==0):
                xb=xb+5
            if(isVersHaut==1):
                dyb=0            
        elif direction==1:
            if(isVersHaut==0):           
                xb=xb-5
            if(isVersHaut==1):
                dyb=0            
        elif direction==2:
            yb=yb-5         
        elif direction==3:
            if(isVersHaut==0):
                dyb=0         
    if xb>=690:
        xb=xb-5
    if xb<=10:
        xb=xb+5 
    if yb<=10:
        yb=yb+5
    if yb>=490:
        yb=yb-5
    xb = xb + dxb
    yb = yb + dyb          
    # DESSIN
    ecran.fill(BLANC)
    print(dyb," ",dxb)
    pygame.draw.rect(ecran, ROUGE, [xBlocRouge,yBlocRouge,largeurXBlocRouge,largeurYBlocRouge])
    pygame.draw.circle(ecran, BLEU, [a,200], 20)
    pygame.draw.circle(ecran, VERT, [xb,yb], 10)
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
