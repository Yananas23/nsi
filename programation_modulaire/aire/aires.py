from math import *


def disque(rayon):
    '''
    calcul l'aire d'un dique pour un rayon donné, passé en paramètre.

    paramètre:
        rayon (float) = rayon du disque

    renvoi:
        l'aire du disque

    exemple:
    >>> disque(5) == 78.53981633974483
    True
    '''
    return pi * rayon**2


def rectangle(longueur, largueur):
    '''
    calcul l'aire d'un rectangle dont la longueur et la largueur sont passé en
    paramètre.

    paramètres:
        longueur, largueur (float) = longueur de deux cotés consécutifs du
                                     rectangle

    renvoi:
        l'aire du rectangle

    exemple:
    >>> rectangle(5, 6) == 30
    True
    '''
    return longueur * largueur


def carre(cote):
    '''
    calcul l'aire d'un carré dont la longueur du coté est passé en
    paramètre.

    paramètre:
        cote (float) = longueur d'un coté du carré


    renvoi:
        l'aire du carré

    exemple:
    >>> carre(5) == 25
    True
    '''
    return cote * cote


def triangle(base, hauteur):
    '''
    calcul l'aire d'un triangle dont la longueur de la base et de la hauteur
    sont passé en paramètres.

    paramètres:
        base (float) = longueur de la base du triangle
        hauteur (float) = longeur depuis la base jusqu'à un sommet du triangle


    renvoi:
        l'aire du triangle

    exemple:
    >>> triangle(5, 5) == 12.5
    True
    '''
    return 1/2 * base * hauteur


if __name__ == "__main__" :
    import doctest
    doctest.testmod(verbose = True)