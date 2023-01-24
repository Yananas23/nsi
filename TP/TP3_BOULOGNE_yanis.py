# Créé par yanis.boulogne, le 23/02/2022

def taille(arbre, sommet):
    '''
    Permet de connaitre la taille d'un arbre binaire.

    Paramètre:
        arbre (str) ==> Nom du dictionnaire contenant l'arbre binaire.
        sommet (str) ==> Lettre correspondant au sommet de l'arbre binaire.

    renvoie:
        x (int) => Taille de l'arbre binaire.
    '''
    x = 0

    racine = arbre.get(sommet)

    if racine[1] == '':
        x = x + 1
        return taille(arbre, racine[0])
    elif racine[0] == '':
        x = x + 1
        return taille(arbre, racine[1])
    elif racine[0] != '' and racine[1] != '':
        x = x + 1
        return taille(arbre, racine[0]) and taille(arbre, racine[1])
    else :
        return x

    # Erreur 'NoneType' object is not subscriptable


a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],'H':['','']}




def chercher(T, n, i, j):
    if i < 0 or j > len(T) :
        print("ERREUR")
        return None
    if i > j:
        return None
    m = (i + j) // 2
    if T[m] < n:
        return chercher(T, n, m, j)
    elif T[m] > n:
        return chercher(T, n, i, m)
    else :
        return m

    #renvoie n et non l'emplacement de n