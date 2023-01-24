import somme2 as mod1

def seuil(A, q, u):
    '''
    calcule la somme des termes d'une suite géométrique jusqu'à une valeur A,
    passé en paramètre, de premier terme u et de raison q, tous deux passés
    en paramètre.

    paramètre:
    A (float) : valeur que u doit atteidre
    q (float) : raison de la suite
    u (float) : premier terme de la suite

    renvoie :
    (float) : terme de rang n

    exemple :
    >>> seuil(60, 2, 1) == 5
    True
    '''

    assert (q > 1 )
    n = 0
    while mod1.somme(q, u, n) < A :
        n = n + 1
    return n

if __name__ == "__main__" :
    import doctest
    doctest.testmod()