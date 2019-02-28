
import pygame
pygame.init()
taille = [700, 500]
ecran = pygame.display.set_mode(taille)
a=50
xb=10
yb=400
dxb=0
dyb=0
saut=1
sens=1
isVersHaut=0
isVersBas=0
direction=0
xBV=200
yBV=350
xBlocRouge=100
yBlocRouge=450
xBlocBleu=150
yBlocBleu=400
largeurXBloc=50
largeurYBloc=20
compteurSaut=0
saut=0
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
couleurBalle=VERT

# 0 veut dire pas sur un sol 1 oui
def IsOnAFloor(x,y,xBloc,yBloc,Largeurbloc,longueurBloc):
    if y >= 490:
        print("Sur le fond en :", x,y)
        return 1
    elif(y<=yBloc-4  and y>=yBloc-10 and x+10>=xBloc and x-10<=xBloc+Largeurbloc):
        #je suis sur le cube
        return 1
    else:
        return 0
# DÉBUT
clock = pygame.time.Clock()
fini = 0
while fini == 0:
    dxb = 0
    dyb = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    pressed = pygame.key.get_pressed() 
    
    # TICK
    if sens==1:
        a=a+5
    else:
        a=a-5
    if a>=700-largeurXBloc:
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
        if IsOnAFloor(xb, yb,xBlocBleu,yBlocBleu,largeurXBloc,largeurYBloc)==1 or IsOnAFloor(xb, yb,xBlocRouge,yBlocRouge,largeurXBloc,largeurYBloc) == 1 or IsOnAFloor(xb, yb,xBV,yBV,largeurXBloc,largeurYBloc) == 1 or IsOnAFloor(xb, yb,a,300,largeurXBloc,largeurYBloc)==1: # A modifier 
            saut = 1
            if IsOnAFloor(xb, yb, a, 300, largeurXBloc, largeurYBloc)==1:
                xb=a+25
                print("oui")
    if saut==1:
        compteurSaut=compteurSaut+1
        dyb=-4
        if compteurSaut>=20:
            saut=0
            compteurSaut=0
    elif IsOnAFloor(xb, yb,xBlocRouge,yBlocRouge,largeurXBloc,largeurYBloc)==1 or IsOnAFloor(xb, yb,xBlocBleu,yBlocBleu,largeurXBloc,largeurYBloc)==1 or IsOnAFloor(xb, yb,xBV,yBV,largeurXBloc,largeurYBloc)==1 or IsOnAFloor(xb, yb,a,300,largeurXBloc,largeurYBloc)==1:
        dyb=0
    else :
        dyb=4
    if(saut==1):
        couleurBalle=BLEU
    else:
        couleurBalle=VERT
    xb=xb+dxb
    yb=yb+dyb       
    if xb>=690:
        xb=xb-5
    if xb<=10:
        xb=xb+5 
    if yb<=10:
        yb=yb+5
    if yb>490:
        yb=490
            
    # DESSIN
    ecran.fill(NOIR)
    pygame.draw.rect(ecran, ROUGE, [xBlocRouge, yBlocRouge, largeurXBloc, largeurYBloc])
    pygame.draw.rect(ecran, BLEU, [xBlocBleu, yBlocBleu, largeurXBloc, largeurYBloc])
    pygame.draw.rect(ecran, VERT, [xBV, yBV, largeurXBloc, largeurYBloc])
    pygame.draw.rect(ecran, BLEU, [a,300, largeurXBloc, largeurYBloc])
    pygame.draw.circle(ecran, couleurBalle, [xb,yb], 10)
    pygame.display.flip()
    clock.tick(60)
    
    
pygame.quit()


