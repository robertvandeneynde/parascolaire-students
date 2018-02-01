import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

blanc = [255, 255, 255]
bleu = [0, 0, 255]

bu1 = 100
bu2 = 200
grosseur = 20
KEY_Q = 97
KEY_D = 100
KEY_Z = 119
KEY_S = 115

#musique = pygame.mixer.Sound("Megalovania.ogg")
grandir = pygame.mixer.Sound("grandir.wav")
retrecir = pygame.mixer.Sound("retrecir.wav")
#musique.play()

fini = 0
while fini == 0:d
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            print("La touche numero", event.key)
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 273:
                grandir.play()
            if event.key == 274:
                retrecir.play()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Clic en", event.pos[0], event.pos[1])
            listeDeBalles.append(balle(blanc, 12,event.pos[0], event.pos[1]))

    pressed = pygame.key.get_pressed()

    if pressed[273]:
        grosseur = grosseur + 2

    if pressed[274]:
        grosseur = grosseur - 2

        if grosseur < 2:
            grosseur = 1
    
    if pressed[KEY_Z]:
        bu2 = bu2 - 5
        
    if pressed[KEY_S]:
        bu2 = bu2 + 5
    
    if pressed[KEY_Q]:
        bu1 = bu1 - 5
        
    if pressed[KEY_D]:
        bu1 = bu1 + 5
                       
    if bu1 > 700 - grosseur:
        bu1 = 700 - grosseur
        
    if bu1 < grosseur:
        bu1 = grosseur
        
    if bu2 > 500 - grosseur:
        bu2 = 500 - grosseur
        
    if bu2 < grosseur:
        bu2 = grosseur
    
    # dessin
    ecran.fill(blanc)
    pygame.draw.circle(ecran, bleu, [bu1, bu2], grosseur)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
