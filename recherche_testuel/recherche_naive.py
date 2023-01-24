# Créé par yanis.boulogne, le 27/04/2022 en Python 3.7

def recherche_naive(texte:str,motif:str):
    '''
    Permet de trouver un motif de lettre passé en paramètre dans
    texte passé en paramètre.

    Paramètre:
        texte (str) => Texte où rechercher le motif.
        motif (str) => Motif à rechercher dans le texte.

    Return:
        place (list) => liste des positions du motif dans le texte.

    Exemple:
    >>> recherche_naive('bonjour','jo')
    [3]
    >>> recherche_naive('dsfghj','jo')
    []
    '''

    i = 0
    place = []
    while len(motif) + i < len(texte):
        trouve = True
        for j in range(len(motif)):

            if motif[j] != texte[i + j]:
                trouve = False

        if trouve:
            place.append(i)
        i = i + 1

    return place


if __name__ == '__main__':
    import doctest
    doctest.testmod()
