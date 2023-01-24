def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant
    à un plan d'envoi de messages entre `N` personnes A, B, C,
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon.
    '''
    personne = 'A'
    N = len(plan)
    for i in range(N - 1):
        if plan[personne] == 'A':
            return False
        else:
            personne = plan[personne]
    return True

def correspond(mot,mot_a_trous):
    ok = True
    for elt in range(len(mot)):
        if mot[elt] == mot_a_trous[elt] or mot[elt] == "*":
            ok = True
        else :
            ok = False
    return ok