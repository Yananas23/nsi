import sqlite3

con = sqlite3.connect('')
cur = con.cursor()

def creation_base(nom : str):
    ''' Crée la base de données

    Paramètres : None

    Renvoie : sqlite3.Connection
    '''

    global con
    global cur

    nom = nom + '.db'
    con = sqlite3.connect(nom)
    cur = con.cursor()
    return

def fermeture_base():
    ''' Ferme la base de données

    Paramètres : nom

    Renvoie : None
    '''

    global con

    con.close()

def creation_table(nom_table : str):
    '''
    Crée une table dans la base de données

    Tables possibles : 'Personnage'
                       'Régions'
                       'Voie'
                       'Classe'


    Paramètres: nom_table

    Renvoie:None
    '''

    global con
    global cur

    if nom_table == 'Personnage':
        cur.execute('''CREATE TABLE Personnage
                        (ID_personnage text PRIMARY KEY, ID_région text REFERENCES Régions("ID_région"), ID_classe text REFERENCES Classe("ID_classe"), nom_voie text REFERENCES Voie("nom_voie"), ID_coût real, ID_année real, age real, espèce text, nb_perso real)''')
    elif nom_table == 'Régions':
        cur.execute('''CREATE TABLE Régions
                        (ID_région text PRIMARY KEY, environnement text, empl_logo text)''')
    elif nom_table == 'Voie':
        cur.execute('''CREATE TABLE Voie
                        (nom_voie text PRIMARY KEY, type_monstre text, empl_logo text)''')
    elif nom_table == 'Classe':
        cur.execute('''CREATE TABLE Classe
                        (ID_classe text PRIMARY KEY, portée real, ressource text)''')


def ajout_donnee(nom_table : str, donnees : list):
    ''' Ajoute des données à une table

    Paramètres : nom_table
                 donnees

    Renvoie : None
    '''

    global con
    global cur

    requete = '''INSERT INTO ''' + nom_table + ''' VALUES('''
    for i in range(len(donnees)):
        if isinstance(donnees[i], str):
            d = '''"''' + donnees[i] + '''"'''
        else:
            d = donnees[i]
        requete = requete + d + ','
    requete = requete[:-1] + ')'
    cur.execute(requete)
    con.commit()

def afficher_table(nom_table : str):
    '''Permet d'afficher une table d'une base déjà créée

    Paramètre : nom_table

    Renvoie : i (str)

    '''

    global con
    global cur

    cur.execute("SELECT * FROM " + nom_table)
    affiche = cur.fetchall()
    for i in affiche:
        print(i)

def filtre_donnees(nom_table : str, attribut : str, condition : str):
    ''' Trie les données selon les éléments voulus

    Paramètres : nom_table
                 donnees

    Renvoie : donnees_triees (str)

    '''
    requete = '''SELECT * FROM ''' + nom_table + ''' WHERE ''' + attribut + ''' = ''' + '''"''' + condition + '''"'''
    global con
    global cur
    Test = cur.execute(requete)
    affiche = cur.fetchall()
    for i in affiche:
        print(i)

def tri_donnees(nom_table : str, attribut : str, ordre : str):
    ''' Trie les données selon un attribut et un ordre (ASC ou DESC)

    Paramètres : nom_table
                 attribut
                 ordre

    Renvoie : i (str)

    '''
    global con
    global cur

    requete = '''SELECT * FROM ''' + nom_table + ''' ORDER BY ''' + attribut + ''' ''' + ordre
    Test = cur.execute(requete)
    affiche = cur.fetchall()
    for i in affiche:
        print(i)

