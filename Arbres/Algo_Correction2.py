import binary_tree_sans_Graphviz as bt
import myqueue, mystack

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

def largeur(A, file = myqueue.Queue()):
    '''Affiche le parcours en largeur de l'arbre passé en paramètre
    '''
    if A.is_empty():
        if file.is_empty():
            return None
        else:
            A = file.dequeue()
            largeur(A, file)
    else:
        print(A.get_data())
        file.enqueue(A.get_left_subtree())
        file.enqueue(A.get_right_subtree())
        A = file.dequeue()
        largeur(A, file)

def parcours(A, pile = mystack.Stack()):
    '''Affiche le parcours en largeur de l'arbre passé en paramètre
    '''
    if A.is_empty():
        if pile.is_empty():
            return None
        else:
            A = pile.pop()
            parcours(A, pile)
    else:
        print(A.get_data())
        pile.push(A.get_right_subtree()) # On a inverser cette ligne avec la suivante
        pile.push(A.get_left_subtree()) # On obtient ainsi un parcours préfixe
        A = pile.pop()
        parcours(A, pile)

def infixe2(A, res = []):
    '''Renvoie la liste des étiquette de l'arbre passé en paramètre.
    '''
    if A.is_empty():
        return res
    else:
        infixe2(A.get_left_subtree(), res)
        res.append(A.get_data())
        infixe2(A.get_right_subtree(), res)
        return res

def est_abr(A):
    '''Renvoie un booléen selon si l'arbre passé en paramètre est un ABR ou non.
    '''
    etiq_lst = infixe2(A)
    for indice in range(len(etiq_lst) - 1):
        if etiq_lst[indice] > etiq_lst[indice + 1]:
            return False
    return True








def appartient(A, val):
    '''Renvoie un booléen selon si le second paramètre est une étiquette du
    premier paramètre.
    '''
    etiq_lst = infixe2(A)
    return val in etiq_lst

def appartient2(ABR, val, rep = False):
    '''Renvoie un booléen selon si le second paramètre est une étiquette du
    premier paramètre.
    '''
    if ABR.is_empty():
        return rep
    elif ABR.get_data() == val:
        rep = True
        return rep
    elif ABR.get_data() > val:
        return appartient2(ABR.get_left_subtree(), val, rep)
    else:
        return appartient2(ABR.get_right_subtree(), val, rep)




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

ABR = bt.BinaryTree(17,
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
                                    bt.BinaryTree(29,
                                        bt.BinaryTree(),
                                        bt.BinaryTree()
                                        )
                                    )

                    )