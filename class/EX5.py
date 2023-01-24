def vide():
    return tuple()

def cons(x,L):
    return(x,L)

def ajouteEnTete(L,x):
    return cons(x,L)

def supprEnTete(L):
    return(L[0],L[1])

def estVide(L):
    return L is None

def compte(L):
    if estVide(L):
        return 0
    return 1 + compte(L[1])


class Stack():
    def __init__(self):
        self.att = []

    def isEmpty(self):
        return estVide(self)

    def push(self,val):
        self.att.append(val)
        return

    def pop(self):
        x = self.att.pop[-1]
        return

    def sommet(self):
        return self.att[-1]

    def taille(self):
        return compte(self)