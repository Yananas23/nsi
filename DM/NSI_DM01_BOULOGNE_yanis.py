# Créé par Yanis Boulogne, le 13/09/2021 en Python 3.7
import random

def vérif(x, y, L, L6=[]):
    '''
    vérifier que L est une liste
    '''
    assert isinstance(L,str)
    L=L.split(',')
    return transcrit(x, y, L, L6=[])

#exercice 1
def estADN(L,L2=["A","C","G","T"]):
    '''
    vérifier la présence de certain caractère
    '''
    if not(L):
        return True
    a = L.pop(0)
    if a not in L2:
        return False
    else :
        return estADN(L,L2)

#exercice 2
def genereADN(x):
    '''
    génére une séquence ADN avec un nombre non défini de terme
    '''
    L3=["A","C","G","T"]
    L4=[]
    for i in range (x):
        L4.append(random.choice(L3))
    return ("".join(L4))

#exercice 3
def baseComplementaire(L5,N):
    '''
    transforme la séquence ADN en ARN et inversement
    '''
    if N == "ARN":
        if 'A' in L5:
            return 'U'
        elif 'C' in L5:
            return 'G'
        elif 'G' in L5:
            return "C"
        elif 'T' in L5:
            return "A"
    elif N == "ADN" :
        if "U" in L5:
            return 'A'
        elif "C" in L5:
            return 'G'
        elif "G" in L5:
            return "C"
        elif "A" in L5:
            return "T"
    else :
        return

#exercice 4
def transcrit( x, y, L, L6=[]):
    '''
    change une liste ADN en son ARN et en prends une partie choisie
    '''
    L5 = L[x]
    if x == y:
        L6.append(baseComplementaire(L5,"ARN"))
        return L6
    else :
        L6.append(baseComplementaire(L5,"ARN"))
        return transcrit( x+1, y, L,L6)

#exercice 5
code_genetique = {
'UUU' : "F", 'UUC' : 'F',
'UUA' : 'L', 'UUG' : 'L', 'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L',
'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I',
'AUG' : 'M',
'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V',
'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S', 'AGU' : 'S', 'AGC' : 'S',
'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P',
'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T',
'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A',
'UAU' : 'Y', 'UAC' : 'Y',
'UAA' : '*', 'UAG' : '*', 'UGA' : '*',
'CAU' : 'H', 'CAC' : 'H',
'CAA' : 'Q', 'CAG' : 'Q',
'AAU' : 'N', 'AAC' : 'N',
'AAA' : 'K', 'AAG' : 'K',
'GAU' : 'D', 'GAC' : 'D',
'GAA' : 'E', 'GAG' : 'E',
'UGU' : 'C', 'UGC' : 'C',
'UGG' : 'W',
'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGA' : 'R', 'AGG' : 'R',
'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G'}
