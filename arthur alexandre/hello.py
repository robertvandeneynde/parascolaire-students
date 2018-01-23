#! coding: utf-8
# h et m sont deux variables qui représentent une heure
h = 13
m = 59
# ici elles représentent l'heure "15h30"

# Écris un programme qui affiche la minute suivante.
# Ici le programme affichera 15 31
# Mais si l'heure était 15h59 ça doit évidemment afficher 16h00
m=m+1
if m == 60:
    h=h+1
print(h, m)
