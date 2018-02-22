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

Y = 200
Y2 = 200
ball_x= 100
ball_y= 100
sens_x= 100
sens_y= 100


rect1 =50
rect2 =730
sensrect1=100

ball2 = 100
sensball2 = 100

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
        ball_x = ball_x +4
    
    
    else:
        ball_x = ball_x -4



    if ball_y > 500:
        sens_y = -1
    if ball_y < 0:
        sens_y = 1
            
    if sens_y == 1:
        ball_y = ball_y +4
        
    else:
        ball_y = ball_y -4
        
    if Y > 500 - 50:
        Y = 500 - 50 
    
    if Y < 0:
        Y = 0
    
  
    
    # clavier
    pressed = pygame.key.get_pressed()

    if pressed[HAUT]:
        Y -= 8

    if pressed[BAS]:
        Y += 8
        #colision
    if ball_x <= rect1 + 20 and Y < ball_y < Y + 50:
        sens_x = 1
        
    if ball_x >= rect2  and Y2 < ball_y < Y2 + 50:
        sens_x = 1
    



    # dessin
    ecran.fill(BLANC)
    
    pygame.draw.rect(ecran, CYAN, [rect1, Y, 20, 50])
    pygame.draw.circle(ecran, VERT, [ball_x, ball_y], 10) 
    pygame.draw.rect(ecran, ROUGE, [rect2, ball_y-25, 20, 50])
    pygame.display.flip()

    
    clock.tick(60)
    
pygame.quit()