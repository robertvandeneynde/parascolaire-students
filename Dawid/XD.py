import pygame
pygame.init()

taille = [800, 500]
ecran = pygame.display.set_mode(taille)


VERT = [0, 255, 0]
BLANC = [255, 255, 255]
BLEU = [0, 0, 255]
CYAN = [24, 156, 171]

GAUCHE = 276
DROITE = 275
HAUT = 273 
BAS = 274

Y = 50
ball_x= 100
ball_y= 100
sens_x= 100
sens_y= 100
rect1 =40
rect2 =760
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
            
            
    if ball_x > 800:
        sens_x = -1
    if ball_x < 0:
        sens_x = 1
        
    if sens_x == 1:
        ball_x = ball_x +5
    
    else:
        ball_x = ball_x -5

    pressed = pygame.key.get_pressed()

    if pressed[HAUT]:
        Y -= 5

    if pressed[BAS]:
        Y += 5

    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, CYAN, [rect1,Y, 20, 50 ])
    pygame.draw.circle(ecran, VERT, [ball_x, ball_y], 10)
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()