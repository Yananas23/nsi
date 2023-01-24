# Créé par simon.hermy, le 17/03/2022 en Python 3.7
def creer_grille(l, h):

    grille = [ [0, 0, 0],
               [0, 0, 0] ]
    return grille

def hauteur_grille(l, h):
    return h

def largeur_grille(l, h):
    return l


def creer_grille_aleatoire(l, h, p):
    grille_aleatoire = [ [0, 0, 0],
                         [0, 0, 0] ]
    if p == 0:
        return  [[0, 0, 0],[0, 0, 0] ]
    elif p == 1:
        return [[1, 1, 1],[1, 1, 1] ]
    return grille_aleatoire


