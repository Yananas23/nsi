# Créé par Yanis Boulogne, le 20/10/2021 en Python 3.7
import pygame

main = pygame.display.set_mode((900, 900))

def cercle_victoire_diagonale1():
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''
    ROUGE = (200, 45, 70)
    for i in range(3):
        x =  i * 300 + 150
        y =  i * 300 + 150
        pygame.draw.circle(main, (ROUGE), (x, y), 150, 5)
    return

def cercle_victoire_diagonale2():
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''
    x = 750
    y = 900
    ROUGE = (200, 45, 70)
    for i in range(3):
        y = i * 300 + 150
        pygame.draw.circle(main, (ROUGE), (x, y), 150, 5)
        x = x - 300
    return

def cercle_victoire_ligne(ligne):
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''

    ROUGE = (200, 45, 70)

    for i in range(3):
        x =  i * 300 + 150
        y = ligne * 300 + 150
        pygame.draw.circle(main, (ROUGE), (x, y), 150, 5)
    return

def cercle_victoire_colonne(colonne):
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''

    ROUGE = (200, 45, 70)

    for i in range(3):
        x =  colonne * 300 + 150
        y =  i * 300 + 150
        pygame.draw.circle(main, (ROUGE), (x, y), 150, 5)
    return

def croix_victoire_diagonale1():
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''
    ROUGE = (200, 45, 70)
    for i in range(3):
        x=  i * 300
        y =  i * 300
        pygame.draw.line(main, (ROUGE), ((300) * (x // 300), 300 * (y // 300)), (300 * (x // 300) + 300, 300 * (y // 300) + 300), 5)
        pygame.draw.line(main, (ROUGE), ((300) * (x // 300), 300 * (y // 300) + 300), ((300) * (x // 300) + (300), 300 * (y // 300) ), 5)
    return

def croix_victoire_diagonale2():
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''
    x = 900
    ROUGE = (200, 45, 70)
    for i in range(4):
        y = i * 300
        pygame.draw.line(main, (ROUGE), (x , y), (300 * (x // 300) - 300, 300 * (y // 300) - 300), 5)
        pygame.draw.line(main, (ROUGE), (( x ), ( y ) - 300), ((300) * (x // 300) - (300), 300 * (y // 300) ), 5)
        x = 900 - (i * 300)

    return

def croix_victoire_ligne(ligne):
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''
    ROUGE = (200, 45, 70)
    for i in range(3):
        x =  i * 300
        y =  ligne * 300
        pygame.draw.line(main, (ROUGE), ((300) * (x // 300), 300 * (y // 300)), (300 * (x // 300) + 300, 300 * (y // 300) + 300), 5)
        pygame.draw.line(main, (ROUGE), ((300) * (x // 300), 300 * (y // 300) + 300), ((300) * (x // 300) + (300), 300 * (y // 300) ), 5)
    return

def croix_victoire_colonne(colonne):
    ''' Trace les cercles dans le plateau pygame en cas de victoire

        Paramètres :
            None

        Renvoie :
            None
    '''
    ROUGE = (200, 45, 70)
    for i in range(3):
        x =  colonne * 300
        y =  i * 300
        pygame.draw.line(main, (ROUGE), ((300) * (x // 300), 300 * (y // 300)), (300 * (x // 300) + 300, 300 * (y // 300) + 300), 5)
        pygame.draw.line(main, (ROUGE), ((300) * (x // 300), 300 * (y // 300) + 300), ((300) * (x // 300) + (300), 300 * (y // 300) ), 5)
    return