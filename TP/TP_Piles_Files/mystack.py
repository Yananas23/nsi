from collections import deque

class StackEmptyError(Exception):
    """
    exception pour pile vide
    """
    def __init__(self, msg):
        self.message = msg

class Stack:
    """
    une classe pour manipuler les piles
    """

    def __init__(self):
        """
        constructeur de pile
        """
        self.inside = deque()

    def is_empty(self):
        """
        :return: (bool) True si la pile est vide, False sinon
        :CU: None
        :Exemples:

        >>> p = Stack()
        >>> p.is_empty()
        True
        >>> p.push(1)
        >>> p.is_empty()
        False
        """
        return self.inside == deque()

    def push(self, el):
        """
        :param el: (any) un élément
        :return: None
        :Side-Effet: ajoute un élément au sommet de la pile
        :CU: None

        >>> p = Stack()
        >>> p.push(1)
        >>> p.pop() == 1
        True
        """
        return self.inside.appendleft(el)

    def pop(self):
        """
        :return: (any) l'élément au sommet de la pile
        :CU: la pile ne doit pas être vide
        :raise: StackEmptyError
        :Side-Effect: la pile est modifiée
        :Exemples:

        >>> p = Stack()
        >>> p.push(1)
        >>> p.pop() == 1
        True
        >>> p.is_empty()
        True
        """
        T = self.inside.popleft()
        return T

    def top(self):
        """
        :return: (any) l'élément au sommet de la pile
        :CU: la pile ne doit pas être vide
        :raise: StackEmptyError
        :Exemples:

        >>> p = Stack()
        >>> p.push(1)
        >>> p.top() == 1
        True
        >>> p.is_empty()
        False
        """
        T = self.inside.popleft()
        self.inside.appendleft(T)
        return T

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
