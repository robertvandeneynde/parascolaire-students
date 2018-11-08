# il affiche le nombre le plus grand de la liste
liste = [1,2,7,2]
if liste[0] >= liste[1] and liste[0] >= liste[2] and liste[0] >= liste[3]:
    m = liste[0]
    print(m)
elif liste[1] >= liste[0] and liste[1] >= liste[2] and liste[1] >= liste[3]:
    m = liste[1]
    print(m)
elif liste[2] >= liste[0] and liste[2] >= liste[1] and liste[2] >= liste[3]:
    m = liste[2]
    print(m)
elif liste[3] >= liste[0] and liste[3] >= liste[1] and liste[3] >= liste[2]:
    m = liste[3]
    print(m)