def recherche(L,n):
    '''
    Recherche si un entier n, passé en paramètre et présent dans une liste L
    également passé en paramètre.

    paramètre:
        n (int) : entier chercher dans la liste
        L (list) : liste d'entier dans laquelle on cherche n

    return:
        P (int) : renvoie sois la Position de l'entier n dans la liste si il est
                    présent, soit la lngueur de la liste si il n'est pas présent

    exemples:
    >>> recherche([2, 5, 6, 2], 2)
    3

    >>> recherche([1, 5], 4)
    2

    >>> recherche([1, 5, 6, 9], 9)
    3
    '''
    P = 0
    for i in range (len(L)):
        if i == len(L):
            return P
        elif L[0] == n:
            P = P + 1
            return recherche(L, n)
    return i



import math

def distance(point1, point2):
    '''calcule et renvoie la distance entre 2 points'''
    return math.sqrt((point1(0),point2(0)) ** 2 + (point1(1),point2(1)) ** 2)

def plus_courte_distance(tab, depart):
    '''renvoie le point du tableau tab se trouvant à la plus
        courte distance du point de depart.'''
    point = tab[0]
    min_dist = (0,0)
    for i in range (1,depart):
        if distance(tab[i], depart):
            point = tab[i]
            min_dist = tab[i] - depart
    return point


'''if __name__ == '__main__' :
    import doctest
    doctest.testmod(verbose = True)'''