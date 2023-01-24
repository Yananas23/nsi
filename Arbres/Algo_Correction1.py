# Créé par yanis.boulogne, le 12/01/1922 en Python 3.7

import binary_tree_sans_Graphviz as bt

def taille(A):
    '''Renvoie la taille d'un arbre passé en paramètres
    '''
    if A.is_empty():
        return 0
    #elif A.is_leaf():
    #    return 1
    else:
        return 1 + taille(A.get_left_subtree())+ taille(A.get_right_subtree())


def hauteur(A):
    '''Renvoie la hauteur d'un arbre passé en paramètres
    '''
    if A.is_empty():
        return -1
    #elif A.is_leaf():
    #    return 0
    else:
        return 1 + max(hauteur(A.get_left_subtree()), hauteur(A.get_right_subtree()))


def prefixe(A):
    '''Affiche le parcours préfixe de l'arbre passé en paramètre
    '''
    if not A.is_empty():
        print(A.get_data())
        prefixe(A.get_left_subtree())
        prefixe(A.get_right_subtree())

def infixe(A):
    '''Affiche le parcours postfixe de l'arbre passé en paramètre
    '''
    if not A.is_empty():
        infixe(A.get_left_subtree())
        print(A.get_data())
        infixe(A.get_right_subtree())

def postfixe(A):
    '''Affiche le parcours infixe de l'arbre passé en paramètre
    '''
    if not A.is_empty():
        postfixe(A.get_left_subtree())
        postfixe(A.get_right_subtree())
        print(A.get_data())



A = bt.BinaryTree(1,
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

