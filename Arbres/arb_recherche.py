# Créé par yanis.boulogne, le 13/01/2022 en Python 3.7

import Algo_Correction as ac
import binary_tree_sans_Graphviz as bt

def infixe2(A, L=[]):
    '''
    récupère les étiquettes d'un arbres binaire

    paramètre :
        A : un arbre binaire
        L : liste contenant les étiquettes

    renvoie :
        booléen
        '''
    if not A.is_empty():
        infixe2(A.get_left_subtree())
        L.append(A.get_data())
        infixe2(A.get_right_subtree())
        return L

def est_recherche(A, L = []):
    '''
    vérifie si un arbre binaire est un arbre binaire de recherche

    paramètre :
        A : un arbre binaire
        L : liste contenant les étiquettes

    renvoie :
        booléen
    '''
    L = infixe2(A)
    for i in range(len(L)-1):
        if not L[i] < L[i+1]:
            return False
    return True

def est_present1(A, x):
    '''
    vérifie si un arbre binaire poosède une valeur cherché

    paramètre :
        A : un arbre binaire
        x : valeur recherché

    renvoie :
        booléen
    '''
    L = infixe2(A)
    for i in range(len(L)-1):
        if L[i] == x:
            return True
    return False

def est_present2(A, x):
    '''
    vérifie si un arbre binaire poosède une valeur cherché

    paramètre :
        A : un arbre binaire
        x : valeur recherché

    renvoie :
        booléen
    '''
    L = infixe2(A)
    return x in L



A = bt.BinaryTree(17,
                    bt.BinaryTree(4,
                                    bt.BinaryTree(1,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        ),
                                    bt.BinaryTree(12,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        )
                                    ),
                    bt.BinaryTree(25,
                                    bt.BinaryTree(14,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        ),
                                    bt.BinaryTree(29,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        )
                                    )

                    )

B = bt.BinaryTree(1,
                    bt.BinaryTree(2,
                                    bt.BinaryTree(4,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        ),
                                    bt.BinaryTree(5,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        )
                                    ),
                    bt.BinaryTree(3,
                                    bt.BinaryTree(6,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        ),
                                    bt.BinaryTree()
                                    )

                    )

C = bt.BinaryTree(17,
                    bt.BinaryTree(4,
                                    bt.BinaryTree(1,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        ),
                                    bt.BinaryTree(12,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        )
                                    ),
                    bt.BinaryTree(25,
                                    bt.BinaryTree(19,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        ),
                                    bt.BinaryTree()
                                    )

                    )