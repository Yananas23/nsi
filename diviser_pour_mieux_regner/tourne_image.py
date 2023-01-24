#Yanis.Boulogne 26/01/2022

from matplotlib.pyplot import *

def rotation_droite(t):
    '''
    Fais tourner une image de 90 degrés vers la droite.

    paramètre:
        t (list) : tableau de triplet

    renvoie:
        t2 (list) : nouvelle tableau de triplet
    '''
    dim = len(t)
    if dim == 1:
        return t
    else:
        A = rotation_droite([[t[i][j] for j in range(dim // 2)] for i in range(dim // 2)])
        B = rotation_droite([[t[i][j] for j in range(dim // 2, dim)] for i in range(dim // 2)])
        C = rotation_droite([[t[i][j] for j in range(dim // 2, dim)] for i in range(dim // 2, dim)])
        D = rotation_droite([[t[i][j] for j in range(dim // 2)] for i in range(dim // 2, dim)])
        t2 = []
        for i in range(dim // 2):
            t2.append([D[i][j] for j in range(dim // 2)] + [A[i][j] for j in range(dim // 2)])
        for i in range(dim // 2):
            t2.append([C[i][j] for j in range(dim // 2)] + [B[i][j] for j in range(dim // 2)])
        return t2

def rotation_gauche(t):
    '''
    Fais tourner une image de 90 degrés vers la gauche.

    paramètre:
        t (list) : tableau de triplet

    renvoie:
        t2 (list) : nouvelle tableau de triplet
    '''
    dim = len(t)
    if dim == 1:
        return t
    else:
        A = rotation_gauche([[t[i][j] for j in range(dim // 2)] for i in range(dim // 2)])
        B = rotation_gauche([[t[i][j] for j in range(dim // 2, dim)] for i in range(dim // 2)])
        C = rotation_gauche([[t[i][j] for j in range(dim // 2, dim)] for i in range(dim // 2, dim)])
        D = rotation_gauche([[t[i][j] for j in range(dim // 2)] for i in range(dim // 2, dim)])
        t2 = []
        for i in range(dim // 2):
            t2.append([B[i][j] for j in range(dim // 2)] + [C[i][j] for j in range(dim // 2)])
        for i in range(dim // 2):
            t2.append([A[i][j] for j in range(dim // 2)] + [D[i][j] for j in range(dim // 2)])
        return t2

def inverser(t):
    '''
    Retourne une image.

    paramètre:
        t (list) : tableau de triplet

    renvoie:
        t2 (list) : nouvelle tableau de triplet
    '''
    dim = len(t)
    if dim == 1:
        return t
    else:
        A = inverser([[t[i][j] for j in range(dim // 2)] for i in range(dim // 2)])
        B = inverser([[t[i][j] for j in range(dim // 2, dim)] for i in range(dim // 2)])
        C = inverser([[t[i][j] for j in range(dim // 2, dim)] for i in range(dim // 2, dim)])
        D = inverser([[t[i][j] for j in range(dim // 2)] for i in range(dim // 2, dim)])
        t2 = []
        for i in range(dim // 2):
            t2.append([C[i][j] for j in range(dim // 2)] + [D[i][j] for j in range(dim // 2)])
        for i in range(dim // 2):
            t2.append([B[i][j] for j in range(dim // 2)] + [A[i][j] for j in range(dim // 2)])
        return t2

def tourne(name,x):
    '''
    Permet de faire tourner une image.

    paramètre :
        name (str) : nom de l'image.
        x (int) : numéro du procéder(1 ==> rotation_droite
                                     2 ==> rotation_gauche
                                     3 ==> inverser )

    renvoie :
        None
    '''
    image = imread(name+'.png')

    if x == 1:
        imshow(rotation_droite(image))
        show()

    elif x == 2:
        imshow(rotation_gauche(image))
        show()

    elif x == 3:
        imshow(inverser(image))
        show()

    else:
        return 'x est invalide'