import pygame
from random import randint
pygame.init()

taille = [700, 700]
R = 15
Rr = 10

bonus_x = randint(0,taille[0]) // 30 * 30 + R
bonus_y = randint(0, taille[1]) // 30 * 30 + R
ecran = pygame.display.set_mode(taille)

# 0 : UP, 1 : Right, 2 : Down, 3 : Left 
last_direction = 0
class Segment:
    r = R
    x = 0
    y = 0
    color = [10,10,10]
    def __init__(self,x, y):
        self.x = x
        self.y = y


snake = []
snake.append(Segment(taille[0]//2 // 30 * 30 + R, taille[1]//2 // 30 * 30 + R))
snake.append(Segment(taille[0]//2 // 30 * 30 + R, taille[1]//2 // 30 * 30 + R + R*2))
snake.append(Segment(taille[0]//2 // 30 * 30 + R, taille[1]//2 // 30 * 30 + R + 2* R*2))
clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                last_direction = 1
            elif event.key == pygame.K_UP:
                last_direction = 0
            elif event.key == pygame.K_DOWN:
                last_direction = 2
            elif event.key == pygame.K_LEFT:
                last_direction = 3              
    
    # TICK

    # DESSIN
    ecran.fill([255,255,255])


    # Mouvement
    # poistion of the snake 's head
    (head_x, head_y) = (snake[0].x, snake[0].y)
    
    if last_direction == 0:
        # UP
        head_y = head_y - R * 2
        head_x = head_x
    elif last_direction == 1:
        # Right
        head_y = head_y 
        head_x = head_x + R * 2 
    elif last_direction == 2:
        # Down
        head_y = head_y + R * 2
        head_x = head_x
    elif last_direction == 3:
        # Down
        head_y = head_y 
        head_x = head_x - R * 2 
    
    # Supprimer le dernier segment du snake
    snake.pop()
    # Créer une nouvelle tête
    snake.insert(0,Segment(head_x, head_y))
    
    # Dessin
    # Snake
    i = 0
    while i < len(snake):

        pygame.draw.circle(ecran, snake[i].color, [snake[i].x,snake[i].y], snake[i].r)
        i += 1
    # Bonus
    pygame.draw.circle(ecran, [100, 100, 50], [bonus_x, bonus_y], Rr)
    pygame.display.flip()
    
    clock.tick(4)
    
pygame.quit()