import random
import pygame
pygame.init()
taille = [700, 500]
ecran = pygame.display.set_mode(taille)


NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
GRIS = [99, 99, 99]
VERT = [0, 255, 0]
JAUNE = [255, 255, 0]
ROUGE = [255, 0, 0]

font = pygame.font.SysFont('Impact', 20)

def deroulementDuCombat():
    fini = 0
    while(fini):
        pygame

        #Afficher le coeur et g??rer son comportement
joueurEstMort = 0


X = 30
Y = 450
X2 = X + 16
Y2 = Y + 16
Zone_X = 185
Zone_Y = 180
Combat = 1
PV = 99
PVCHARA = 500
Action = 0
attaque = 0
enemi_X1 = 200
enemi_Y1 = 200
enemi_X2 = enemi_X1 + 83
enemi_Y2 = enemi_Y1 + 22

Coeur = pygame.image.load('Heart.png').convert_alpha()
Zone = pygame.image.load('Zone.png').convert_alpha()
Zone2 = pygame.image.load('Zone2.png').convert_alpha()
COMBAT = pygame.image.load('COMBAT.png').convert_alpha()
ACTION = pygame.image.load('ACTION.png').convert_alpha()
OBJET = pygame.image.load('OBJET.png').convert_alpha()
CLEMENCE = pygame.image.load('CLEMENCE.png').convert_alpha()
Info = pygame.image.load('PlayerInfo.png').convert_alpha()
ACTIONInfo = pygame.image.load('ACTIONINFO.png').convert_alpha()
Knife = pygame.image.load('Knife.png').convert_alpha()
GAME_OVER = pygame.image.load('GAME_OVER.png').convert_alpha()

musique = pygame.mixer.Sound('REALMEGALOVANIA.ogg')
damage = pygame.mixer.Sound('TakeDamage.ogg')
attack = pygame.mixer.Sound('attack.wav')
Determination = pygame.mixer.Sound('Determination.ogg')
musique.play(loops=-1, maxtime=0, fade_ms=0)

clock = pygame.time.Clock()

class elementMenu:
    def __init__(self, nomImage, positionX, positionY, ecran):
        self.Image = pygame.image.load(nomImage).convert_alpha()
        self.posX = positionX
        self.posY = positionY
        self.ecran = ecran
    def dessiner(self):
        self.ecran.blit(self.Image, [self.posX, self.posY])

listeElementMenu = []

listeElementMenu.append(elementMenu('CharaCombat.png', 280, 50, ecran))

fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1

        elif event.type == pygame.KEYDOWN:
            if Combat == 1:
                if event.key == 276:
                    X = X - 160
                if event.key == 275:
                    X = X + 160
                if event.key == 13:
                    if X == 30:
                        if Y == 450:
                            deroulementDuCombat()
    
                            PVCHARA = PVCHARA -25
                            Combat = 0
                            X = 334
                            Y = 275
                            attack.play()
                    if X == 190:
                        if Y == 450:
                            Zone = ACTIONInfo
                            Zone_X = 85
                            X = 105
                            Y = 215
                            Combat = 2
            elif Combat == 2:
                if event.key == 276:
                    X = X - 265
                if event.key == 275:
                    X = X + 265
                if event.key == 303:
                    if Zone == ACTIONInfo:
                        Combat == 1
                        Zone == Zone
                        X == 30
                        Y == 450
                        
                if X < 105:
                    X = 105
                if X > 370:
                    X = 370



    pressed = pygame.key.get_pressed()
    
    if Combat == 0:
        if pressed[276]:
            X = X - 5
            
        if pressed[275]:
            X = X + 5
            
        if pressed[273]:
            Y = Y - 5
            
        if pressed[274]:
            Y = Y + 5



    if Combat ==1:
        if X < 30:
            X = 30
        if X > 510:
            X = 510

    if Combat == 0:
        if X < 189:
            X = 189
        if X > 465:
            X = 465
        if Y < 184:
            Y = 184
        if Y > 360:
            Y = 360

    if PV > 99:
        PV = 99


    if X < enemi_X1:  # perso est trop ?? gauche
        PV == PV
    elif X > enemi_X2:  # perso est trop ?? droite
        PV == PV
    elif Y < enemi_Y1:  # perso est trop en haut
        PV == PV
    elif Y > enemi_Y2:  # perso est trop en bas
        PV == PV
    else:
        PV = PV - 1
        damage.play()
        
    #IMAGES/DESSINS

    ecran.fill(NOIR)

    ecran.blit (Info, [22, 400])
    ecran.blit (COMBAT, [22, 435])
    ecran.blit (ACTION, [182, 435])
    ecran.blit (OBJET, [342, 435])
    ecran.blit (CLEMENCE, [502, 435])
    ecran.blit (Zone, [Zone_X, Zone_Y])
    ecran.blit (Knife, [enemi_X1, enemi_Y1])
    ecran.blit (Coeur, [X, Y])

    for element in listeElementMenu:
        element.dessiner()

    pygame.draw.rect(ecran, ROUGE, [255,400, 99,16])
    pygame.draw.rect(ecran, JAUNE, [255,400, PV,16])

    image_PV = font.render(str(PV) + "/99", True, BLANC)
    ecran.blit(image_PV, [370,395])

    pygame.draw.rect(ecran, GRIS, [100,20, 500,16])
    pygame.draw.rect(ecran, VERT, [100,20, PVCHARA,16])

    #GAME OVER

    if PV < 0 and joueurEstMort == 0:
        musique.stop()
        Determination.play(loops=-1, maxtime=0, fade_ms=0)
        joueurEstMort = 1

    if joueurEstMort == 1:
        ecran.blit(GAME_OVER, [0, 0])
    pygame.display.flip()

    clock.tick(30)

pygame.quit()