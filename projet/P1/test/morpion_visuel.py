# Créé par yanis.boulogne, le 16/09/2021 en Python 3.7
import pygame
import time

MARRON = (90,40,0)
VERT = (100,100,50)
BLEU = (50,50,100)
JAUNE =(218, 248, 125)
ROUGE = (199, 44, 72)
pos = (0,0)
joueur = 1
x = 900
l = 0
c = 0
jeu_en_cours = True

main = pygame.display.set_mode((900,900))

def init_plateau():
    jeu_en_cours = True
    return [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
tableau_jeu = init_plateau()

def affichage_tableau(tableau_jeu):
    for ligne in tableau_jeu:
        for cases in ligne:
            print(cases, end=' ')
        print('')
    return

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
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(main, (BLEU), (300 * (pos[0]//300) + (300//2) ,(x//3) * (pos[1]//300) + (300//2)), (300//2), 5)
    return

def croix():
    '''
    permet de créer un cercle à partir du centre de la case du plateau

    paramètre:
        aucun

    renvoie:
        déssine un cerle dans la case voulu
    '''
    pos = pygame.mouse.get_pos()
    pygame.draw.line(main, (JAUNE), (300 * (pos[0]//300), 300 * (pos[1]//300)), (300 * (pos[0]//300) + 300, 300 * (pos[1]//300) + 300), 5)
    pygame.draw.line(main, (JAUNE), (300 * (pos[0]//300), 300 * (pos[1]//300) + 300), (300 * (pos[0]//300) + 300, 300 * (pos[1]//300) ), 5)
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

def choix_case(tableau_jeu, joueur, jeu_en_cours, pos):
    if jeu_en_cours == True :
        l = (pos[1]//300)
        c = (pos[0]//300)
        if tableau_jeu[l][c] != 0 :
            affichage_tableau(tableau_jeu)

            l = 0
            c = 0
            return
        else :
            tableau_jeu[l][c] = joueur
            affichage_tableau(tableau_jeu)
            joueur = changer_joueur(joueur)
            time.sleep(1)
            return choix_case(tableau_jeu, joueur, jeu_en_cours, pos)

while jeu_en_cours :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            jeu_en_cours = False

        if joueur == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pos = pygame.mouse.get_pos()
                    choix_case(tableau_jeu, joueur, jeu_en_cours, pos)
                    croix()
                    verif(tableau_jeu)
                    joueur = 2

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pos = pygame.mouse.get_pos()
                    choix_case(tableau_jeu, joueur, jeu_en_cours, pos)
                    cercle()
                    verif(tableau_jeu)
                    joueur = 1

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RETURN :
                plateau(x)


    pygame.display.flip()
pygame.quit()
