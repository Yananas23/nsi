import binary_tree_sans_Graphviz as bt
import myqueue as qe
import mystack as sk

def largeur_file(A,file = qe.Queue()):
    if not A.is_empty():
        print(A.get_data())
        file.enqueue(A.get_left_subtree())
        file.enqueue(A.get_right_subtree())
        A = file.dequeue()
        largeur_file(A,file)



def largeur_pile(A,pile = sk.Stack()):
    if not A.is_empty():
        print(A.get_data())
        pile.push(A.get_left_subtree())
        pile.push(A.get_right_subtree())
        A = pile.pop()
        largeur_pile(A,pile)



A = bt.BinaryTree(1,
                    bt.BinaryTree(2,
                                    bt.BinaryTree(4,
                                        bt.BinaryTree(),
                                        bt.BinaryTree(7,bt.BinaryTree(),bt.BinaryTree())
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