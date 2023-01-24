def nbLig(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image)

def nbCol(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(len(image)):
        for j in range(len(image[0])):
            L[i][j] = 255 - image[i][j]
    return L

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil
       et 1 sinon'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


def occurrence_max(chaine):

    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n' ,'o,','p','q','r','s','t','u','v','w','x','y','z']
    occurence=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    texte = []

    for lettre in chaine:
        texte.append(lettre)
    for i in range(len(texte)):
        for j in range(len(alphabet)):
            if texte[i] == alphabet[j]:
                occurence[j] = occurence[j] + 1

    max = occurence[0]
    indice = 0
    liste_max = []

    for k in range(len(occurence)):
        if max < occurence[k]:
            indice = k
            max = occurence[k]

    for l in range(len(occurence)):
        if occurence[l] == max:
            liste_max.append(l)

    lettre_max = []
    for m in range(len(liste_max)):
        lettre_max.append(alphabet[liste_max[m]])
    return lettre_max
