# Créé par yanis.boulogne, le 15/09/2021 en Python 3.7
from turtle import *

couleurs = ['blue', 'green', 'yellow', 'orange', 'red', 'purple']
bgcolor('black')

def dessin():
    for i in range(180):
        color(couleurs[i % 6])
        forward(i)
        right(59)

#dessin()

def dessin_rec(i=0):
    if i == 180 :
        exit()
    else :
        color(couleurs[i % 6])
        forward(i)
        right(59)
        return dessin_rec(i+1)

dessin_rec()