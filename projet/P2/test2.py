# Créé par Yanis Boulogne, le 10/12/2021 en Python 3.7
import sqlite3

connexion = sqlite3.connect('')
curseur = connexion.cursor()

def creation_base(nom):
    '''
        Fonction qui va servir à créer et ouvrir une base de données. Si la base
        existe déjà, elle sera remplacée.

        Paramètres:
            nom (str) : Nom que l'on veut donner à la base, il faut qu'il contienne le chemin
                        d'accès à la base avec le suffixe du fichier au bout

        Renvoie:
            Aucun

        Effets de Bord:
            connexion
            curseur
    '''
    pass
    #global connexion
    #global curseur
    #connexion = sqlite3.connect(nom)
    #curseur = connexion.cursor()
    #print('Base Ouverte')

def ouverture(chemin_vers_base):
    '''
    permet d'ouvrir une base de donnée

    paramètre:
        chemin_vers_base = chemin vers la base de donée pour l'ouvir
    '''
    global connexion
    global curseur
    base_donnee = chemin_vers_base + '.db'
    connexion = sqlite3.connect(base_donnee)
    curseur = connexion.cursor()
    print('La base de donnée "',base_donnee,'" est ouverte.')
    return curseur,connexion

def creation_table(nom_table):
    '''
        Fonction qui va servir à créer une table en fonction du nom entré
        en paramètres.

        Paramètres:
            nom_table (Str) : Nom de la Table à créer


    '''
    global curseur
    global connexion
    requetes = {'Type' : """CREATE TABLE Type ('ID Type' INTEGER PRIMARY KEY, 'Nom' TEXT, 'Casse' TEXT);"""
                , 'Matériau' : """CREATE TABLE Matériau ('ID Matériau' TEXT PRIMARY KEY, 'Nom' TEXT, 'Image' TEXT);"""
                , 'Outil' : """CREATE TABLE Outil ('ID' TEXT PRIMARY KEY, 'ID Type' INTEGER REFERENCES Type('ID Type'), 'ID Matériau' TEXT REFERENCES Matériau('ID Matériau'), 'Nom' TEXT, 'Durabilité' INTEGER, 'Dégâts' INTEGER, 'Image' TEXT);"""}
    txt = requetes[nom_table]
    curseur.execute(txt)
    connexion.commit

def suppression_table(nom_table):
    global curseur
    global connexion
    txt = "DROP TABLE "+ str(nom_table) + ';'
    curseur.execute(txt)
    connexion.commit()

def fermeture_base():
    '''
        Fonction qui va servir à fermer la base de données.

        Paramètres:
            Aucun

        Renvoie:
            Aucun

        Effets de Bord:
            connection
    '''
    global connexion
    connexion.close()
    print('Base Fermée')

def ajout(name_table,args):
    '''
    Permet d'ajouter des données à  une Table à une base de données.

    paramètre:
        name_table = nom de la table
        args = paramètre de la table
    '''
    global curseur
    global connexion

    P = '('
    for i in range(len(args)):
        P = P + "'"
        P = P + args[i]
        P = P + "',"
        print(P)
    P = P[:-1]
    P = P + ')'
    print(P)
    add = 'INSERT INTO ' + name_table + ' VALUES ' + P + ';'
    print(P)
    curseur.execute(add)
    connexion.commit()
    return add

def modifier(name_table,categorie1, nouvelle_donne, categorie2, donne_a_modifier):
    '''
    Permet de modifier des données à une base de données.

    paramètre:
        name_table = nom de la table

        categorie1 = catégorie où placer la nouvelle donnée

        categorie2 = catégorie où apparait la donnée à modifier

        nouvelle_donne = donnée qui apparaitera dans la base de donnée

        donne_a_modifier = donnée dannant des indications sur quoi modifier
    '''
    global curseur
    global connexion

    modif = 'update ' + name_table + ' set ' + categorie1 +"='" + nouvelle_donne + "' " + 'WHERE ' + categorie2 +"='" + donne_a_modifier + "';"
    print(modif)
    curseur.execute(modif)
    connexion.commit()
    return modif

def suppression_donnee(name_table, categorie, donne_a_suppr):
    '''
    Permet de modifier des données à une base de données.

    paramètre:
        name_table = nom de la table

        categorie = catégorie où supprimer donnée

        donne_a_suppr = donnée qui sera supprimé

    '''
    global curseur
    global connexion

    suppr = 'DELETE FROM ' + name_table +  ' WHERE ' + categorie +"='" + donne_a_suppr + "';"
    print(suppr)
    curseur.execute(suppr)
    connexion.commit()
    return suppr

def affichage(table):
    global curseur
    global connexion
    txt = 'SELECT * FROM ' + table +';'
    print(txt)
    curseur.execute(txt)
    connexion.commit()
    return txt


if __name__ == '__main__':
    creation_base('G:\projet_DY\JEU_DE_CUBE.db')
    #fermeture_base()
