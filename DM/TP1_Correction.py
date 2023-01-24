def recherche(tab, n):
    '''
    Renvoie la dernière occurence de l'élément n dans tab.
    Renvoie la longueur de tab si n n'appartient pas à tab.
    :param:
        tab (list) : tableau d'entiers
        n (int) : entier à chercher dans tab
    :return:
        (int)
    >>> recherche([9, 45, 12], 45) == 1
    True
    >>> recherche([45, 45, 12], 45) == 1
    True
    >>> recherche([45, 45, 12], 45) == 0
    False
    >>> recherche([45, 9, 12], 87) == 3
    True
    '''
    derniere_occurence = len(tab)
    for indice in range(len(tab)):
        if tab[indice] == n:
            derniere_occurence = indice
    return derniere_occurence

def recherche_rec(tab, n, indice = 0, derniere_occurence = len(tab)):
    if indice == len(tab):
        return derniere_occurence
    elif tab[indice] == n:
        derniere_occurence = indice
        indice = indice + 1
        return recherche_rec(tab, n, indice, derniere_occurence)
    else:
        indice = indice + 1
        return recherche_rec(tab, n, indice, derniere_occurence)


import math

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def plus_courte_distance(tab, depart):
    point = tab[0]
    min_dist = distance(depart, tab[0])
    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point














