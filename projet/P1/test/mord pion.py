#def des variables

Tableau=[   [0,4,0,4,0],
            [3,5,3,5,3],
            [0,4,0,4,0],
            [3,5,3,5,3],
            [0,4,0,4,0]]

nbr_cases_jouees=0

numero_joueur=1

l=0
c=0
x=0

ligne=[]
colonne=[]

#def des fonctions

def Demande(l,c) :
    l=int(input('quelle ligne ? (1, 3 ou 5)'))
    ligne.append(l)
    c=int(input('quelle colonne ? (1, 3 ou 5)'))
    colonne.append(c)

#le jeu

while nbr_cases_jouees<9 :
    Demande(l,c)
    if Tableau[l][c]==0:
        nbr_cases_jouees +=1

        if numero_joueur==1 :
            numero_joueur=2
            Tableau[l][c]=1

        elif numero_joueur==2 :
            numero_joueur=1
            Tableau[l][c]=2

for i in range(5):
    for j in range(5):
        if Tableau[i][j]==0:
            print(' ',end='')
        elif Tableau[i][j]==1:
            print('X',end='')
        elif Tableau[i][j]==2:
            print('O',end='')
        elif Tableau[i][j]==3:
            print('-',end='')
        elif Tableau[i][j]==5:
            print('+',end='')
        else:
            print('|',end='')
    print('')