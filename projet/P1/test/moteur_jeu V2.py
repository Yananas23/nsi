joueur = 1
l = 0
c = 0
jeu_en_cours = True

def init_plateau():
    jeu_en_cours = True
    return [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

def affichage_tableau(tableau_jeu):
    for ligne in tableau_jeu:
        for cases in ligne:
            print(cases, end=' ')
        print('')
    return


def verif_ligne(tableau_jeu):
    for ligne in range(3):
        if tableau_jeu[ligne][0] == tableau_jeu[ligne][1] and tableau_jeu[ligne][1] == tableau_jeu[ligne][2] != 0:
            jeu_en_cours = False
            print('joueur ', joueur, 'gagnant')


def verif_colonne(tableau_jeu):
    for colonne in range(3):
        if tableau_jeu[0][colonne] == tableau_jeu[1][colonne] and tableau_jeu[1][colonne] == tableau_jeu[2][colonne] != 0:
            jeu_en_cours = False
            print('joueur ', joueur, 'gagnant')


def verif_diagonale1(tableau_jeu):
    if tableau_jeu[0][0] == tableau_jeu[1][1] == 1 and tableau_jeu[1][1] == tableau_jeu[2][2] != 0:
        jeu_en_cours = False
        print('joueur', joueur, 'gagnant')


def verif_diagonale2(tableau_jeu):
    if tableau_jeu[0][2] == tableau_jeu[1][1] == 1 and tableau_jeu[1][1] == tableau_jeu[2][0] != 0:
        jeu_en_cours = False
        print('joueur', joueur, 'gagnant')


def verif(tableau_jeu):
    verif_ligne(tableau_jeu)
    verif_colonne(tableau_jeu)
    verif_diagonale1(tableau_jeu)
    verif_diagonale2(tableau_jeu)

def changer_joueur(joueur):
    joueur = 3 - joueur
    return joueur

def choix_case(tableau_jeu, joueur, jeu_en_cours):
    verif(tableau_jeu)
    if jeu_en_cours == True :
        l = int(input('choisir ligne'))
        c = int(input('choisir colonne'))
        if tableau_jeu[l][c] != 0 :
            affichage_tableau(tableau_jeu)
            return choix_case(tableau_jeu, joueur, jeu_en_cours)
        else :
            tableau_jeu[l][c] = joueur
            affichage_tableau(tableau_jeu)
            joueur = changer_joueur(joueur)
            return choix_case(tableau_jeu, joueur, jeu_en_cours)

tableau_jeu = init_plateau()
affichage_tableau(tableau_jeu)
choix_case(tableau_jeu, joueur, jeu_en_cours)
changer_joueur(joueur)

