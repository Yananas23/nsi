from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    """
    a class that parse a document and allow tag access
    :exemples:

    >>> parser = MyHTMLParser("<!DOCTYPE hml><html lang="fr"></html>")
    >>> parser.has_tag()
    True
    >>> parser.next_tag() 
    '<html>'
    >>> parser.next_tag()
    '</html>'
    >>> parser.has_tag()
    False
    """    
    def __init__(self, data):
        """
        constructor for MyHTMLParse
        :param data: (str) html document
        :UC: None
        """
        super().__init__()
        self.__tags = []
        self.__tag_index = 0
        HTMLParser.feed(self, data)

    def handle_starttag(self, tag, attrs):
        """
        handle an opening tag
        :param tag: (str) the opening tag
        :param attrs: (list) attributes
        """
        self.__tags.append('<{:s}>'.format(tag))

    def handle_endtag(self, tag):
        """
        handle an ending tag
        :param tag: (str) the ending tag
        """
        self.__tags.append('</{:s}>'.format(tag))

    def has_tag(self):
        """
        :return: (bool) True if document contains another tag, False otherwise
        """
        return self.__tag_index < len(self.__tags)

    def next_tag(self):
        """
        :return: (str) the next tag in document
        """
        res = self.__tags[self.__tag_index]
        self.__tag_index += 1
        return res

def parser(doc):
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)

