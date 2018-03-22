import pygame
pygame.init()

taille = [800, 500]
ecran = pygame.display.set_mode(taille)


VERT = [0, 255, 0]
BLANC = [255, 255, 255]
BLEU = [0, 0, 255]
CYAN = [24, 156, 171]
ROUGE = [255, 0, 0]

GAUCHE = 276
DROITE = 275
HAUT = 273 
BAS = 274

playerX = 50
playerY = 200

perso = 100
image_perso = pygame.image.load('player.png').convert_alpha()

opponentY = 200

ball_x = 100
ball_y = 100
balle_sens_x = 100
balle_sens_y = 100

opponentX = 730
sensrect1 = 100


clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
            
    if ball_x > 800:
        balle_sens_x = -1
    if ball_x < 0:
        balle_sens_x = 1
        
    if balle_sens_x == 1:
        ball_x = ball_x + 4
    else:
        ball_x = ball_x -4

    if ball_y > 500:
        balle_sens_y = -1
    if ball_y < 0:
        balle_sens_y = 1
            
    if balle_sens_y == 1:
        ball_y = ball_y +4
        
    else:
        ball_y = ball_y -4
        
    if playerY > 500 - 50:
        playerY = 500 - 50 
    
    if playerY < 0:
        playerY = 0
    
    # clavier
    pressed = pygame.key.get_pressed()

    if pressed[HAUT]:
        playerY -= 8

    if pressed[BAS]:
        playerY += 8
    # collisions
    if ball_x <= playerX + 20 and playerY < ball_y < playerY + 50:
        balle_sens_x = 1
        
    if ball_x >= opponentX: # and opponentY < ball_y < opponentY + 50:
        balle_sens_x = -1

    ecran.fill(BLANC)
    # dessin
    
    ecran.blit(image_perso, [perso -99, 1])

    pygame.draw.rect(ecran, CYAN, [playerX, playerY, 20, 50])
    pygame.draw.circle(ecran, VERT, [ball_x, ball_y], 10) 
    pygame.draw.rect(ecran, ROUGE, [opponentX, ball_y-25, 20, 50])
    pygame.display.flip()

    
    clock.tick(60)
    
pygame.quit()