from myqueue import Queue

import re

#Expression régulière
HTML_REGEX = re.compile(
    r"""<                        # commence par un <
(/?\w+)                          # capture le nom du tag (éventuellement avec un slash
(                                # groupe des attributs
 (
  \s+                            # autant d'espace que l'on veut
  \w+                            # suivi d'un mot (nom de l'attribut)
  (
   \s*=\s*                       # un signe égal, entouré d'espaces
   (?:".*?"|'.*?'|[\^'">\s]+)    # valeur de l'attribut : capture de tout ce qui est entre guillemets
  )?                             # valeur optionnelle
 )+                              # autant de couple nom=valeur que l'on veut
 \s*                             # suivi d'éventuelles espaces
 |\s*                            # ou bien pas d'attributs : que des espaces
)                                # fin des attributs
>                                # finit par un >
""", re.VERBOSE)

#Version courte :
'''
HTML_REGEX = re.compile(
        r"""<(/?\w+)((\s+\w+(\s*=\s*(?:".*?"|'.*?'|[\^'">\s]+))?)+\s*|\s*)>""")
'''

#Exemple d'utilisation :
"""
>>> html = '<!DOCTYPE html> <!-- un commentaire --> <html lang="fr-FR">   <body>' +\
        "<h1> Un titre </h1> <p class='code'>  un paragraphe    while i < len(l):" +\
        ' </p> <br/> </body> </html>'
>>> for tag_element in HTML_REGEX.findall(html):
        print(tag_element[0])
html
body
h1
/h1
p
/p
/body
/html
"""


def parse(doc):
    """
    :param doc: (str) a document to be parsed
    :return: (Queue) a queue containing tag (without attributes)
    :CU: None
    :Example:

    >>> q = parse("<!DOCTYPE html><html><div class='titre'>du contenu ignoré</div></html>")
    >>> q.is_empty()
    False
    >>> q.dequeue() == "html"
    True
    >>> q.dequeue() == "div"
    True
    >>> q.dequeue() == "/div"
    True
    >>> q.dequeue() == "/html"
    True
    >>> q.is_empty()
    True
    >>> # Other example
    >>> q = parse("<html><div><p <a")
    >>> q.dequeue() == "html"
    True
    >>> q.dequeue() == "div"
    True
    >>> q.is_empty()
    True
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
