
import pygame
pygame.init()
taille = [700, 500]
ecran = pygame.display.set_mode(taille)
a=50
xb=10
yb=500
dxb=0
dyb=0
saut=1
sens=1
isVersHaut=0
isVersBas=0
direction=0
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

# 0 veut dire pas sur un sol 1 oui
def IsOnAFloor(x,y):
    if y > 490:
        print("Sur le fond en :", x,y)
        return 1
    elif(y<=yBlocRouge-4  and y>=yBlocRouge-10 and x+10>=xBlocRouge and x-10<=xBlocRouge+largeurXBloc):
        return 1
    elif(y<=yBlocBleu-4  and y>=yBlocBleu-10 and x+10>=xBlocBleu and x-10<=xBlocBleu+largeurXBloc):
        #je suis sur le cube
        print("sur cube")
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
        if IsOnAFloor(xb, yb) == 1: # A modifier 
            saut = 1
    if saut==1:
        compteurSaut=compteurSaut+1
        dyb=-4
        if compteurSaut>=20:
            saut=0

    elif IsOnAFloor(xb,yb)==1:
        dyb=0
    else :
        dyb=4
    if IsOnAFloor(xb,yb)==1 and compteurSaut > 20:
        compteurSaut = 0
        saut=0
    
    if (xb+10>=xBlocRouge
        and xb-10<=xBlocRouge+largeurXBloc
        and yb+10>=yBlocRouge
        and yb-10<=yBlocRouge+largeurYBloc):
        if direction==0:
            ...
            #xb=xb+5       
        elif direction==1:         
            ...
            #xb=xb-5 
    if xb>=690:
        xb=xb-5
    if xb<=10:
        xb=xb+5 
    if yb<=10:
        yb=yb+5
    if yb>=490:
        ...
        #yb=yb-5
    xb=xb+dxb
    yb=yb+dyb          
    # DESSIN
    ecran.fill(BLANC)
    pygame.draw.rect(ecran, ROUGE, [xBlocRouge,yBlocRouge,largeurXBloc,largeurYBloc])
    pygame.draw.rect(ecran, BLEU, [xBlocBleu,yBlocBleu,largeurXBloc,largeurYBloc])
    pygame.draw.circle(ecran, BLEU, [a,200], 20)
    pygame.draw.circle(ecran, VERT, [xb,yb], 10)
    pygame.display.flip()
    clock.tick(60)
    print(saut)
    
pygame.quit()


