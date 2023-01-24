#Pr○jet de Daniel Le T○riellec et de Yanis B○ul○gne, TGB ☻

import sqlite3

connexion = sqlite3.connect('')
curseur = connexion.cursor()

# Fonctions de Base

def creation_base(nom):
    '''
        Fonction qui va servir à créer et ouvrir une base de données. Si la base
        existe déjà, elle sera remplacée.

        Paramètres:
            ► nom (str) : Nom que l'on veut donner à la base, il faut qu'il contienne le chemin
                        d'accès à la base avec le suffixe du fichier au bout

        Renvoie:
            Aucun

        Effets de Bord:
            ► connexion
            ► curseur
    '''
    global connexion
    global curseur
    connexion = sqlite3.connect(nom)
    curseur = connexion.cursor()
    print('Base Ouverte')

def fermeture_base():
    '''
        Fonction qui va servir à fermer la base de données.

        Paramètres:
            Aucun

        Renvoie:
            Rien

        Effets de Bord:
            ► connexion
    '''
    global connexion
    connexion.close()
    print('Base Fermée')

def creation_table(nom_table):
    '''
        Fonction qui va servir à créer une table en fonction du nom entré
        en paramètres.

        Paramètres:
            ► nom_table (Str) : Nom de la Table à créer (soit Type, soit Matériel, soit Outil)

        Renvoie:
            Rien

        Effets de Bord:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    requetes = {'Type' : """CREATE TABLE Type ('ID_Type' SMALLINT PRIMARY KEY, 'Nom_T' VARCHAR(15), 'Casse' VARCHAR(15));"""
                , 'Matériau' : """CREATE TABLE Matériau ('ID_Matériau' TEXT PRIMARY KEY, 'Nom_M' VARCHAR(15), 'Image' TEXT);"""
                , 'Outil' : """CREATE TABLE Outil ('ID' TEXT PRIMARY KEY, 'ID_Type' SMALLINT REFERENCES Type('ID_Type'), 'ID_Matériau' TEXT REFERENCES Matériau('ID_Matériau'), 'Nom_O' VARCHAR(30), 'Durabilité' SMALLINT, 'Dégâts' REAL, 'Image' TEXT);"""}
    txt = requetes[nom_table]
    curseur.execute(txt)
    connexion.commit()

def suppression_table(nom_table):
    '''
        Fonction qui permet de supprimer une table.

        Paramètres:
            ► nom_table (str) : Nom de la table à supprimer

        Renvoie:
            Rien

        Effets de Bords:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    txt = "DROP TABLE "+ str(nom_table) + ';'
    curseur.execute(txt)
    connexion.commit()

def ajout_donnee(nom_table, liste_valeurs):
    '''
        Fonction qui permet d'ajouter des données à  une Table à une base de données.

        paramètre:
            ► nom_table (str) : Nom de la table
            ► liste_valeurs (tuple) :

        Renvoie:
            Rien

        Effets de Bord:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    txt = 'INSERT INTO ' + nom_table + ' VALUES ' + str(liste_valeurs) + ';'
    print(txt)
    curseur.execute(txt)
    connexion.commit()

def suppression_donnee(name_table, categorie, donne_a_suppr):
    '''
        Fonction qui permet de modifier des données à une base de données.

        Paramètres:
            ► name_table (str) : Nom de la table
            ► categorie (str) : Catégorie d'où provient la donnée à supprimer
            ► donne_a_suppr (str) : Donnée qui sera supprimée

        Renvoie:
            Rien

        Effets de Bords:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    txt = 'DELETE FROM ' + name_table +  ' WHERE ' + categorie +"='" + donne_a_suppr + "';"
    print(txt)
    curseur.execute(txt)
    connexion.commit()

def modifier_valeurs(nom_table,categorie1, nouvelle_donnee, categorie2, donnee_a_modifier):
    '''
        Fonction qui permet de modifier des données à une base de données.

        Paramètres:
            ► nom_table (str) : Nom de la table
            ► categorie1 (str) : Catégorie où placer la nouvelle donnée
            ► nouvelle_donnee (str) : Nouvelle donnée qui apparaîtera dans la base de donnée
            ► categorie2 (str) : Catégorie où apparaît la donnée à modifier
            ► donnee_a_modifier (str) : Donnée donnant des indications

        Renvoie:
            Rien

        Effets de Bords:
            ► connexion
            ► curseur

        Exemple de requête:
            ► UPDATE *nom_table* SET *categorie1*='*nouvelle_donnee*' WHERE *categorie2*='*donnee_a_modifier*';
    '''
    global curseur
    global connexion
    txt = 'UPDATE ' + nom_table + ' SET ' + categorie1 +"='" + nouvelle_donnee + "' " + 'WHERE ' + categorie2 +"='" + donnee_a_modifier + "';"
    curseur.execute(txt)
    connexion.commit()

