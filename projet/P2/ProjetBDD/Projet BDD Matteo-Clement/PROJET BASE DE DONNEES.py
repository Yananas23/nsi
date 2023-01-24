# Créé par matteo.devred, le 15/12/2021 en Python 3.7
# Créé par matteo.devred, le 02/12/2021 en Python 3.7
import sqlite3
connexion= ''
curseur = ''

# -----------------------------------------------------------------------

def Ouverture():
    """
    Cette fonction permet d'ouvrir notre base de donéee
    """
    global connexion,curseur
    connexion = sqlite3.connect('mabasededonnees.db')
    curseur= connexion.cursor()

def Fermeture():
    """
     Cette fonction permet de fermer notre base de donéee
    """
    global connexion,curseur
    connexion.close()

# -----------------------------------------------------------------------

def Creation_Table_POkemon( ):
    """
    La fonction 'Creation_Table_POkemon' va permettre de creer
    la table "Pokemon" dans la base de donées et d'y ajouter un pokemon.

    """
    global connexion,curseur
    curseur.execute('''CREATE TABLE POkemon
        ("Nom_Pokemon" CHAR(20) PRIMARY KEY,"Type" CHAR(20) ,"PC" INTEGER ,"PV" INTEGER ,"Attaque" CHAR(20) , "Defense" CHAR(20))''')
    connexion.commit()

# -----------------------------------------------------------------------*

def Creation_Table_Type():
    """
    La fonction 'Creation_Table_Type' va permettre de creer
    la table "Type" dans la base de donées.
    """
    global connexion,curseur
    curseur.execute('''CREATE TABLE Type
        ( "Nom_Type" REFERENCES CHAR(20), "Type_1" CHAR(20) , "Type_2" CHAR(20) , "Legendaire" CHAR(20))''')
    connexion.commit()

# ----------------------------------------------------------------------*

def Creation_Table_Point():
    """
    La fonction 'Creation_Table_Point' va permettre de creer
    la table "Point" dans la base de donées.

    """
    global connexion,curseur
    curseur.execute('''CREATE TABLE Point
               ( "Nom_Point" REFERENCES CHAR(20), "PC" INTEGER ,"PV" INTEGER, "Total" INTEGER, "Vitesse" INTEGER )''')
    connexion.commit()

# -----------------------------------------------------------------------*

def Inserer_Valeurs_POkemon(Nom_Pokemon, Type,PC ,PV ,Attaque, Defense):
    """
    Cette fonction permet à l'utilisateur d'ajouter des valeurs dans la table
    POkemon

    Nom de la table = POkemon
    param:
        Nom_Pokemon (str) = nom du pokemon
        Type ( str) = type du pokemon
        PC (int) = points de combat
        PV (int) = points de vie
        Attaque (str) = attaque du pokemon
        Defense (str) = defense du pokemon

        exemple:

        >>> Inserer_Valeurs_POkemon('Pikachu', 'Electric', 402, 111, 'Eclair', 'Foudre')

    """
    global connexion, curseur
    curseur.execute('INSERT INTO POkemon VALUES ( "' + Nom_Pokemon + '", "' + Type + '", '+ str(PC) + ''',''' + str(PV) + ''',"''' + Attaque + '''","''' + Defense + '''")'''
                    )
    connexion.commit()

# -----------------------------------------------------------------------*

def Inserer_Valeurs_Type(Nom_Type ,Type_1,Type_2, Legendaire):
    """
    Cette fonction permet à l'utilisateur d'ajouter des valeurs
     dans la table Type

     Nom de la table = Type
     param:
        Nom_Type (str) = Nom du pokemon auquel appartient les types
        Type_1 (str) = type du pokemon (principal)
        Type_2 (str) = type du pokemon n2 (None si le pokemon n'a qu'un seul type)
        Legendaire (booleen) = oui ou non le pokemon est legendaire

     exemple:

        >>> Insert_valeur_Type('Pikachu', 'electric', None, False)


    """
    global connexion,curseur
    curseur.execute('INSERT INTO Type VALUES ( "' + Nom_Type + '", "' + Type_1 + '","' + Type_2 + "'," + Legendaire + '''")'''
                    )
    connexion.commit
# -----------------------------------------------------------------------*

def Inserer_Valeurs_Point(Nom_Point, PC,PV, Total, Vitesse):
    """
    Cette fonction permet à l'utilisateur d'ajouter des valeurs
     dans la table Point

     Nom de la table=  Point
     param:

        Nom_Point (str) = Nom du pokemon à qui appartiennent les points
        PC (int) = points de combats du pokemon
        PV (int) =points de vie
        Total (int) = total des points du pokemon
        Vitesse (int) = vitesse du pokemon

        exemple:

            >>> Inserer_Valeurs_Point('Pikachu', 402, 111, 513, 66)


    """
    global connexion,curseur
    curseur.execute('INSERT INTO POkemon VALUES ( "' + Nom_Point + '", '+ str(PC) + ''',''' + str(PV) +''',''' + str(Total)+''','''+str(Vitesse)+''')'''
                    )
    connexion.commit

# -----------------------------------------------------------------------*

def Delete_POkemon(Nom_Pokemon):
    """
    Cette fonction permet à l'utilisateur de supprimer un Pokemon
     dans la table POkemon

    Nom de la table = POkemon
    param:
            Nom_Pokemon(str)= Nom du pokémon à effacer de la table

    exemple:

        >>>Delate_Pokemon("Pikachu")

    """
    global connexion,curseur
    rq= "DELETE FROM POkemon WHERE nom =" + Nom_Pokemon + ";"
    curseur.execute(rq)
    connexion.commit()

# -----------------------------------------------------------------------*

def Delete_Type(Nom_Type):
    """
    Cette fonction permet à l'utilisateur de supprimer les attributs types point d'un pokémon
     dans la table Type


    Nom de la table = Type
    param:
            Nom_Type(str)= Nom du pokémon associé aux Type à effacer de la table

    exemple:

        >>>Delate_Type("Pikachu")


    """
    global connexion,curseur
    rq1="DELETE FROM Type WHERE nom ="+ Nom_Type + ";"
    curseur.execute(rq1)
    connexion.commit()

# -----------------------------------------------------------------------*

def Delete_Point(Nom_Point):
    """
    Cette fonction permet à l'utilisateur de supprimer les attributs point d'un pokémon
     dans la table Point


    Nom de la table = Point
    param:
            Nom_Point(str)= Nom du pokémonassocié aux Points à effacer de la table

    exemple:

        >>>Delate_Point("Pikachu")


    """
    global connexion,curseur
    rq2="DELETE FROM Point WHERE nom ="+ Nom_Point+ ";"
    curseur.execute(rq2)
    connexion.commit()


