# Créé par Yanis Boulogne, le 08/03/2022 en Python 3.7

def d_ord(mot):
    for lettre in mot:
            ascii = ord(lettre)
            print(lettre,ascii)

def d_chr(args):
    for lettre in args:
            ascii = chr(lettre)
            print(lettre,ascii)