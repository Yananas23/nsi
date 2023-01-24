

def creer_grille(lignes, colones):
    """
    """
    grille= [[]]* lignes
    for lignes in range(lignes):
        grille[lignes]= [0] * colones
    return grille


def hauteur_grille(lignes,colones):
    """
    """
    return colones

def largeur_grille(lignes,colones):
    """
    """
    return lignes

def creer_grille_aleatoire(lignes, colones, p):
    """
    """
    grille= [[]]* lignes
    for lignes in range(lignes):
        grille[lignes]= [0] * colones * p

    return grille





