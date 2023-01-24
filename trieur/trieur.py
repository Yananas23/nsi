L=[]

x=int(input("taille de la liste "))

for i in range(x):
        L.append(int(input("donne un chiffre ")))

print("liste non rangé",L)

liste_dans_lordre=[]

while len(L)!=0:
    mini=L[0]
    print(L,liste_dans_lordre)
    for i in range(1,len(L)):
        if L[i]<mini:
            mini=L[i]
    liste_dans_lordre.append(mini)
    L.remove(mini)


print("liste rangé",liste_dans_lordre)