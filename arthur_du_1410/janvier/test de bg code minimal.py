from __future__ import print_function, division


import pygame
pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)
ma_position2 = 100
ma_position = 100
sens = + 1
NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            fini = 1
        elif event.type == pygame.KEYDOWN:
            print("La touche numero", event.key)
            if event.key == 276:
                ma_position2 = ma_position2 - 100
            elif event.key == 275:  # touche droite
                ma_position2 = ma_position2 + 100
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ecran.fill(BLANC)
    if sens == + 1:
            ma_position = ma_position + 5
    if sens == - 1:
        ma_position = ma_position - 5
    if ma_position > 700:
        sens = -1
    if ma_position < 0 :
        sens = + 1
    ecran.fill(BLANC) 
    
    pygame.draw.rect(ecran, ROUGE, [ma_position2,200, 20,40])
    pygame.draw.circle(ecran, BLEU, [100,200], 20) 
    pygame.draw.circle(ecran, VERT, [ma_position, 80], 10) 
    pygame.draw.polygon(ecran, ROUGE, [[0,50], [100,0], [100,100]])
    pygame.display.flip()
    
    
    clock.tick(1000)
    
pygame.quit()