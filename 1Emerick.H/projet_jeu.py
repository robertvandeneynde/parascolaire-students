from __future__ import print_function, division

import pygame

pygame.init()

taille = [1200, 900]

ecran = pygame.display.set_mode(taille)


rouge = [255,0,0]
blanc = [255,255,255]

x= 10
y= 10
a= 10
b= 10


clock = pygame.time.Clock()

fini = 0
while fini == 0:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1

    pressed = pygame.key.get_pressed() 
    
    if pressed[276]: 
        x= x - 5
    if pressed[275]: 
        x = x + 5
    if pressed[274]:
        y=y+5        
    if pressed[273]:
        y=y-5 
        
    if x>=1200:
        x=-20 
    elif x<=-20:
        x=1200  
        
    if y>=900:
        y=-20
    elif y<=-20:
        y=900
    
    print (a,b,x,y)
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [x, y, a, b])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()doi<wbruwqiogriqt<vrdjhbiuyfiyvlsdhigr<o!y§tegrwsg'(!ç<qtç'ç<y3F   a"etAf3