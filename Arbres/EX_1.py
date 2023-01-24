import binary_tree_sans_Graphviz  as bt


def Taille(A):
    if A.is_empty():
        return 0
    else:
        return 1 + Taille(A.get_left_subtree()) + Taille(A.get_right_subtree())

def Hauteur(A):
    if A.is_empty():
        return 0
    else:
        return 1 + max(Taille(A.get_left_subtree()) , Taille(A.get_right_subtree()))

def Prefixe(A):
    if not A.is_empty():
        print(A.get_data())
        Prefixe(A.get_left_subtree())
        Prefixe(A.get_right_subtree())

'''def Prefixe2(A,etiq=[]):
    etiq.append(A.get_data())
    etiq = Prefixe2(A.get_left_subtree,etiq)
    etiq = Prefixe2(A.get_right_subtree,etiq)
    return etiq'''

def Infixe(A):
    if not A.is_empty():
        Infixe(A.get_left_subtree())
        print(A.get_data())
        Infixe(A.get_right_subtree())

def Postfixe(A):
    if not A.is_empty():
        Postfixe(A.get_left_subtree())
        Postfixe(A.get_right_subtree())
        print(A.get_data())