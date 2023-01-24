from myqueue import Queue

def cherche_balise(doc):
    for i in range(len(doc)):
        if doc[i] == "<":
            B1 = i
            print(B1)
        elif doc[i] == ">":
            B2 = i
            print(B2)
            return (B1,B2)

def parse(doc,B1 = 0, B2 = 0):
    """
    :param doc: (str) a document to be parsed
    :return: (Queue) a queue containing tag (without attributes)
    :CU: None
    :Example:

    >>> q = parse("<!DOCTYPE html><html><div class='titre'>du contenu ignoré</div></html>")
    >>> q.is_empty()
    False
    >>> q.dequeue() == "<html>"
    True
    >>> q.dequeue() == "<div>"
    True
    >>> q.dequeue() == "</div>"
    True
    >>> q.dequeue() == "</html>"
    True
    >>> q.is_empty()
    True
    >>> # Other example
    >>> q = parse("<html><div><p <a")
    >>> q.dequeue() == "<html>"
    True
    >>> q.dequeue() == "<div>"
    True
    >>> q.is_empty()
    True
    """
    File = Queue()
    while ">" in doc:
        B1, B2 = cherche_balise(doc)
        balise = doc[B1: B2 + 1]
        if not('DOCTYPE' in balise):
            index_b = balise.index(" ")
            balise = balise[:-1]
            print(index_b)
            for i in range((index_b) ):
                balise_sans_esp = balise[i]
            balise = balise + '>'
            File.enqueue(balise)

        doc = doc[B2 + 1:]

    return File


def afficher_file(f):
    while not f.is_empty():
        print(f.dequeu())

if __name__ == "__main__":
    import doctest
    doctest.testmod()