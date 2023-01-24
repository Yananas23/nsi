import mystack

class QueueEmptyError(Exception):
    def __init__(msg):
        super().__init__(msg)

class Queue:
    """
    a class representing a queue

    >>> q = Queue()
    >>> q.is_empty()
    True
    >>> q.enqueue(1)
    >>> q.enqueue(2)
    >>> q.is_empty()
    False
    >>> q.dequeue()
    1
    >>> q.dequeue()
    2
    """

    def __init__(self):
        """
        create a new queue
        """
        self.pile_entree = mystack.Stack()
        self.pile_sortie = mystack.Stack()

    def is_empty(self):
        """
        :return: (bool) True si la queue est vide, False sinon
        """
        return self.pile_entree.is_empty() and self.pile_sortie.is_empty()


    def enqueue(self, el):
        """
        enfile un élément dans la file
        :param el: (any) un élément
        """
        return self.pile_entree.push(el)


    def dequeue(self):
        """
        défile un élément
        :return: (any) un élément
        """


        if self.pile_entree.is_empty() and self.pile_sortie.is_empty():
            return None
        elif  not self.pile_sortie.is_empty() :
            return self.pile_sortie.pop()
        else:
            while not self.pile_entree.is_empty():
                el = self.pile_entree.pop()
                self.pile_sortie.push(el)
            return self.pile_sortie.pop()

        #or

        if self.pile_sortie.is_empty():
            while not self.pile_sortie.is_empty():
                self.pile_sortie.push(self.pile_entree.pop())
        return self.pile_sortie.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
