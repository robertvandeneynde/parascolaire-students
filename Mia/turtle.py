from turtle import *
shape("turtle")


def maison(t, c):
  fd(80)  # bas de la maison
  lt(90)
  fd(80)  # mur droit

  lt(30)
  fd(80)
  lt(120)
  fd(80)
  
  lt(120)
  fd(80)  # haut
  lt(180)
  fd(80)
  
  lt(90)
  fd(80)  # mur gauche
  lt(90)
  fd(20)
  lt(90)
 
  color(c) 
  fd(10)  # porte (mur gauche)
  rt(90)
  fd(40)  # porte (haut)
  rt(90)
  fd(10)  # porte (mur droit)

def triangle():
  for i in range(3):  
    fd(20)
    lt(60)






for i in range(6):
  triangle()
  lt()

