# il affiche le nombre le plus grand de la liste
liste = [1,2,7,2]
if liste[0] > liste[1]:
    m = liste[0]
elif liste[1] > liste[0]:
    m = liste[1]

if m < liste[2]:
    m =liste[2]

if m < liste[3]:    
    m = liste[3]
    