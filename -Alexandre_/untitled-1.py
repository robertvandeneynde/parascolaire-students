alice = Personnage()
alice.vie = 40
alice.max_vie = 70
alice.mana = 50

# imaginez une liste de personnages !
les_personnages = [alice, bob]

alice.vie += 10
print(les_personnages[0].vie)  # 50
print(les_personnage[0] == alice)  # True

p = Personnage()
p.vie = 20
p.max_vie = 20
p.mana = 30

les_personnages.append(p)

p = Personnage()
p.vie = 25
p.max_vie = 25
p.mana = 20

les_personnages.append(p)