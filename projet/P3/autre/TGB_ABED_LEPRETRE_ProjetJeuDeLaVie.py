
import random

def creer_grille(nb_element, nb_liste):
    """ fonction de crétion de la grille

    La fonction permet de creer la grille de départ, en prenant en paramètre la
    hauteur qui est le nombre de liste dans la grille et la largeur de la grille
    qui est le nombre d'élément dans chacunes des listes.

    :param:
        nb_element (int)
        nb_liste (int)
    """
    global grille
    grille = []
    for i in range(nb_liste):
        liste = []
        grille.append(liste)
        for i in range(nb_element):
            liste.append(0)

    return grille


def hauteur_grille(grille):
    """
    La fonction renvoie la hauteur qui correspond à la longueur de la grille.

    """
    return len(grille)


def largeur_grille(grille):
    """
    La fonction renvoir la longueur qui est la longueur de la première liste à l'intérieur de la grille
    """
    return len(grille[0])


def creer(l, h, p):
    """
    La fonction crée une grille de hauteur h, largeur l et de probabilité p tous
    les trois passé en paramètre.
    La probabilité p sert à déterminé si l'élément sera à 1 ou un 0

    :paam:
        l (int)
        h (int)
        p (int)
    """
    creer_grille(h, l)
    for i in range(l):
        for j in range(h):
            if random.randint(0, 100) < p * 100:
                grille[i][j] = 1
            else:
                grille[i][j] = 0
        return grille


def voisins_case(grille, abcisse, ordonee):
    """
    La fonction liste le nombre de voisin d'une case donnée à l'aide de son abcisse et de son ordonée
    donné en paramètre

    :param:
        grille (list)
        abcisse (int)
        ordonee (int)
        voisins (list)
        voisin_abcisse (int)
        voisin_ordonee (int)
    """
    global voisins
    voisins = []

    voisin_abcisse = abcisse - 1
    voisin_ordonee = ordonee - 1
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    voisin_abcisse = abcisse - 1
    voisin_ordonee = ordonee
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    voisin_abcisse = abcisse - 1
    voisin_ordonee = ordonee + 1
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    voisin_abcisse = abcisse
    voisin_ordonee = ordonee - 1
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    voisin_abcisse = abcisse
    voisin_ordonee = ordonee + 1
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    voisin_abcisse = abcisse + 1
    voisin_ordonee = ordonee - 1
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    voisin_abcisse = abcisse + 1
    voisin_ordonee = ordonee
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    voisin_abcisse = abcisse + 1
    voisin_ordonee = ordonee + 1
    if 0 <= voisin_abcisse and voisin_abcisse < hauteur_grille(grille) and 0 <= voisin_ordonee and voisin_ordonee < largeur_grille(grille):
        voisins = voisins + [grille[voisin_abcisse][voisin_ordonee]]
    return voisins


def nb_cellule_voisins(grille, absicce, ordonee):
    """
    La fonction aide à déterminé le nombre de voisin d'une case donnée à l'aide de son abcisse et de son ordonée
    donné en paramètre

    :param:
        grille (list)
        abcisse (int)
        ordonee (int)
        voisins (list)
        nb_voisins (int)
    """
    global nb_voisins
    voisins_case(grille, absicce, ordonee)
    nb_voisins = sum(voisins)
    return nb_voisins


def afficher_grille(grille):
    """
    La fonction affiche la grille sous forme d'une chaine de caractèrree remplacant les "1" par "O" et les "0" par "_"

    :param:
        grille (list)
        affichage (str)
    """
    affichage = ''
    for i in range(hauteur_grille(grille)):
        affichage = ''
        for j in range(largeur_grille(grille)):
            if grille[i][j] == 1:
                affichage = affichage + 'O'
            else:
                affichage = affichage + '_'
        print(affichage)


def generation_suivante(grille):
    """
    La fonction affiche la génération suivante c'est à dire qu'elle s'aide de la fonction comptant le nombre de voisin
    et regarde chaque case à l'aide d'une boucle et si il possède 2 voisins ou plus on insère dans une nouvelle grille
    "1" sinon on insère 0puis l'onyaffiche la grille
    """
    global nouvelle_grille
    nouvelle_grille = creer_grille(hauteur_grille(grille), largeur_grille(grille))
    for i in range(hauteur_grille(grille)):
        for j in range(largeur_grille(grille)):
            nb_cellule_voisins(grille, i, j)
            if nb_voisins >= 2:
                nouvelle_grille[i][j] = 1
            else:
                nouvelle_grille[i][j] = 0
    grille = nouvelle_grille
    return afficher_grille(grille)


def evolution_n_generations(grille, n):
    """
    Cette fonction permet de repeter n fois la fonction génération suivante avec de nouveau paramètre
    """
    gene_n = 0
    grille_n = grille
    for i in range(n):
        gene_n = gene_n + 1
        print("\n" + "Génération " + str(gene_n) + "\n")
        generation_suivante(grille_n)
        grille_n = nouvelle_grille
