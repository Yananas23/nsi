def recherche_naive(mot:str, texte:str)->list:
    '''Renvoie un tableau contenant les index du paramètre texte où se trouve le
    paramètre mot.

    :exemple:
    >>> m = "jo"
    >>> t1 = "Bonjour"
    >>> recherche_naive(m, t1) == [3]
    True
    >>> t2 = "Bjoujojoa"
    >>> recherche_naive(m, t2) == [1, 4, 6]
    True
    >>> t3 = "defghjsascj"
    >>> recherche_naive(m, t3) == []
    True
    '''
    long_mot = len(mot)
    long_txt = len(texte)
    position = 0
    res = []
    while long_mot + position < long_txt:
        trouve = True
        for i in range(long_mot):
            if mot[i] != texte[position + i]:
                trouve = False
        if trouve:
            res.append(position)
        position = position + 1
    return res


def recherche_naive2(mot:str, texte:str)->list:
    '''Renvoie un tableau contenant les index du paramètre texte où se trouve le
    paramètre mot.

    :exemple:
    >>> m = "jo"
    >>> t1 = "Bonjour"
    >>> recherche_naive2(m, t1) == [3]
    True
    >>> t2 = "Bjoujojoa"
    >>> recherche_naive2(m, t2) == [1, 4, 6]
    True
    >>> t3 = "defghjsascj"
    >>> recherche_naive2(m, t3) == []
    True
    '''
    long_mot = len(mot)
    long_txt = len(texte)
    position = 0
    res = []
    while long_mot + position < long_txt:
        trouve = True
        i = 0
        while trouve and long_mot > i:
            if mot[i] != texte[position + i]:
                trouve = False
            i = i + 1
        if trouve:
            res.append(position)
        position = position + 1
    return res





if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)
    motif = "ACG"
    brin_adn = "CAAGCGCACAAGACGCGGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTTGCTGTATGTTCCATGGTGGCCAATCCGTCTCTTTTCGACAGCACGGCCAATTCTCCTAGGAAGCCAGCTCAATTTCAACGAAGTCGGCTGTTGAACAGCGAGGTATGGCGTCGGTGGCTCTATTAGTGGTGAGCGAATTGAAATTCGGTGGCCTTACTTGTACCACAGCGATCCCTTCCCACCATTCTTATGCGTCGTCTGTTACCTGGCTTGGCAT"
    print(recherche_naive2(motif, brin_adn))
