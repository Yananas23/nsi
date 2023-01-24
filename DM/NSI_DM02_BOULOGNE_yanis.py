# Créé par yanis.boulogne, le 15/09/2021 en Python 3.7
from turtle import *

couleurs = ['white']
bgcolor('black')

def Koch(n,l):
    color(couleurs)
    if n == 0 :
        forward(l)
    else :
        Koch(n-1,l//3)
        left(60)
        Koch(n-1,l//3)
        right(120)
        Koch(n-1,l//3)
        left(60)
        Koch(n-1,l//3)

'''Koch(3,180)'''

def flocon(n, l) :
	for _ in range(3) :
		Koch(n, l)
		right(120)

flocon(1,300)