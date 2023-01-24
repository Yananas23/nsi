import pygame
from random import randint


ROUGE = (218, 124, 104)
pos = (0, 0)
x = 900
joueur = randint(1,2)
jeu_en_cours = True
peut_jouer = True
main = pygame.display.set_mode((900, 900))


def init_plateau():
    ''' Initialise le tableau de tableau du jeu

    Paramètres :
        None

    Renvoie :
        tab(tableau)
    '''
    jeu_en_cours = True
    tab =  [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    return tab
tableau_jeu = init_plateau()

def affichage_tableau(tableau_jeu):
    ''' Affiche le tableau de jeu

    Paramètres :
        tableau_jeu(tableau)

    Renvoie :
        None
    '''
    for ligne in tableau_jeu:
        for cases in ligne:
            print(cases, end=' ')
        print('')
    return

def verif_ligne(tableau_jeu):
    ''' Vérifie  dans les lignes s'il y a un alignement

        Paramètres :
            tableau_jeu(tableau)

        Renvoie :
            None
    '''
    for ligne in range(3):
        if tableau_jeu[ligne][0] == tableau_jeu[ligne][1] and tableau_jeu[ligne][1] == tableau_jeu[ligne][2] != 0:
            pygame.draw.line(main, (ROUGE), (0, (ligne * 300) + 150), (900, ((ligne * 300) + 150)), 10)
            print('joueur', joueur, 'gagnant')
    return

def verif_colonne(tableau_jeu):
    ''' Vérifie dans les colonnes s'il y a un alignement

        Paramètres :
            tableau_jeu(tableau)

        Renvoie :
            None
    '''
    for colonne in range(3):
        if tableau_jeu[0][colonne] == tableau_jeu[1][colonne] and tableau_jeu[1][colonne] == tableau_jeu[2][colonne] != 0:
            pygame.draw.line(main, (ROUGE), ((colonne * 300) + 150 , 0),((colonne * 300) + 150 , 900), 10)
            print('joueur ', joueur, 'gagnant')
    return

def verif_diagonale1(tableau_jeu):
    ''' Vérifie dans la première diagonale ([0][0] à [2][2]) s'il y a un alignement

        Paramètres :
            tableau_jeu(tableau)

        Renvoie :
            None
    '''
    if tableau_jeu[0][0] == tableau_jeu[1][1] != 0 and tableau_jeu[1][1] == tableau_jeu[2][2] != 0:
        pygame.draw.line(main, (ROUGE), (0, 0), (900, 900), 20)
        print('joueur', joueur, 'gagnant')
    return

def verif_diagonale2(tableau_jeu):
    ''' Vérifie dans la deuxième diagonale ([0][2] à [2][0]) s'il y a un alignement

        Paramètres :
            tableau_jeu(tableau)

        Renvoie :
            None
    '''
    if tableau_jeu[0][2] == tableau_jeu[1][1] != 0 and tableau_jeu[1][1] == tableau_jeu[2][0] != 0:
        pygame.draw.line(main, (ROUGE), (900, 0), (0, 900), 20)
        print('joueur', joueur, 'gagnant')
    return

def verif_egalite(tableau_jeu):
    ''' Vérifie dans le tableau si toutes les cases sont différentes de 0

        Paramètres :
            tableau_jeu(tableau)

        Renvoie :
            None
    '''
    for ligne in range(2):
        if tableau_jeu[ligne][0] and tableau_jeu[ligne][1] != 0 and tableau_jeu[ligne][1] and tableau_jeu[ligne][2] != 0:
            print('égalité')
    return

def verif(tableau_jeu):
    ''' contient toutes les vérifications en une seule fonction

        Paramètres :
            tableau_jeu(tableau)

        Renvoie :
            None
    '''
    verif_ligne(tableau_jeu)
    verif_colonne(tableau_jeu)
    verif_diagonale1(tableau_jeu)
    verif_diagonale2(tableau_jeu)
    verif_egalite(tableau_jeu)
    return

def changer_joueur(joueur):
    ''' Permet de changer des joueurs à partir de la fonction affine 3 - x

        Paramètres :
            joueur(int)

        Renvoie :
            joueur(int)
    '''
    joueur = 3 - joueur
    return joueur

def plateau(x):
    ''' Trace le plateau pygame

        Paramètres :
            x(int)

        Renvoie :
            None
    '''
    MARRON = (90, 40, 0)
    VERT = (100, 100, 50)
    L = 0.0
    main.fill(MARRON)
    for i in range(2):
        L = L + x/3
        pygame.draw.line(main, (VERT), (L, 0), (L, x), 10)
        pygame.draw.line(main, (VERT), (0, L), (x, L), 10)
    pygame.display.flip()
    return

def cercle():
    ''' Trace un cercle dans le plateau pygame

        Paramètres :
            None

        Renvoie :
            None
    '''
    BLEU = (50, 50, 100)
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(main, (BLEU), ((x // 3) * (pos[0] // (x // 3)) + ((x // 3) // 2) ,(x // 3) * (pos[1] // 300) + ((x // 3) // 2)), ((x // 3) // 2), 5)
    return

def croix():
    ''' Trace une croix dans le plateau pygame

        Paramètres :
            None

        Renvoie :
            None
    '''
    JAUNE =(218, 248, 125)
    pos = pygame.mouse.get_pos()
    pygame.draw.line(main, (JAUNE), ((x // 3) * (pos[0] // 300), 300 * (pos[1] // 300)), (300 * (pos[0] // 300) + 300, 300 * (pos[1] // 300) + 300), 5)
    pygame.draw.line(main, (JAUNE), ((x // 3) * (pos[0] // 300), 300 * (pos[1] // 300) + 300), ((x // 3) * (pos[0] // 300) + (x // 3), 300 * (pos[1] // 300) ), 5)
    return

def choix_case(tableau_jeu, joueur, jeu_en_cours, pos):
    ''' Permet de mettre les coordonnées dans le tableau

        Paramètres :
            tableau_jeu(tableau)
            joueur(int)
            jeu_en_cours(booléen)
            pos(tupple)

        Renvoie :
            peut_jouer(booléen)
    '''
    if jeu_en_cours == True :
        pos = pygame.mouse.get_pos()
        l = pos[1] // 300
        c = pos[0] // 300
        if tableau_jeu[l][c] != 0 :
            peut_jouer = False
            return peut_jouer
        else:
            peut_jouer = True
            tableau_jeu[l][c] = joueur
            return peut_jouer

while jeu_en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            jeu_en_cours = False

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN :
                plateau(x)
                tableau_jeu.clear()
                init_plateau()
                tableau_jeu = init_plateau()


            if joueur == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pos = pygame.mouse.get_pos()
                        choix_case(tableau_jeu, joueur, jeu_en_cours, pos)
                        if peut_jouer == True:
                            cercle()
                            joueur = 3 - joueur
                            verif(tableau_jeu)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        pos = pygame.mouse.get_pos()
                        choix_case(tableau_jeu, joueur, jeu_en_cours, pos)
                        if peut_jouer == True:
                            croix()
                            joueur = 3 - joueur
                            verif(tableau_jeu)
        else:
            quit()
    pygame.display.flip()
pygame.quit()


'''
peut pas jouer sur case jouée
finir partie quand égalité
'''