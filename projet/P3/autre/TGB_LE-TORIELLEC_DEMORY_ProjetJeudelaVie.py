import random as r
import time as t

def creer_grille(nb_colonnes, nb_lignes):
    ''' Crée la grille du jeu de la vie de dimensions nb_colonnes et nb_lignes

    Paramètres : nb_colonnes(int)
                 nb_lignes(int)

    Renvoie : grille(list)

    Exemples :
    >>> creer_grille(3, 3)

    >>> creer_grille(5, 5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    '''
    grille = []
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            ligne.append(0)
        grille.append(ligne)
    return grille

def hauteur_grille(grille):
    ''' Renvoie la hauteur de la grille (nombre de colonnes)

    Paramètres : grille(list)

    Renvoie : (int)

    Exemples :
    >>> hauteur_grille([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    3
    >>> hauteur_grille([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    5

    '''
    return len(grille)

def largeur_grille(grille):
    ''' Renvoie la hauteur de la grille (nombre de lignes)

    Paramètres : grille(list)

    Renvoie : (int)

    Exemples :
    >>> largeur_grille([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    3
    >>> largeur_grille([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    4
    '''
    return len(grille[0])

def creer_grille_aleatoire(nb_colonnes, nb_lignes, proba_cellule):
    ''' Crée une grille dont les cases contiennent une cellule selon la probabilité proba_cellule

    Paramètres : nb_colonnes(int)
                 nb_lignes(int)
                 proba_cellule(float)

    Renvoie : grille(list)

    Exemple :
    >>> creer_grille_aleatoire(5, 5, 0.75)
    [[1, 1, 0, 1, 1], [1, 1, 1, 1, 1], [0, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 0, 1, 1, 1]]
    >>> creer_grille_aleatoire(5, 5, 1)
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    '''
    grille = []
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            if cellule_ou_pas(proba_cellule) == True:
                ligne.append(1)
            else:
                ligne.append(0)
        grille.append(ligne)
    return grille

def cellule_ou_pas(proba_cellule):
    ''' Permet de calculer une probabilité comprise dans [0;1] grâce à la fonction random de la bibliothèque random

    Paramètre : proba_cellule(float)

    Renvoie (bool)
    '''
    aleatoire = r.random()
    if aleatoire <= proba_cellule:
        return True
    else:
        return False

def coin_haut_gauche(grille, voisins):
    ''' Vérifie les voisins de la case dans le coin supérieur gauche

    Paramètres : grille(list)
                 voisins(list)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[0][1])
    voisins.append(grille[1][0])
    voisins.append(grille[1][1])
    return voisins

def coin_bas_gauche(grille, voisins):
    ''' Vérifie les voisins de la case dans le coin inférieur gauche

    Paramètres : grille(list)
                 voisins(list)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[(len(grille) - 1) - 1][0])
    voisins.append(grille[(len(grille) - 1) - 1][1])
    voisins.append(grille[(len(grille) - 1)][1])
    return voisins

def bord_gauche(grille, voisins, y, x):
    ''' Vérifie les voisins de la première colonne

    Paramètres : grille(list)
                 voisins(list)
                 y(int)
                 x(int)

    Renvoie : voisins(list)
    '''

    voisins.append(grille[y - 1][0])
    voisins.append(grille[y - 1][1])
    voisins.append(grille[y][1])
    voisins.append(grille[y + 1][0])
    voisins.append(grille[y + 1][1])
    return voisins

def coin_haut_droit(grille, voisins):
    ''' Vérifie les voisins de la case dans le coin supérieur droit

    Paramètres : grille(list)
                 voisins(list)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[0][(len(grille[0]) - 1) - 1])
    voisins.append(grille[1][(len(grille[0]) - 1) - 1])
    voisins.append(grille[1][(len(grille[0]) - 1)])
    return voisins

def coin_bas_droit(grille, voisins, y, x):
    ''' Vérifie les voisins de la case dans le coin inférieur droit

    Paramètres : grille(list)
                 voisins(list)
                 y(int)
                 x(int)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[(len(grille) - 1) - 1][(len(grille[y]) - 1)])
    voisins.append(grille[(len(grille) - 1) - 1][(len(grille[y]) - 1) - 1])
    voisins.append(grille[(len(grille) - 1)][(len(grille[y]) - 1) - 1])
    return voisins

def bord_droit(grille, voisins, y, x):
    ''' Vérifie les voisins de la dernière colonne

    Paramètres : grille(list)
                 voisins(list)
                 y(int)
                 x(int)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[y - 1][x])
    voisins.append(grille[y - 1][x - 1])
    voisins.append(grille[y][x - 1])
    voisins.append(grille[y + 1][x])
    voisins.append(grille[y + 1][x - 1])
    return voisins

def bord_haut(grille, voisins, y, x):
    ''' Vérifie les voisins de la première ligne

    Paramètres : grille(list)
                 voisins(list)
                 y(int)
                 x(int)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[y][x - 1])
    voisins.append(grille[y][x + 1])
    voisins.append(grille[y + 1][x - 1])
    voisins.append(grille[y + 1][x])
    voisins.append(grille[y + 1][x + 1])
    return voisins

