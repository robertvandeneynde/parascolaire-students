import random
#! coding: utf-8
# h et m sont deux variables qui représentent une heure
h = 15
m = 30
# ici elles représentent l'heure "15h30"

# Écris un programme qui affiche la minute suivante.
# Ici le programme affichera 15 31
# Mais si l'heure était 15h59 ça doit évidemment afficher 16h00 !
h=random.randint(0,23)
m=random.randint(0,59)
print("Heure avant :",h, 'h ', m,'m')
i = 0
while i<100:
    m=m+1
    if m==60:
        m=0
    print("Heure :",h, 'h ', m,'m')
    i +=1


