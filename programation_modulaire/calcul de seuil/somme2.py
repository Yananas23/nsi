def somme(q, u, n):
    '''
    calcule la somme des termes d'une suite géométrique jusqu'à un rang n,passé
    en paramètre, de premier terme u et de raison q, tous deux passés
    en paramètre.

    paramètre:
    q (float) : raison de la suite
    u (float) : premier terme de la suite
    n (int) : rang du terme à calculer

    renvoie :
    (float) : somme des termes de la suite jusqu'au rang n

    exemple :
    >>> somme(2, 1, 5) == 63
    True
    '''

    if n == 0:
        return u
    else :
        n = n - 1
        u = u + q ** (n + 1 )
        return somme(q, u, n)

if __name__ == "__main__" :
    import doctest
    doctest.testmod()