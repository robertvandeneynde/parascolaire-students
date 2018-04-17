import random
#! coding: utf-8
# a et b sont deux nombres quelquonques
a = 1
b = 2

# Écris ci-dessous un programme qui affiche les deux nombres dans l'ordre croissant
# Ici le programme affichera 1 2
# Mais si on remplace en haut "a = 1" par "a = 5" il devra afficher 2 5 !
a= random.randint(0, 100)
b= 50
if a>b:
    print(b,a)
if a<b:
    print(a,b)
    
