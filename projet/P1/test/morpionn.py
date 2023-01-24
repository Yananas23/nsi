#Alderweirelt Charles, Lebouazda Chamseddine, Ait Brahim Anass
cases = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
def affichage(tableau):
    for i in range(len(tableau)):
        print(tableau[i]) #on affiche chaque ligne du tableau une par une
    return

def demande(numero):
    while True:
        ligne = input("Saisissez la ligne") #on demande la ligne
        colonne = input("Saisissez la colonne") #on demande la colonne
        if ligne + colonne in restant: #on verifie si les coordonnées sont valides
            for i in range(len(restant) - 1):
                if restant[i] == ligne + colonne:
                    restant.pop(i) #on enleve des coordonnées valides restantes celle que l'utilisateur vient de rentrer
            break
    cases[int(ligne) - 1][int(colonne) - 1] = numero #on place 1 ou -1 sur la grille du morpion
    return cases #on renvoit le morpion modifié

def verif(tableau):
    sommesLignes = [tableau[0][0] + tableau[0][1] + tableau[0][2], tableau[1][1] + tableau[1][1] + tableau[1][2], tableau[2][1] + tableau[2][1] + tableau[2][2]]
    sommesColonnes = [tableau[0][0] + tableau[1][0] + tableau[2][0], tableau[0][1] + tableau[1][1] + tableau[2][1], tableau[0][2] + tableau[1][2] + tableau[2][2]]
    sommesDiagonales = [tableau[0][0] + tableau[1][1] + tableau[2][2], tableau[0][2] + tableau[1][1] + tableau[2][0]]
    #ici on crée 3 listes stockant l'une les 3 sommes des listes, l'une les 3 sommes des colonnes et la dernière les 2 sommes des 2 diagonales
    for i in sommesLignes:
        if i == 3:
            return 1 #si dans les sommes des lignes l'une est de 3 on renvoit le numero du joueur 1 gagnant
        elif i == -3:
            return 2 #si dans les sommes des lignes l'une est de -3 on renvoit le numero du joueur 2 gagnant
    for i in sommesColonnes:
        if i == 3:
            return 1 #si dans les sommes des colonnes l'une est de 3 on renvoit le numero du joueur 1 gagnant
        elif i == -3:
            return 2 #si dans les sommes des colonnes l'une est de -3 on renvoit le numero du joueur 2 gagnant
    for i in sommesDiagonales:
        if i == 3:
            return 1 #si dans les sommes des diagonales l'une est de 3 on renvoit le numero du joueur 1 gagnant
        elif i == -3:
            return 2 #si dans les sommes des diagonales l'une est de -3 on renvoit le numero du joueur 2 gagnant
    return False #retourner False si aucune somme de ligne, colonne ou diagonale est égale à 3 ou -3

affichage(cases) #afficher morpion actuel, ici vierge
restant = ["11", "12", "13", "21", "22", "23", "31", "32", "33"] #on définit les coordonnées valides du morpion
for i in range(9): #on réalise 9 tours
    if i % 2 == 0:
        cases = demande(1)
        print('Au tour du joueur 1')
    else:
        cases = demande(2)
        print('Au tour du joueur 2') #tout cela permet d'alterner entre joueur 1 et 2 à chaque tour
    affichage(cases) #afficher le morpion actuel
    if verif(cases) == 1:
        print("Le gagnant de la partie est le joueur 1") #si la somme d'une ligne, colonne ou d'une diagonale est de 3 alors est renvoyé 1, soit le joueur 1 gagne
        break
    elif verif(cases) == 2:
        print("Le gagnant de la partie est le joueur 2") #si la somme d'une ligne, colonne ou d'une diagonale est de -3 alors est renvoyé 2, soit le joueur 2 gagne
        break
    if i == 9:
        print("Personne n'a gagné.")#si au bout de neuf tours aucune somme d'une ligne, colonne ou diagonale est de 3 ou d -3 personne n'a gagné