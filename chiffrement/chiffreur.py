# Créé par yanis.boulogne, le 07/03/2022 en Python 3.7

def rot13(mot):
    '''
    Permet de chiffré et déchiffrer un mot en décalent de 13.

    Paramètre:
        mot (STR) ==> Mot à chiffrer ou à déchiffrer

    Renvoie:
        N_mot (STR) ==> Mot après chiffrement ou déchiffrement
    '''

    N_mot = ''

    for lettre in mot:
        ascii = ord(lettre)
        print(lettre,ascii)

        if 65 <= ascii <= 90: #majuscule

            if ascii > 78 :

                chiffrage = ascii - 13
                N_lettre = chr(chiffrage)
                N_mot = N_mot + N_lettre

            elif ascii <= 78 :

                chiffrage = ascii + 13
                N_lettre = chr(chiffrage)
                N_mot = N_mot + N_lettre

        elif 97 <= ascii <= 122: #minuscule

            if ascii > 110 :

                chiffrage = ascii - 13
                N_lettre = chr(chiffrage)
                N_mot = N_mot + N_lettre

            elif ascii <= 110 :

                chiffrage = ascii + 13
                N_lettre = chr(chiffrage)
                N_mot = N_mot + N_lettre

        else: #caractère spéciaux

            N_lettre = chr(ascii)
            N_mot = N_mot + N_lettre

    return N_mot


def rot13_bis(mot):
    '''
    Permet de chiffré et déchiffrer un mot en décalent de 13 et en stockant les
    lettres déjà connu dans un dictionnaire.

    Paramètre:
        mot (STR) ==> Mot à chiffrer ou à déchiffrer

    Renvoie:
        N_mot (STR) ==> Mot après chiffrement ou déchiffrement
    '''

    N_mot = ''
    deja_connu={}

    for lettre in mot:

        if lettre in deja_connu:

            N_mot = N_mot + deja_connu[lettre]

        else :
            ascii = ord(lettre)


            if 65 <= ascii <= 90:

                if ascii >= 78 :

                    chiffrage = ascii - 13
                    N_lettre = chr(chiffrage)
                    deja_connu[lettre] = N_lettre
                    N_mot = N_mot + N_lettre

                elif ascii <= 78 :

                    chiffrage = ascii + 13
                    N_lettre = chr(chiffrage)
                    deja_connu[lettre] = N_lettre
                    N_mot = N_mot + N_lettre

            elif 97 <= ascii <= 122:

                if ascii >= 110 :

                    chiffrage = ascii - 13
                    N_lettre = chr(chiffrage)
                    deja_connu[lettre] = N_lettre
                    N_mot = N_mot + N_lettre

                elif ascii <= 110 :

                    chiffrage = ascii + 13
                    N_lettre = chr(chiffrage)
                    deja_connu[lettre] = N_lettre
                    N_mot = N_mot + N_lettre

            else:

                N_lettre = chr(ascii)
                deja_connu[lettre] = N_lettre
                N_mot = N_mot + N_lettre

    return N_mot


def rotN(mot,n):
    '''
    Permet de chiffré et déchiffrer un mot en décalent de 13.

    Paramètre:
        mot (STR) ==> Mot à chiffrer ou à déchiffrer
        n (int) ==> Décalage des lettres

    Renvoie:
        N_mot (STR) ==> Mot après chiffrement ou déchiffrement
    '''

    assert isinstance(n, int) and 0 <= n <= 26, 'Le paramètre doit être compris entre 0 et 26'

    if n == 26 or 0:
        return mot

    else:

        N_mot = ''
        for lettre in mot:
            ascii = ord(lettre)

            if 65 <= ascii <= 90: #majuscule

                if ascii > (90 - n) :

                    chiffrage = ascii - (26 - n)
                    N_lettre = chr(chiffrage)
                    N_mot = N_mot + N_lettre

                elif ascii <= (90 - n) :

                    chiffrage = ascii + n
                    N_lettre = chr(chiffrage)
                    N_mot = N_mot + N_lettre

            elif 97 <= ascii <= 122: #minuscule

                if ascii > (122 - n)  :

                    chiffrage = ascii - (26 - n)
                    N_lettre = chr(chiffrage)
                    N_mot = N_mot + N_lettre

                elif ascii <= (122 - n) :

                    chiffrage = ascii + n
                    N_lettre = chr(chiffrage)
                    N_mot = N_mot + N_lettre

            else: #caractère spéciaux

                N_lettre = chr(ascii)
                N_mot = N_mot + N_lettre

        return N_mot


def rotN_bis(mot,n):
    '''
    Permet de chiffré et déchiffrer un mot en décalent de 13 et stock les
    lettres déjà connu dans un dictionnaire.

    Paramètre:
        mot (STR) ==> Mot à chiffrer ou à déchiffrer
        n (int) ==> Décalage des lettres

    Renvoie:
        N_mot (STR) ==> Mot après chiffrement ou déchiffrement
    '''

    assert isinstance(n, int) and 0 <= n <= 26, 'Le paramètre doit être compris entre 0 et 26'

    if n == 26 or 0:
        return mot

    else:

        N_mot = ''
        deja_connu = {}
        for lettre in mot:
            if lettre in deja_connu:

                N_mot = N_mot + deja_connu[lettre]
            else:
                ascii = ord(lettre)

                if 65 <= ascii <= 90: #majuscule

                    if ascii > (90 - n) :

                        chiffrage = ascii - (26 - n)
                        N_lettre = chr(chiffrage)
                        N_mot = N_mot + N_lettre

                    elif ascii <= (90 - n) :

                        chiffrage = ascii + n
                        N_lettre = chr(chiffrage)
                        N_mot = N_mot + N_lettre

                elif 97 <= ascii <= 122: #minuscule

                    if ascii > (122 - n)  :

                        chiffrage = ascii - (26 - n)
                        N_lettre = chr(chiffrage)
                        N_mot = N_mot + N_lettre

                    elif ascii <= (122 - n) :

                        chiffrage = ascii + n
                        N_lettre = chr(chiffrage)
                        N_mot = N_mot + N_lettre

                else: #caractère spéciaux

                    N_lettre = chr(ascii)
                    N_mot = N_mot + N_lettre

        return N_mot
