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
BLEU = [0, 0, 255]

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

class Ennemi:
    pass


Zone_X = 185
Zone_Y = 180
Combat = 1
PV = 99
PVCHARA = 500
attaque = 0

enemi1 = Ennemi()
enemi1.X1 = 200
enemi1.Y1 = 200

enemi2 = Ennemi()
enemi2.X1 = 300
enemi2.Y1 = 300

enemi3 = Ennemi()
enemi3.X1 = 400
enemi3.Y1 = 400

enemi4 = Ennemi()
enemi4.X1 = 100
enemi4.Y1 = 100

les_ennemis = [enemi1, enemi2, enemi3, enemi4]

POWER = 0



timer = 0

Coeur = pygame.image.load('Heart.png').convert_alpha()
Zone = pygame.image.load('Zone.png').convert_alpha()
COMBAT = pygame.image.load('COMBAT.png').convert_alpha()
SOIN = pygame.image.load('SOIN.png').convert_alpha()
COMBAT2 = pygame.image.load('COMBAT2.png').convert_alpha()
SOIN2 = pygame.image.load('SOIN2.png').convert_alpha()
Info = pygame.image.load('PlayerInfo.png').convert_alpha()
Knife = pygame.image.load('Knife.png').convert_alpha()
GAME_OVER = pygame.image.load('GAME_OVER.png').convert_alpha()

print(Knife.get_width(), Knife.get_height())

musique = pygame.mixer.Sound('REALMEGALOVANIA.ogg')
attack = pygame.mixer.Sound('attack.wav')
Determination = pygame.mixer.Sound('Determination.ogg')
RECOVER = pygame.mixer.Sound('RECOVER.ogg')
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
                if Frisk.X1 < 30:
                    Frisk.X1 = 30
                if Frisk.X1 > 190:
                    Frisk.X1 = 190
                if event.key == 13:
                    if Frisk.X1 == 30:
                        if Frisk.Y1 == 450:
                            PVCHARA = PVCHARA - 20
                            Combat = 0
                            timer = 1
                            Frisk.X1 = 334
                            Frisk.Y1 = 275
                            attack.play()
                            POWER = POWER + 5
                    if Frisk.X1 == 190:
                        if Frisk.Y1 == 450:
                            timer = 1
                            Frisk.X1 = 334
                            Frisk.Y1 = 275
                            Combat = 0
                            PV = PV + POWER
                            POWER = 0
                            RECOVER.play()
                            if PV > 99:
                                PV = 99


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
    
    # déplacement de l'ennemi
    
    Frisk.X2 = Frisk.X1 + 16
    Frisk.Y2 = Frisk.Y1 + 16
    
    for e in les_ennemis:
        e.X2 = e.X1 + 83
        e.Y2 = e.Y1 + 22
    
    if PV > 99:
        PV = 99
        
    q = 0
    while q < len(les_ennemis):
        if not(Frisk.X2 < les_ennemis[q].X1
               or Frisk.X1 > les_ennemis[q].X2
               or Frisk.Y2 < les_ennemis[q].Y1
               or Frisk.Y1 > les_ennemis[q].Y2):
            PV = PV - 1
        q = q + 1        


    # IMAGES/DESSINS

    ecran.fill(NOIR)

    if Frisk.X1 == 30:
        if Frisk.Y1 == 450:
            ecran.blit(COMBAT2, [22, 435])
    else:
            ecran.blit(COMBAT, [22, 435])

    if Frisk.X1 == 190:
        if Frisk.Y1 == 450:
                ecran.blit(SOIN2, [182, 435])
    else:
            ecran.blit(SOIN, [182, 435])

    ecran.blit(Info, [22, 400])
    ecran.blit(Zone, [Zone_X, Zone_Y])
    
    #¢pygame.draw.rect(ecran, BLANC, [enemi1.X1, enemi1.Y1, Knife.get_width(), Knife.get_height()], 1)
    #ecran.blit(Knife, [enemi1.X1, enemi1.Y1])
    i = 0
    while i < len(les_ennemis):
        pygame.draw.rect(ecran, BLANC, [les_ennemis[i].X1, les_ennemis[i].Y1, Knife.get_width(), Knife.get_height()], 1)
        ecran.blit(Knife, [les_ennemis[i].X1, les_ennemis[i].Y1])
        i = i + 1

    
    ecran.blit(Coeur, [Frisk.X1, Frisk.Y1])

    for element in listeElementMenu:
        element.dessiner()

    pygame.draw.rect(ecran, ROUGE, [255,400, 99,16])
    pygame.draw.rect(ecran, JAUNE, [255,400, PV,16])

    image_PV = font.render(str(PV) + "/99", True, BLANC)
    ecran.blit(image_PV, [370,395])
    
    image_Timer = font.render("Temps: " + str(200-timer), True, BLANC)
    ecran.blit(image_Timer, [450,395])
    
    image_POWER = font.render(str(POWER) + "/100", True, BLANC)
    ecran.blit(image_POWER, [430,444])

    pygame.draw.rect(ecran, GRIS, [100,20, 500,16])
    pygame.draw.rect(ecran, VERT, [100,20, PVCHARA,16])

    pygame.draw.rect(ecran, ROUGE, [320,448, 100,16])
    pygame.draw.rect(ecran, JAUNE, [320,448, POWER,16])

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