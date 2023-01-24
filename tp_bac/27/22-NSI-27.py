def tri_iteratif(tab):
    for k in range( len(tab)-1 , 0, -1):
        imax = k
        for i in range(0 , k):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k] :
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab

def taille(arbre, lettre):
    sous_arbre = arbre[lettre]
    if sous_arbre == ['','']:
        return 1

    else:
        if sous_arbre[0] == '':
            return 1 + taille(arbre,sous_arbre[1])
        elif sous_arbre[1] == '':
            return 1 + taille(arbre,sous_arbre[0])
        else:
            return 1 + taille(arbre,sous_arbre[0]) + taille(arbre,sous_arbre[1])

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}