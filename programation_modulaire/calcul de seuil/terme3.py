def terme(q, u, n):
    '''
    calcule le terme de rang n, passé en paramètre, d'une suite géométrique de
    premier terme u et de raison q, tous deux passés en paramètre.

    paramètre:
    q (float) : raison de la suite
    u (float) : premier terme de la suite
    n (int) : rang du terme à calculer

    renvoie :
    (float) : terme de rang n

    exemple :
    >>> terme(2, 1, 5) == 32
    True
    '''
    u= u * q ** n
    return u

if __name__ == "__main__" :
    import doctest
    doctest.testmod()