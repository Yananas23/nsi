from tkinter import *
test = 0

def quitter():
    fen.destroy()

def creation_lignes():
    for x in range(0,11):
        Canevas.create_line(64*x, 0, 64*x, 640, width=1, fill="blue")
        Canevas.create_line(0,64*x, 640, 64*x, width=1, fill="blue")

def clear():
    Canevas.delete("all")
    creation_lignes()
    creer_tableau()

def placement(n):
    m = int(n/64)
    m = 64*m
    return m

def creer_grille():
    global tab
    tab = [[0 for i in range(10)] for j in range(10)]

def matrice_clic(X,Y):
    X = int(X/64)
    Y = int(Y/64)
    tab[Y][X] = 1

def Clic(event):
    # position du pointeur de la souris
    X = event.x
    Y = event.y
    X0 = placement(X)
    Y0 = placement(Y)
    X1 = X0 + 60
    Y1 = Y0 + 60
    r = 10
    Canevas.create_oval(X0+2, Y0+2, X1, Y1,fill='magenta')
    matrice_clic(X0,Y0)

def adapte_dessin():
    tab = tab2
    Canevas.delete("all")
    creation_lignes()
    for y in range(0,10):
        for x in range(0,10):
            z = tab[y][x]
            if z == 1:
                Canevas.create_oval(64*x, 64*y, (64*x)+60, (64*y)+60,fill='magenta')
    tab = tab2


def tour_suivant():
    global tab,tab2,x,y,test
    test = test +1
    tab2 = [[0 for i in range(10)] for j in range(10)]
    for y in range(0,9):
        for x in range(0,9):
            compter_cellules_voisines(y,x)
    tab = tab2
    adapte_dessin()


def verif_valeurs(m,n,o,p):
    if m == -1:
        m = 9
    if n == 10:
        n = 0
    if o == -1:
        o = 9
    if p == 10:
        p = 0
    return m,n,o,p

def adapte_matrice(y,x,z):
    tab2[y][x] = z


def cellule_actuelle(y,x,s):
    cell = tab[y][x]
    z = 0
    if cell == 0:                     # Si une cellule morte
        if s == 3:                    # possède exactement 3 voisins vivants
            z = 1                    # elle devient vivante
    else:
        if s == 2 or s == 3:           # Une cellule vivante avec 2 ou 3 voisines vivantes le reste
            z = 1                    # sinon elle meurt (z reste égal à 0)
    adapte_matrice(y,x,z)



def compter_cellules_voisines(y,x):
    m = y-1
    n = y+1
    o = x-1
    p = x+1
    verif_valeurs(m,n,o,p)
    a = tab[m][o]
    b = tab[m][x]
    c = tab[m][p]
    d = tab[y][o]
    e = tab[y][p]
    f = tab[n][o]
    g = tab[n][x]
    h = tab[n][p]
    s = a+b+c+d+e+f+g+h                #somme des cellules vivantes (voisines de la cellule actuelle(x,y))
    cellule_actuelle(y,x,s)




fen = Tk()
fen.title("Le jeu de la vie")
fen.geometry("%dx%d%+d%+d" % (1105,680,80,100))
fen.resizable(width=False, height=False)

Canevas = Canvas(fen, width = 640, height = 640, bg = "White")
Canevas.pack(side =LEFT, padx =18, pady =17 )

quitter = Button(fen, text ='Quitter le jeu', command =quitter)
quitter.pack(side =RIGHT, padx =40, pady =310)

clr = Button(fen, text ='Nettoyer le plateau', command =clear)
clr.pack(side =RIGHT)

etape = Button(fen, text ='Tour suivant', command = tour_suivant)
etape.pack(side =RIGHT, padx =30)


creation_lignes()
Canevas.bind('<Button-1>', Clic)
creer_grille()
fen.mainloop()