def est_descriptif(nombre):
    '''
    Permet de savoir si un nombre passé en paramètre est descriptif.

    Paramètre:
        nombre (int) ==> nombre entier qui passera la vérification.

    Return:
        Booléen ==> True ou False

    Exemple:

    >>> est_descriptif(21200)
    True
    >>> est_descriptif(87)
    False
    '''

    nombre = str(nombre)
    chiffres = {'0': 0, '1': 0, '2':0, '3':0, '4': 0, '5': 0, '6':0, '7':0, '8': 0, '9':0}

    for chiffre in nombre:
        chiffres[str(chiffre)] = chiffres[str(chiffre)] + 1

    nombre_recree = ''
    for key in range(len(nombre)):
        nombre_recree = nombre_recree + str(chiffres[str(key)])

    return int(nombre_recree) == int(nombre)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def sont_descriptif():
    le_sont = []
    for n in range(1000000000):
        if est_descriptif(n) == True:
            le_sont.append(n)
    return le_sont
