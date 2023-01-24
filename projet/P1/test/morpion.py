import pygame
from random import randint

nb_case_jouee = 0
ROUGE = (199, 44, 72)
pos = (0,0)
x = 900
joueur = randint(1,2)
l = 0
c = 0
jeu_en_cours = True
main = pygame.display.set_mode((900,900))


def init_plateau():
    jeu_en_cours = True
    tab =  [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    return tab
tableau_jeu = init_plateau()

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

def plateau( x ):
    '''
    permet de creer le plateau à partir des dimmension de l'écran x passé
    en paramètre.

    paramètres:
        x (int) = valeur du coté de la fenètre

    variables:
        L (float) =

    renvoie:
        fenètre du morpion
    '''
    MARRON = (90,40,0)
    VERT = (100,100,50)
    L = 0.0
    main.fill(MARRON)
    for i in range(2):
        L = L + x/3
        pygame.draw.line(main, (VERT),(L,0),(L,x),10)
        pygame.draw.line(main, (VERT),(0,L),(x,L),10)
    pygame.display.flip()
    return

def cercle():
    '''
    permet de créer un cercle à partir du centre de la case du plateau

    paramètre:
        aucun

    renvoie:
        déssine un cerle dans la case voulu
    '''
    BLEU = (50,50,100)
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(main, (BLEU), ((x//3) * (pos[0]//(x//3)) + ((x//3)//2) ,(x//3) * (pos[1]//300) + ((x//3)//2)), ((x//3)//2), 5)
    return

def croix():
    '''
    permet de créer un cercle à partir du centre de la case du plateau

    paramètre:
        aucun

    renvoie:
        déssine un cerle dans la case voulu
    '''
    JAUNE =(218, 248, 125)
    pos = pygame.mouse.get_pos()
    pygame.draw.line(main, (JAUNE), ((x//3) * (pos[0]//300), 300 * (pos[1]//300)), (300 * (pos[0]//300) + 300, 300 * (pos[1]//300) + 300), 5)
    pygame.draw.line(main, (JAUNE), ((x//3) * (pos[0]//300), 300 * (pos[1]//300) + 300), ((x//3) * (pos[0]//300) + (x//3), 300 * (pos[1]//300) ), 5)
    return

def choix_case(tableau_jeu, joueur, jeu_en_cours, pos, nb_case_jouee):
    if jeu_en_cours == True :
        pos = pygame.mouse.get_pos()
        l = pos[1]//300
        c = pos[0]//300
        if tableau_jeu[l][c] != 0 :
            affichage_tableau(tableau_jeu)
            l = 0
            c = 0
            nb_case_jouee = nb_case_jouee + 1
            return(nb_case_jouee)
        else :
            tableau_jeu[l][c] = joueur
            affichage_tableau(tableau_jeu)
            l = 0
            c = 0

            return(nb_case_jouee)

affichage_tableau(tableau_jeu)


while jeu_en_cours:
    if nb_case_jouee != 9 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                jeu_en_cours = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN :
                    plateau(x)
                    init_plateau()



            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    choix_case(tableau_jeu, joueur, jeu_en_cours, pos, nb_case_jouee)
                    if joueur == 1:
                        pos = pygame.mouse.get_pos()

                        cercle()
                        joueur = 3 - joueur
                        verif(tableau_jeu)
                    else:
                        pos = pygame.mouse.get_pos()

                        croix()
                        joueur = 3 - joueur
                        verif(tableau_jeu)



    pygame.display.flip()
pygame.quit()

if nb_case_jouee == 9 :
            print(nb_case_jouee)
            jeu_en_cours = False
'''
couleur qui change
reset tableau
finir partie quand égalité
doc
empecher le redessin
'''