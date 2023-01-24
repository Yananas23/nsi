def tri_selection(L):
    '''
    Permet de trier une liste.

    parametre :
        L (list) : liste à trier

    return:
        L_dans_lordre (list) : liste triée
    '''

    L_dans_lordre = []
    while len(L)!=0:
        mini=L[0]
        print(L,L_dans_lordre)
        for i in range(1,len(L)):
            if L[i]<mini:
                mini=L[i]
        L_dans_lordre.append(mini)
        L.remove(mini)
    return L_dans_lordre

def tri_selection_recu(L, L_dans_lordre):
    '''
    Permet de trier une liste.

    parametre :
        L (list) : liste à trier
        L_dans_lordre (list) : liste triée

    return:
        L_dans_lordre (list) : liste triée
    '''

    mini=L[0]
    print(L,L_dans_lordre)
    for i in range(1,len(L)):
        if L[i]<mini:
            mini=L[i]
    L_dans_lordre.append(mini)
    L.remove(mini)
    if len(L)!= 0:
        return tri_selection_recu(L,L_dans_lordre)
    else:
        return L_dans_lordre

def tri_insertion(L):
    '''
    Permet de trier une liste.

    Paramètres :
        L (list)

    Retturn :
        L_dans_lordre (list) : liste triée
    '''
    print(L)
    for i in range(1, len(L)):
        k = L[i]
        j = i-1
        while j >= 0 and k < L[j] :
                L[j + 1] = L[j]
                j -= 1
        L[j + 1] = k
    return L

def tri_insertion_recu(L):
    '''
    Permet de trier une liste.

    parametre :
        L (list) : liste à trier
        L_dans_lordre (list) : liste triée

    return:
        L_dans_lordre (list) : liste triée
    '''
    print(L)
    for i in range(1, len(L)):
        k = L[i]
        j = i - 1
        while j >= 0 and k < L[j] :
                L[j + 1] = L[j]
                j -= 1
        L[j + 1] = k
    if j == 0:
        j = j - 1
        return tri_insertion_recu(L)
    else:
        return L