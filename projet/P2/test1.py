# Créé par yanis.boulogne, le 01/12/2021 en Python 3.7
import sqlite3 as sql

con = None
cur = None

def ouverture(chemin_vers_base):
    '''
    permet d'ouvrir une base de donnée

    paramètre:
        chemin_vers_base = chemin vers la base de donée pour l'ouvir
    '''
    base_donnee = chemin_vers_base + '.db'
    con = sql.connect(base_donnee)
    cur = con.cursor()
    print('La base de donnée "',base_donnee,'" est ouverte.')
    return cur,con

def ajout(name_table,args):
    '''
    Permet d'ajouter des données à  une Table à une base de données.

    paramètre:
        name_table = nom de la table
        P = paramètre de la table
    '''
    global cur,con

    P = '('
    for i in range(len(args)):
        P = P + args[i]
        P = P + ','
        print(P)
    P = P[:-1]
    P = P + ')'

    add = 'INSERT INTO ' + name_table + 'VALUES ' + P + ';'

    cur.execute(add)
    con.commit
    con.close
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
    global cur,con

    modif = 'update ' + name_table + 'set ' + categorie1 +"='" + nouvelle_donne + "'" + 'WHERE ' + categorie2 +"='" + donne_a_modifier + "';"

    cur.execute(add)
    con.commit
    con.close
    return modif



def test():
    global cur,con
    ligne = cur.execute('SELECT * FROM Type').fetchall()
    print(ligne)
    return


