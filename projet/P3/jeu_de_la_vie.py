from random import randint
from time import sleep
from copy import *

def creer_grille(colonne, ligne):
    '''
    Permet de créer une grille vide de hauteur et largeur paramétrable.

    Paramètre:
        colonne (INT) ==> Nombre de valeur dans les lignes de la grille.
        ligne (INT) ==> Nombre de tableau dans la grille.

    Return:
        L (LIST) ==> Grille rempli de 0.
    '''
    L = []
    L1 = []

    for i in range(colonne):
        L1.append(0)

    for i in range(ligne):
        L.append(L1)

    return L


def hauteur_grille(grille):
    '''
    Donne la hauteur d'une grille passé en paramètre.

    Paramètre:
        grille (LIST) ==> Tableau de tableau.
    Return:
        Nombre de tableau dans grille.
    '''
    return len(grille)


def largeur_grille(grille):
    '''
    Donne la largeur d'une grille passé en paramètre.

    Paramètre:
        grille (LIST) ==> Tableau de tableau.
    Return:
        Nombre valeur dans chaque tableau de la grille.
    '''
    return len(grille[0])


def creer_grille_aleatoire(colonne, ligne, chiffre):
    '''
    Permet de créer aléatoirement une grille avec le nombre de colonnes et
    lignes voulu passé en paramètre ainsi que comment elle sera rempli.

    Paramètre:
        colonne (INT) ==> Nombre de valeur dans les lignes de la grille.
        ligne (INT) ==> Nombre de tableau dans la grille.
        chiffre (INT) ==> Valeurs permetant de remplir la grille.

    Return:
        L (LIST) ==> Grille rempli de 0, 1 ou des 2.
    '''
    L = []
    L1 = []

    if chiffre == 0:

        for i in range(colonne):
            L1.append(0)

        for i in range(ligne):
                L.append(L1)


    elif chiffre == 1:
        for i in range(colonne):
            L1.append(1)

        for i in range(ligne):
                L.append(L1)


    else :
            for i in range(colonne):
                Li = []

                for i in range(ligne):
                    x = randint(0,1)
                    Li.append(x)

                L.append(Li)

    return L


def voisins_case(grille, colonne, ligne):
    '''
    Permet de connaitre chaque voisins d'une cellule de la grille.

    Paramètre:
        grille (LIST) ==> Tableau de tableau où chercher les voisins d'une cellule de la grille.
        colonne (INT) ==> Placement d'une cellule dans les lignes de la grille.
        ligne (INT) ==> Tableau où se trouve une cellule dans la grille.

    Return:
        Voisins (LIST) ==> Liste contenant tous les voisins d'une cellule de la grille.
    '''
    Voisins = []

    if ligne == 0 and colonne == 0:
        Voisins.append(grille[ligne + 1][colonne])
        Voisins.append(grille[ligne][colonne + 1])
        Voisins.append(grille[ligne + 1][colonne + 1])
        return Voisins

    elif ligne == hauteur_grille(grille) - 1 and colonne == 0:
        Voisins.append(grille[ligne - 1][colonne])
        Voisins.append(grille[ligne - 1][colonne + 1])
        Voisins.append(grille[ligne][colonne + 1])
        return Voisins

    elif ((ligne !=0 and ligne != hauteur_grille(grille) - 1) and colonne == 0):
        Voisins.append(grille[ligne - 1][colonne])
        Voisins.append(grille[ligne - 1][colonne + 1])
        Voisins.append(grille[ligne][colonne + 1])
        Voisins.append(grille[ligne + 1][colonne])
        Voisins.append(grille[ligne + 1][colonne + 1])
        return Voisins

    if ligne == 0 and colonne == largeur_grille(grille) - 1:
        Voisins.append(grille[ligne][colonne - 1])
        Voisins.append(grille[ligne + 1][colonne - 1])
        Voisins.append(grille[ligne + 1][colonne])
        return Voisins

    elif ligne == hauteur_grille(grille) - 1 and colonne == largeur_grille(grille) - 1:
        Voisins.append(grille[ligne - 1][colonne])
        Voisins.append(grille[ligne - 1][colonne - 1])
        Voisins.append(grille[ligne][colonne - 1])
        return Voisins

    elif ((ligne !=0 and ligne != hauteur_grille(grille) - 1) and colonne == largeur_grille(grille) - 1):
        Voisins.append(grille[ligne - 1][colonne - 1])
        Voisins.append(grille[ligne - 1][colonne])
        Voisins.append(grille[ligne][colonne - 1])
        Voisins.append(grille[ligne + 1][colonne - 1])
        Voisins.append(grille[ligne + 1][colonne])
        return Voisins

    elif (ligne == 0 and (colonne != largeur_grille(grille) - 1 and colonne != 0)):
        Voisins.append(grille[ligne][colonne - 1])
        Voisins.append(grille[ligne][colonne + 1])
        Voisins.append(grille[ligne + 1][colonne - 1])
        Voisins.append(grille[ligne + 1][colonne])
        Voisins.append(grille[ligne + 1][colonne + 1])
        return Voisins

    elif (ligne == hauteur_grille(grille) - 1 and (colonne != largeur_grille(grille) - 1 and colonne != 0)):
        Voisins.append(grille[ligne - 1][colonne - 1])
        Voisins.append(grille[ligne - 1][colonne])
        Voisins.append(grille[ligne - 1][colonne + 1])
        Voisins.append(grille[ligne][colonne - 1])
        Voisins.append(grille[ligne][colonne + 1])
        return Voisins

    else:
        Voisins.append(grille[ligne - 1][colonne - 1])
        Voisins.append(grille[ligne - 1][colonne])
        Voisins.append(grille[ligne - 1][colonne + 1])
        Voisins.append(grille[ligne][colonne - 1])
        Voisins.append(grille[ligne][colonne + 1])
        Voisins.append(grille[ligne + 1][colonne - 1])
        Voisins.append(grille[ligne + 1][colonne])
        Voisins.append(grille[ligne + 1][colonne + 1])
        return Voisins


