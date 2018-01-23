ma_liste =[1,2,1,2]
del ma_liste[3]
print(ma_liste)
ma_liste.append(5)
print(ma_liste[2])
# écrire d'abord un code ne marchant que avec des listes de taille 4
# ensuite utilisez un while pour permettre une liste de n'importe quelle taille
# rappel : len(l) donne la taille de la liste

i=3
print(ma_liste[i])
i=0
while i<len(ma_liste):
    print(ma_liste[i])
    i=i+1

