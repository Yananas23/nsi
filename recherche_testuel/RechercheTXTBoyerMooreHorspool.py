def recherche_bmh(motif:str, txt:str)->list:
    """Renvoie un tableau contenant les index du paramètre texte où se trouve le
    paramètre mot selon l'algorithme de Boyer-Moore-Horspool.
    """
    long_motif = len(motif)
    long_texte = len(txt)
    tab_car = [-1] * 256
    for i in range(long_motif):
        tab_car[ord(motif[i])] = i
    decalage = 0
    res = []
    while(decalage <= long_texte - long_motif):
        j = long_motif - 1
        while j >= 0 and motif[j] == txt[decalage + j]:
            j = j - 1
        if j < 0:
            res.append(decalage)
            if decalage + long_motif < long_texte :
                decalage = decalage + long_motif - tab_car[ord(txt[decalage + long_motif])]
            else :
                decalage = decalage + 1
        else:
            decalage = decalage + max(1, j - tab_car[ord(txt[decalage + j])])
    return res



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)
    motif = "ACCTTCG"
    texte = "CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGGCGATGATTTCGAACCTACTAGTGGGTCTCTTAGGCCGAGCGGTTCCGAGAGATAGTGAAAGATGGCTGGGCTGTGAAGGGAAGGAGTCGTGAAAGCGCGAACACGAGTGTGCGCAAGCGCAGCGCCTTAGTATGCTCCAGTGTAGAAGCTCCGGCGTCCCGTCTAACCGTACGCTGTCCCCGGTACATGGAGCTAATAGGCTTTACTGCCCAATATGACCCCGCGCCGCGACAAAACAATAACAGTTT"
    print(recherche_bmh(motif,texte))