def nb_cellules_voisins(grille, colonne, ligne):
    '''
    Permet de connaitre le nombre de voisins d'une cellule de la grille.

    Paramètre:
        grille (LIST) ==> Tableau de tableau où chercher les voisins d'une cellule de la grille.
        colonne (INT) ==> Placement d'une cellule dans les lignes de la grille.
        ligne (INT) ==> Tableau où se trouve une cellule dans la grille.

    Return:
        nb_voisins (INT) ==> Nombre de voisins d'une cellule de la grille.
    '''
    nb_voisins = 0
    Voisins = voisins_case(grille, colonne, ligne)

    for i in range(len(Voisins)):

        if Voisins[i] == 1 :
            nb_voisins = nb_voisins + 1

    return nb_voisins


def afficher_grille(grille):
    '''
    Permet d'afficher une grille pour connaitre les cellules en vie et les cellules mortes.

    Paramètre:
        grille (LIST) ==> Tableau de tableau qui sera affiché.

    Return :
        None

    Effets de bord :
        Modifie la console.
    '''
    for i in range(hauteur_grille(grille)):
        for j in range(largeur_grille(grille)):

            if grille[i][j]==1:
                print('O ',end='')

            elif grille[i][j]==0:
                print('_ ',end='')

        print('')


def generation_suivante(grille):
    '''
    Permet d'avancer d'une génération la grille passé en paramètre.

    Paramètre :
        grille (LIST) ==> Grille qui servira pour passer une génération.

    Return :
        grille (LIST) ==> Nouvelle génération de l'ancienne grille.
    '''
    nouvelle_grille = deepcopy(grille)

    for i in range(hauteur_grille(grille)):
        for j in range(largeur_grille(grille)):

            nb_voisins = nb_cellules_voisins(nouvelle_grille, i, j)

            if nb_voisins <= 2 or nb_voisins > 3:
                grille[j][i] = 0

            else:
                grille[j][i] = 1
    return grille


def evolution_n_generations(grille,n):
    '''
    Permet d'avancer de plusieurs génération la grille passé en paramètre.

    Paramètre :
        grille (LIST) ==> Grille qui servira pour passer une génération.
        n (INT) ==> Nombre de nouvelle génération de la grille.

    Return :
        None
    '''
    for i in range(n):
        generation_suivante(grille)
        afficher_grille(grille)
        sleep(1)
    return