def bord_bas(grille, voisins, y, x):
    ''' Vérifie les voisins de la dernière ligne

    Paramètres : grille(list)
                 voisins(list)
                 y(int)
                 x(int)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[y][x - 1])
    voisins.append(grille[y][x + 1])
    voisins.append(grille[y - 1][x - 1])
    voisins.append(grille[y - 1][x])
    voisins.append(grille[y - 1][x + 1])
    return voisins

def milieu(grille, voisins, y, x):    # milieu d'un carré de 3x3
    ''' Vérifie les voisins du milieu de la grille

    Paramètres : grille(list)
                 voisins(list)
                 y(int)
                 x(int)

    Renvoie : voisins(list)
    '''
    voisins.append(grille[y][x - 1])
    voisins.append(grille[y][x + 1])
    voisins.append(grille[y - 1][x - 1])
    voisins.append(grille[y - 1][x])
    voisins.append(grille[y - 1][x + 1])
    voisins.append(grille[y + 1][x - 1])
    voisins.append(grille[y + 1][x])
    voisins.append(grille[y + 1][x + 1])
    return voisins

def voisins_case(grille, y, x):
    ''' Vérifie toutes les cases voisines d'une case donnée de coordonnées x et y

    Paramètres : grille(list)
                 y(int)
                 x(int)

    Renvoie : (list)

    Exemples:
    >>> voisins_case(grille, 1, 1)
    [1, 0, 0, 1, 0, 1, 1, 1]
    >>> voisins_case(grille, 2, 2)
    [0, 0, 1]
    '''
    voisins = []
    bord_droit_2 = (len(grille[y]) - 1)
    if x == 0:
        if y == 0:
            return coin_haut_gauche(grille, voisins)
        elif y == (len(grille) - 1):
            return coin_bas_gauche(grille, voisins)
        else:
            return bord_gauche(grille, voisins, y, x)
    elif x == bord_droit_2:
        if y == 0:
            return coin_haut_droit(grille, voisins)
        elif y == (len(grille) - 1):
            return coin_bas_droit(grille, voisins, y, x)
        else:
            return bord_droit(grille, voisins, y, x)
    else:
        if y == 0:
            return bord_haut(grille, voisins, y, x)
        elif y == len(grille) - 1:
            return bord_bas(grille, voisins, y, x)
        else:
            return milieu(grille, voisins, y, x)


def nb_cellules_voisines(grille, y, x):
    ''' Calcule le nombre de cellules voisines d'une case donnée de coordonnées y et x

    Paramètres : grille(list)
                 y(int)
                 x(int)

    Renvoie : cellules_voisines(int)

    Exemples :
    >>> nb_cellules_voisines([[0, 1, 0], [1, 0, 0], [1, 1, 1]], 1, 1)
    5
    >>> nb_cellules_voisines(grille, 0, 0)
    3
    '''
    voisins = voisins_case(grille, y, x)
    cellules_voisines = 0
    for i in voisins:
        if i == 1:
            cellules_voisines = cellules_voisines + 1
    return cellules_voisines

def affichage_grille(grille):
    ''' Affiche la grille du jeu de la vie en remplaçant la valeur 0 par '_' et la valeur 1 par 'O'

    Paramètres : grille(list)

    Renvoie : txt(str)

    Exemples :
    >>> affichage_grille([[1, 1, 1], [1, 1, 1], [0, 1, 0]])
    O O O
    O O O
    _ O _
    >>> affichage_grille([[1, 0, 0], [0, 1, 0], [0, 1, 0]])
    O _ _
    _ O _
    _ O _
    '''
    for lignes in range(len(grille)):
        txt = ''
        for symbole in grille[lignes]:
            if symbole == 0:
                txt = txt + '_ '
            elif symbole == 1:
                txt = txt + 'O '
        print(txt)


def generation_suivante(grille):
    ''' Calcule la génération suivante d'une grille du jeu de la vie entrée en paramètre

    Paramètre : grille(list)

    Renvoie : (str)

    '''
    grille_nouvelle = []
    for i in range(len(grille)):
        grille_nouvelle.append([])
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if nb_cellules_voisines(grille, i, j) == 3:
                grille_nouvelle[i].append(1)
            elif nb_cellules_voisines(grille, i, j) < 2:
                grille_nouvelle[i].append(0)
            elif nb_cellules_voisines(grille, i, j) == 2:
                grille_nouvelle[i].append(grille[i][j])
            elif nb_cellules_voisines(grille, i, j) > 3:
                grille_nouvelle[i].append(0)
    return grille_nouvelle

def evolution_n_generations(grille, n):
    ''' Calcule les n prochaines générations d'une grille du jeu de la vie entrée en paramètre

    Paramètres : grille(list)
                 n(int)

    Renvoie : (list)

    Exemples :
        >>> evolution_n_generations([[1, 1, 1], [0, 1, 1], [1, 0, 0]], 3)
        [[1, 1, 1], [0, 1, 1], [1, 0, 0]]
        [[1, 0, 1], [0, 0, 1], [0, 1, 0]]
        [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
        [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        >>> evolution_n_generations([[1, 1, 1], [0, 1, 1], [1, 0, 0]], 2)
        [[1, 1, 1], [0, 1, 1], [1, 0, 0]]
        [[1, 0, 1], [0, 0, 1], [0, 1, 0]]
        [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
    '''
    if n == 0:
        t.sleep(1)
        print(grille)
        t.sleep(1)
        return grille
    if n == 1:
        t.sleep(1)
        print(grille)
        t.sleep(1)
        return generation_suivante(grille)
    else:
        t.sleep(1)
        print(grille)
        t.sleep(1)
        return evolution_n_generations(generation_suivante(grille), n - 1)
