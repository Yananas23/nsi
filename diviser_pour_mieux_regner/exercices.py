# Créé par yanis.boulogne, le 24/01/2022 en Python 3.7

from typing import List


def puissance_iterative(x,n):
    if n == 0:
        return 1
    else:
        produit = 1
        for i in range(1, n+1):
            produit = produit * x
        return produit

def puissance_recursive(x,n):
    if n == 0:
        return 1
    else:
        return x * puissance_recursive(x,n-1)

def puissance_diviser(x,n):
    if n == 0:
        return 1
    else:
        if n % 2 ==0:
            return puissance_diviser(x,n/2) * puissance_diviser(x, n/2)
        else:
            return puissance_diviser(x,(n-1)/2) * x * puissance_diviser(x, (n-1)/2)

def maxi(a,b):
    if a > b :
        return a
    else:
        return b

def maxi_iterative(L):
    max = L[0]
    if len(L) == 1:
        return max
    else:
        for i in range(1, len(L)):
            if L[i] > max:
                max = L[i]
        return maxi

def maxi_recursive(L):
    if len(L) == 1:
        return L[0]
    else:
        if L[1] > L[0]:
            L.pop(0)
        else:
            L.pop(1)
        return maxi_recursive(L)

def maxi_diviser(L):
        x = int(len(L)//2)
        L1 = L[:x]
        L2 = L[x:]
        if len(L) == 1:
            return L[0]
        else:
            return maxi(maxi_diviser(L1),maxi_diviser(L2))

def fusion(L1,L2):
    L = []
    for i in range(len(L1)):
        L.append(L1[i])
    for i in range(len(L2)):
        L.append(L2[i])
    return L

def tri_fusion(L):

    if len(L) == 1:
        return L
    else :
        for i in range(1, len(L)):
            k = L[i]
            j = i - 1
            while j >= 0 and k < L[j] :
                L[j + 1] = L[j]
                j = j - 1
            L[j + 1] = k
        if j == 0:
            j = j - 1
            return tri_fusion(L)
        else:
            x = int(len(L)//2)
            L1 = L[:x]
            L2 = L[x:]    
            return fusion(L1,L2)

