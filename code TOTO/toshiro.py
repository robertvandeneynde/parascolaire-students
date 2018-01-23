import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)
grosseur = 20


clock = pygame.time.Clock()

blanc = [255, 255, 255]
rouge = [255, 0, 0]

listeDeBalles = []
class balle :
    def __init__(self, couleur, rayon, x, y):
        self.couleur = couleur
        self.rayon = rayon
        self.x = x
        self.y = y


bu1 = 100
bu2 = 200

#musique = pygame.mixer.Sound("Megalovania.ogg")
grandir = pygame.mixer.Sound("grandir.wav")
retrecir = pygame.mixer.Sound("retrecir.wav")
#musique.play()

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            print("La touche numero", event.key)
        elif event.type == pygame.KEYDOWN:
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
    
    if pressed[119]:
        bu1 = bu1 + 3




    ecran.fill(blanc)
    pygame.draw.circle(ecran, rouge, [bu1, bu2], grosseur)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
