Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
        return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i + 1)


def occurence(lettre, mot):
    nb_lettre = 0
    mot = str.lower(mot)
    for element in mot :
        if element == lettre:
            nb_lettre = nb_lettre + 1
    return nb_lettre
