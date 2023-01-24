import terme3 as mod1
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
    s = 0
    for _ in range(0, n + 1):
        s = mod1.terme(q, u, _) + s
    return s

if __name__ == "__main__" :
    import doctest
    doctest.testmod()