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

        #Afficher le coeur et ger son comportement
joueurEstMort = 0

class Frisk:
    pass
Frisk.X1 = 30
Frisk.Y1 = 450


Zone_X = 185
Zone_Y = 180
Combat = 1
PV = 99
PVCHARA = 500
Action = 0
attaque = 0
enemi_X1 = 200
enemi_Y1 = 200



timer = 0

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
                    Frisk.X1 = Frisk.X1 - 160
                if event.key == 275:
                    Frisk.X1 = Frisk.X1 + 160
                if event.key == 13:
                    if Frisk.X1 == 30:
                        if Frisk.Y1 == 450:
                            damage = random.randrange(25)
                            realdamage = damage + 25
                            PVCHARA = PVCHARA - realdamage
                            Combat = 0
                            timer = 1
                            Frisk.X1 = 334
                            Frisk.Y1 = 275
                            attack.play()
                    if Frisk.X1 == 190:
                        if Frisk.Y1 == 450:
                            Zone = ACTIONInfo
                            Zone_X = 85
                            Frisk.X1 = 105
                            Frisk.Y1 = 215
                            Combat = 2
            elif Combat == 2:
                if event.key == 276:
                    Frisk.X1 = Frisk.X1 - 265
                if event.key == 275:
                    Frisk.X1 = Frisk.X1 + 265
                if event.key == 303:
                    if Zone == ACTIONInfo:
                        Combat == 1
                        Zone == Zone
                        Frisk.X1 == 30
                        Frisk.Y1 == 450
                        
                if Frisk.X1 < 105:
                    Frisk.X1 = 105
                if Frisk.X1 > 370:
                    Frisk.X1 = 370

    Frisk.X2 = Frisk.X1 + 16
    Frisk.Y2 = Frisk.Y1 + 16
    enemi_X2 = enemi_X1 + 83
    enemi_Y2 = enemi_Y1 + 22

    pressed = pygame.key.get_pressed()
    
    if Combat == 0:
        if pressed[276]:
            Frisk.X1 = Frisk.X1 - 3
            
        if pressed[275]:
            Frisk.X1 = Frisk.X1 + 3
            
        if pressed[273]:
            Frisk.Y1 = Frisk.Y1 - 3
            
        if pressed[274]:
            Frisk.Y1 = Frisk.Y1 + 3

        #timer start
    if timer >= 1:
        timer = timer + 1

    if timer > 200:
        timer = 0
        Combat = 1
        Frisk.X1 = 30
        Frisk.Y1 = 450
        #timer end

    if Combat ==1:
        if Frisk.X1 < 30:
            Frisk.X1 = 30
        if Frisk.X1 > 510:
            Frisk.X1 = 510

    if Combat == 0:
        if Frisk.X1 < 189:
            Frisk.X1 = 189
        if Frisk.X1 > 465:
            Frisk.X1 = 465
        if Frisk.Y1 < 184:
            Frisk.Y1 = 184
        if Frisk.Y1 > 360:
            Frisk.Y1 = 360

    if PV > 99:
        PV = 99


    if Frisk.X2 < enemi_X1:  # perso est trop à gauche
        PV == PV
    elif Frisk.X1 > enemi_X2:  # perso est trop à droite
        PV == PV
    elif Frisk.Y2 < enemi_Y1:  # perso est trop en haut
        PV == PV
    elif Frisk.Y1 > enemi_Y2:  # perso est trop en bas
        PV == PV
    else:
        PV = PV - 1
        damage.play()

    print (timer)
        
    #IMAGES/DESSINS

    ecran.fill(NOIR)

    ecran.blit (Info, [22, 400])
    ecran.blit (COMBAT, [22, 435])
    ecran.blit (ACTION, [182, 435])
    ecran.blit (OBJET, [342, 435])
    ecran.blit (CLEMENCE, [502, 435])
    ecran.blit (Zone, [Zone_X, Zone_Y])
    ecran.blit (Knife, [enemi_X1, enemi_Y1])
    ecran.blit (Coeur, [Frisk.X1, Frisk.Y1])

    for element in listeElementMenu:
        element.dessiner()

    pygame.draw.rect(ecran, ROUGE, [255,400, 99,16])
    pygame.draw.rect(ecran, JAUNE, [255,400, PV,16])

    image_PV = font.render(str(PV) + "/99", True, BLANC)
    ecran.blit(image_PV, [370,395])

    pygame.draw.rect(ecran, GRIS, [100,20, 500,16])
    pygame.draw.rect(ecran, VERT, [100,20, PVCHARA,16])

    #GAME OVER

    if PV < 1 and joueurEstMort == 0:
        musique.stop()
        Determination.play(loops=-1, maxtime=0, fade_ms=0)
        joueurEstMort = 1

    if joueurEstMort == 1:
        ecran.blit(GAME_OVER, [0, 0])
        Frisk.X1 == 0
        Frisk.Y1 == 0
    pygame.display.flip()

    clock.tick(60)

pygame.quit()