# Fonctions Filtres

def affichage_donnees(table, categorie):
    '''
        Fonction qui permet d'afficher les données de la catégorie, entrée en paramètres,
        provenant de la table, entrée en paramètres.

        Paramètres:
            ► table (str) : Nom de la table d'où proviennent les valeurs
            ► categorie (str) : Nom de la colonne d'où proviennent les valeurs

        Renvoie:
            Rien

        Effets de Bords:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    txt = 'SELECT ' + categorie + ' FROM ' + table +';'
    for ligne in curseur.execute(txt):
        print(ligne)

def affichage_filtre(categories1, nom_table, categorie2, donnee):
    '''
        Fonction qui permet de filtrer les données qui seront affichées.

        Paramètres:
            ► categories1 (list) : Liste des catégories qui seront affichées
            ► nom_table (str) : Nom de la table d'où proviennent les données affichées
            ► categorie2 (str) : Nom de la catégorie qui sert à filtrer (après le WHERE)
            ► donnee (str) : Donnée cherchée

        Renvoie:
            Rien

        Effets de Bord:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    txt = 'SELECT '
    for i in range(len(categories1)):
        txt = txt + categories1[i] + ','
    txt = txt[:-1]
    txt = txt + ' FROM ' + nom_table + ' WHERE ' + categorie2 + "='" + donnee + "';"
    for ligne in curseur.execute(txt):
        print(ligne)

def filtre_ordonne(categories1, nom_table, categorie2, DESC_ou_ASC):
    '''
        Fonction qui permet de filtrer et de faire une distinction sur
        les données qui seront affichées.

        Paramètres:
            ► categories1 (list) : Liste des catégories qui seront affichées
            ► nom_table (str) : Nom de la table d'où proviennent les données affichées
            ► categorie2 (str) : Nom de la catégorie qui sert à ranger
            ► DESC_ou_ASC (str) : ordre de rangement

        Renvoie:
            Rien

        Effets de Bord:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    txt = 'SELECT '
    for i in range(len(categories1)):
        txt = txt + categories1[i] + ','
    txt = txt[:-1]
    txt = txt + ' FROM ' + nom_table + ' ORDER BY ' + categorie2  + ' ' + DESC_ou_ASC + ";"
    for ligne in curseur.execute(txt):
        print(ligne)

def filtre_join(categories1, nom_table1, nom_table2, categorie_join):
    '''
        Fonction qui permet de filtrer et de faire une distinction sur
        les données qui seront affichées.

        Paramètres:
            ► categories1 (list) : Liste des catégories qui seront affichées
            ► nom_table1 (str) : Nom de la table d'où proviennent les données affichées
            ► nom_table2 (str) : Nom de la catégorie qui sert à la jointure
            ► categorie_join (str) : Nom de la catégorie utilisée pour la jointure

        Renvoie:
            Rien

        Effets de Bord:
            ► connexion
            ► curseur
    '''
    global curseur
    global connexion
    txt = 'SELECT '
    for i in range(len(categories1)):
        txt = txt + categories1[i] + ','
    txt = txt[:-1]
    txt = txt + ' FROM ' + nom_table1 + ' JOIN ' + nom_table2 + " ON " + nom_table1 + "." + categorie_join + " = " + nom_table2 + "." + categorie_join + ";"
    print(txt)
    for ligne in curseur.execute(txt):
        print(ligne)

def renommer_colonne(nom_table, ancien_nom, nouveau_nom):
    '''
        Fonction qui permet de renommer une colonne dans une table donnée.

        Paramètres:
            ► nom_table (str) : Nom de la table dans laquelle se trouve la colonne à modifier
            ► ancien_nom (str) : Ancien nom de la colonne
            ► nouveau_nom (str) : Nouveau nom que l'on souhaite donner à la colonne

        Renvoie:
            Rien

        Effets de Bord:
            ► connexion
            ► curseur
    '''
    global connexion
    global curseur
    txt = "ALTER TABLE " + nom_table + " RENAME COLUMN " + ancien_nom + " TO " + nouveau_nom + ";"
    print(txt)
    curseur.execute(txt)
    connexion.commit()

