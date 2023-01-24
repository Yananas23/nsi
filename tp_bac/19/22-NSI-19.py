def chercher(T,n,i,j):
    if i < 0 or j > len(T) :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i+j) // 2
    if T[m] < n :
        return chercher(T, n, i , m)
    elif T[m] > n :
        return chercher(T, n, m , j )
    else :
        return m

def multiplication(n1,n2):
    produit  = 0
    if n1 == 0 or n2 == 0: #l'un ou l'autre est égale à 0
        return produit


    elif n1 < 0 and n2 < 0: #les deux sont négatif
        n1 = n1 + (n1 - n1)
        for i in range(n1):
            produit = produit - n2

    elif n1 < 0 or n2 < 0: #l'un ou l'autre est négatif
        if n1 < 0:
            for i in range(n2):
                produit = produit + n1
        else:
            for i in range(n1):
                produit = produit + n2

    else: #les deux sont positif
        for i in range(n1):
            produit = produit + n2

    return produit

