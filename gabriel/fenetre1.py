

import pygame

pygame.init()

#variables
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]
bleu = [31,158,255]
avancement = 0
tir = 0
a = 0
ma_position = 100
ma_position_2 = 20
rect_1 = 120
rect_2 = 200
rekt_3 = 350
taille = [500 ,500]
jeme_suia_chete_unpe_nissan_hor = 12
ecran = pygame.display.set_mode(taille)
bsod = pygame.image.load('bsod.png').convert_alpha()
cpa = pygame.image.load('cpacorsie.jpg')
mairo = pygame.image.load('miro.jpg')
clock = pygame.time.Clock()
tft = pygame.image.load('tfourtweny.jpg')
tardis = pygame.image.load('time_and_relative_dimension_in_space.jpg')
tr = pygame.image.load('tr.jpg')
sys32 = pygame.image.load('life hack informatique impressionant tout a fait san danger cacher dan windowz.jpg')
ff = pygame.image.load('mapemonde.jpg')
cat = pygame.image.load('catapult.jpg')
LV = pygame.image.load('LAMPAVID.jpg')
caca = pygame.image.load('osef.png').convert_alpha()
paysage = [bsod,cpa,mairo,tft,tardis,tr,sys32,ff,cat,LV,caca]
missile = pygame.image.load('chevre.png').convert_alpha()
michel = missile
yep = 0
egg = yep
fini = 0
#fin des variables




while fini == 0:
    monsieur_puel = jeme_suia_chete_unpe_nissan_hor
    cyka_blyat = monsieur_puel
    cucurbitace = cyka_blyat
    jeme_suia_chete_unpe_nissan_hor = cucurbitace    
    p = 12
    avancement += 10
    d = int(a*2/10)
    c = int(ma_position_2 / 10)

    b = int(ma_position / 10)
    ecran_rouge = d*25
    ecran_vert = d*c
    ecran_bleu = d*b
    immmmmage = paysage[a]
    ecran.fill([ecran_rouge, ecran_vert, ecran_bleu])
    ecran.blit(immmmmage ,[78 ,33])
    imposer_la_force_vers_l_ovanium = ma_position_2 * 12
    congolexicomatization = ecran_vert * ecran_bleu


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            print(chr(event.key))

    if ma_position >= 1600:
        ma_position = 2
        a += 1

    if ma_position <= 1:
        ma_position = 1599

    if ma_position_2 >= 900:
        ma_position_2 = 2
    if ma_position_2 <= 1:
        ma_position_2 = 899
    if a >= 10:
        a = 0
       
    p = pygame.key.get_pressed()

    if p[276]:
        ma_position = ma_position - 10
        print("computer")
        egg -= 1
        
    if avancement >= 250:
        tir = 0
    if p[104]:
        a += 1
    if p[275]:
        ma_position += 10
        print("yep yep yep")
        egg += 1


    if p[pygame.K_UP]:
        ma_position_2 -= 10
    if p[274]:
        ma_position_2 += 10
    if p[112]:
        print (ma_position ,ma_position_2)
    if p[32]:
        tir = 1
    if p[312]:
        print("lolololololol")
    if tir == 1:
        pygame.draw.rect(ecran, [100, 200, 255], [avancement + ma_position, ma_position_2, 15, 10])
    if tir == 0:
        avancement = 0
    if p[113]:
        ma_position = 100
        ma_position_2 = 100
    miro = pygame.image.load('lololol.png').convert_alpha()
    deni = pygame.image.load('denis.png').convert_alpha()

    if egg < 28:
        ecran.blit(michel , [imposer_la_force_vers_l_ovanium ,congolexicomatization])


    ecran.blit(miro, [ma_position, ma_position_2])
    ecran.blit(deni, [rekt_3,200])
    pygame.draw.circle(ecran, bleu, [imposer_la_force_vers_l_ovanium,congolexicomatization,], 20)
    pygame.draw.circle(ecran, ROUGE, [rect_2, 250], 10)
    if ma_position == 179:
        if ma_position_2 == 150:
            eguunderscoreimmage = font.render("cd c:/windows/system32", true, [ecran_vert, 267, ecran_rouge])
            ecran.blit(eguunderscoreimmage, 200, 314)
               
    #if ma_position < rect_1:
    #   print("rectangle 1")
    #   print(rect_1-ma_position)
    #elif ma_position > rect_1:
    #    print("rectangle 1")
    #    print(ma_position - rect_1)
    #else:
    #    print("rectangle 1")
    #    print("vous êtes arrivés a destination")

    pygame.display.flip()


    clock.tick(60)


pygame.quit()
