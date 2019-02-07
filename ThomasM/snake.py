import pygame

pygame.init()

taille = [700, 700]
ecran = pygame.display.set_mode(taille)

class Segment:
    r = 15
    x = 0
    y = 0
    color = [10,10,10]
    def __init__(self,x, y):
        self.x = x
        self.y = y


snake = []
snake.append(Segment(taille[0]/2,taille[1]/2))

clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    # TICK

    # DESSIN
    ecran.fill([255,255,255])

    i = 0
    while i < len(snake):

        pygame.draw.circle(ecran, snake[i].color, [snake[i].x,snake[i].y], snake[i].r)
        i += 1

    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()