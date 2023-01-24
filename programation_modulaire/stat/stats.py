# Créé par yanis.boulogne, le 30/09/1837 en Python 3.7
def somme(L):
    '''
    calcule la somme des termes d'une liste passé en paramètre

    paramètre:
        L (list) : contient les valeurs pour le calcul

    renvoi:
        S (float) : somme des valeurs de la liste

    exemple:
    >>> somme([1, 2, 3, 4, 5, 6, 7, 8, 9])
    45
    '''
    S = 0
    for n in range (len(L)):
        S = S + L[n]
    return S

def moyenne(L):
    '''
    calcule la moyenne des termes d'une liste passé en paramètre

    paramètre:
        L (list) : contient les valeurs pour le calcul

    renvoi:
        M (float) : moyenne des valeurs de la liste

    exemple:
    >>> moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9])
    5.0
    '''
    return somme(L)/len(L)

def etendu(L):
    '''
    calcule l'étendu des termes d'une liste passé en paramètre

    paramètre:
        L (list) : contient les valeurs pour le calcul

    renvoi:
        E (float) : étendu des valeurs de la liste

    exemple:
    >>> etendu([1, 2, 3, 4, 5, 6, 7, 8, 9])
    8

    >>> etendu([5, 1, 19, 50, 4, 84, 37, 5, 6])
    83
    '''
    L = sorted(L)
    E = L[-1] - L[0]
    return E

def mediane(L):
    '''
    calcule la médiane des termes d'une liste passé en paramètre

    paramètre:
        L (list) : contient les valeurs pour le calcul

    renvoi:
        D (float) : étendu des valeurs de la liste

    exemple:
    >>> mediane([12, 30, 47])
    30

    >>> mediane([47, 12, 30])
    30

    >>> mediane([1, 10, 30, 47])
    20.0
    '''
    L = sorted(L)
    if len(L) % 2 == 0:
        med1 = L[len(L) // 2]
        med2 = L[(len(L) // 2) - 1]
        D = moyenne([med1, med2])
        return D
    else :
        D = L[len(L)//2]
        return D


if __name__ == "__main__" :
    import doctest
    doctest.testmod()