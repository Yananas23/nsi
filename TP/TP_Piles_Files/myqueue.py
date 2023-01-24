from collections import deque

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
        self.inside = deque()

    def is_empty(self):
        """
        :return: (bool) True si la queue est vide, False sinon
        """
        return  self.inside == deque()

    def enqueue(self, el):
        """
        enfile un élément dans la file
        :param el: (any) un élément
        """
        return self.inside.append(el)

    def dequeue(self):
        """
        défile un élément
        :return: (any) un élément
        """
        return self.inside.popleft()

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
