# Créé par angelina-marie.caron, le 15/11/2021 en Python 3.7

import pandas as pd
import sqlite3

con = sqlite3.connect('Repertoire_Projet.db')
cur = con.cursor()


def ouverture_base(Repertoire_Projet):
  '''
  Fonction servant à ouvrir la base de données en paramètres.

  '''
  con = sqlite3.connect('Repertoire_Projet.db')
  cur = con.cursor()


def fermeture_base(Repertoire_Projet):
    '''
    Fonction servant à fermer la base de données en paramètres.

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    con.close()
    return con.close

def table_pers():
    '''
    Fonction servant à créer la table "personne".

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE personne
                     (id text PRIMARY KEY, nom text, prenom text, numero_pers text )''')
    con.commit()



def table_numero():
    '''
    Fonction servant à créer la table "numéro".

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE numéro
                       (numéro int PRIMARY KEY, type text )''')
    con.commit()



def table_adresse():
    '''
    Fonction servant à créer la table "adresse".

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE adresse
                       (adresse text PRIMARY KEY, rue text, code int, ville text)''')
    con.commit()


def table_adresse_mail():
    '''
    Fonction servant à créer la table "adresse_mail".

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE adresse_mail
                       (mail text PRIMARY KEY, type text)''')
    con.commit()

def table_contact():
    '''
    Fonction servant à créer la table "contact".

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE contact
                       (nom text, prenom text, adresse text, mail text, numéro text, id_contact PRIMARY KEY text)''')
    con.commit()



def ajout_donnees(table_pers):
    '''
    Fonction servant à ajouter des données dans la table "personne" qui est en paramètres.

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute[("INSERT INTO personne VALUES ('001', 'Caron', 'Angélina-Marie', '0755754215')")
                ("INSERT INTO personne VALUES ('002', 'Caron', 'Emanuel', '0123456789')")
                ("INSERT INTO personne VALUES ('003', 'Duez', 'Annie', '0134567891')")
                ("INSERT INTO personne VALUES ('004','Chepaki', 'Chepakoi', '0145678912')") ]
    con.commit()


def ajout_donnees(table_numero):
    '''
    Fonction servant à ajouter des données dans la table "numéro" qui est en paramètres.

    '''
    cur.execute[("INSERT INTO numéro VALUES ('0755754215', '0223456789')")
                ("INSERT INTO numéro VALUES ('0123456789', '0234567891)")
                ("INSERT INTO numéro VALUES ('0134567891', '0245678912')")
                ("INSERT INTO numéro VALUES ('0145678912', '0256789123')")]
    con.commit()


def ajout_donnees(table_adresse):
    '''
    Fonction servant à ajouter des données dans la table "adresse" qui est en paramètres.

    '''
    cur.execute[("INSERT INTO adresse VALUES ('', 'Dr Calmette', '134', 'Lambres-lez-Douai')'")
                ("INSERT INTO adresse VALUES ('', 'Cité Vandamne', '2', 'Roubaix')")
                ("INSERT INTO adresse VALUES ('', 'Cité Vandamne', '2', 'Roubaix')")
                ("INSERT INTO adresse VALUES ('', 'Chepaou', '1', 'Chepawou')")]
    con.commit()


def ajout_donnees(table_adresse_mail):
    '''
    Fonction servant à ajouter des données dans la table "adresse_mail" qui est en paramètres.

    '''
    cur.execute[("INSERT INTO adresse_mail VALUES ('angelinamarie.caron@gmail.com')")
                ("INSERT INTO adresse_mail VALUES ('emanuel.caron@gmail.com')")
                ("INSERT INTO adresse_mail VALUES ('annie.duez@gmail.com', 'annie.duez.pro@gmail.com)")
                ("INSERT INTO adresse_mail VALUES ('chepaki.chepakoi@gmail.com', 'chepaki.chepakoi.pro@gmail.com')")]
    con.commit()


def ajout_donnees(table_contact):
    '''
    Fonction servant à ajouter des données dans la table "contact" qui est paramètres.

    '''
    cur.execute[("INSERT INTO contact VALUES ('001AM', 'Caron', 'Angélina-Marie', '134 Rue du Dr Calmette Lambres-lez-Douai', 'angelinamarie.caron@gmail.com', '0755754215')")
                ("INSERT INTO contact VALUES ('002E', 'Caron', 'Emanuel', '2 Rue Cité Vandamne Roubaix', 'emanuel.caron@gmail.com', '0123456789')")
                ("INSERT INTO contact VALUES ('003A', 'Duez', 'Annie', '2 Rue Cité Vandamne Roubaix', 'annie.duez@gmail.com', '0134567891')")
                ("INSERT INTO contact VALUES ('004C', 'Chepakoi', 'Chepaki', '1 Rue Chepaou Chepawou', 'chepaki.chepakoi@gmail.com', '0145678912')")]
    con.commit()


def suppression_donnees(table_pers):
    '''
    Fonction servant à supprimer des données de la table "personne" qui est en paramètre.

    '''
    cur.execute("DELETE FROM personne WHERE nom = 'Caron' ")
    con.commit()


def modifier_donnees(table_pers):
    '''
    Fonction servant à modifier des données de la table "personne" qui est en paramètres.

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute("UPDATE personne SET nom = 'CARON' WHERE nom = 'Caron'")
    con.commit()


def requêtes():
    '''
    Fonction servant à faire des requêtes.

    '''
    con = sqlite3.connect('Repertoire_Projet.db')
    cur = con.cursor()

    cur.execute("SELECT DISTINCT nom FROM personne")
    con.commit()











