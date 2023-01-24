import sqlite3


Open_data_base = sqlite3.connect('DataBase.db')
cursor = Open_data_base.cursor()

# Fonctions

"""def Open(base):
    """"""
    Cette fonction permet de de créer ou d'ouvrir une base de donnée.
    Le nom de celle-ci est placé en parametre.
    """"""
    global cursor, Open_data_base
    Open_data_base = sqlite3.connect(base)
    cursor = Open_data_base.cursor()"""


def Close():
    """
    Cette fonction permet de quitter en sauvegardant la base de donnée
    """
    global Open_data_base
    Open_data_base.commit()
    Open_data_base.close()

def CreateTable(table_name, attribute = []):
    """
    La fonction permet d'ajouter des attribut dans une base de donnée
    le nom de la bases et les attributs sont entrés en parametre,
    la valeur initiale du parametre attribut est [].
    Certains attribut sont déjà initialiser afin de faciliter la création
    du répertoires téléphonique

    :param:
    table_name(str)
    values(list)
    """
    global cursor, Open_data_base

    if table_name == '*':
        Identity_table()
        PhoneNumber_table()
        Repertory_table()
        Mail_address_table()
        Address_table()

    elif table_name == "Identity":
        Identity_table()

    elif table_name == "Phone_number":
        PhoneNumber_table()

    elif table_name == "Repertory":
        Repertory_table()

    elif table_name == "Mail_address":
        Mail_address_table()

    elif table_name == "Address":
        Address_table()

def Identity_table():
    """
    Fonction permettant de crée la table Identity avec les attributs associés.
    """
    cursor.execute('''CREATE TABLE Identity
    (first_name STRING,
    name TEXT,
    age INTEGER,
    Id_mail_address INTEGER PRIMARY KEY AUTOINCREMENT ,
    nationality TEXT,
    kind TEXT,
    Id TEXT,
    Id_address INTEGER
     )''')
     #Id_mail_address INTEGER PRIMARY KEY AUTOINCREMENT

def PhoneNumber_table():
    """
    Fonction permettant de crée la table Phone_number avec les attributs associés.
    """
    global cursor
    cursor.execute('''CREATE TABLE Phone_number
    ( indicatif TEXT, phone_number INT, Id_phone_number INT PRIMARY KEY
     )''')

def Repertory_table():
    """
    Fonction permettant de crée la table Repertory avec les attributs associés.
    """
    global cursor
    cursor.execute('''CREATE TABLE Repertory
    ( Id_repertory INTEGER, phone_number INT
     )''')

def Mail_address_table():
    """
    Fonction permettant de crée la table Mail_address avec les attributs associés.
    """
    global cursor
    cursor.execute('''CREATE TABLE Mail_address
    ( Id_mail_address INT PRIMARY KEY, mail_address TEXT
     )''')

def Address_table():
    """
    Fonction permettant de crée la table Address avec les attributs associés.
    """
    global cursor
    cursor.execute('''CREATE TABLE Address
    ( number INT, rue TEXT
     )''')

def Add_values(table_name, values = []):
    """
    La fonction permet d'ajouter des valeurs dans une base de donnée
    le nom de la bases et les valeurs sont entrés en parametre,
    la valeur initiale du parametre valeurs est []. Une methode
    try except est prèsente afin d'assurer
    l'unicité des valeurs de l'attribut id_address_mail.

    :param:
    table_name(str)
    values(list)
    """

    global cursor, Open_data_base

    try:
        if table_name == 'Identity':
            req = " INSERT INTO Identity VALUES(?,?,?,?,?,?,?,?)"
        elif table_name == 'Phone_number':
             req = " INSERT INTO Phone_number VALUES(?,?,?)"
        else:
             req = " INSERT INTO {} VALUES(?,?)".format(table_name)
        cursor.execute(req,values)

    except:
        values [3] = values[3] + 1
        Add_values(table_name, values)


def Supp(table_name, attribute, values):
    """
    La fonction permet de supprimer une liste de valeurs.
    La fonction recherche la table, puis dans cette table
    il recherche un attribut et une valeur, si une liste
    de valeurs la contient on la supprime;

    :param:
        table_name (str)
        attribute (str)
        values (str / int)
    """
    global cursor, Open_data_base
    req = "DELETE FROM {} WHERE {} = {}".format(table_name, attribute, values)
    cursor.execute(req)

def Edit(table_name, att, val, new_val):
    """
    La fonction permet de modifier la valeur d'un attribut peu importe la table
    et le nom de l'attribut.
    La nouvelle valeur, l'ancienne valeur, l'attribut et le nom de la table
    sont mis en parametre.
    :param:
        table_name (str)
        att (str)
        val (str / int)
        new_val (str / int)
    """
    global cursor
    req = "UPDATE {} SET {} = {} WHERE {} = {} ".format(table_name, att, val, att, new_val)
    cursor.execute(req)

def Display_filter(table_name, values = []):
    """
    La fonction permet d'afficher toute la liste d'une table en focntion de ce
    qu'on veut afficher dans la table.

    :param:
        table_name(str)
        values (list)
    """
    global cursor, Open_data_base
    req = "SELECT * FROM {}".format(table_name)
    result = cursor.execute(req)

    if table_name == 'Identity':
        dict = {'first_name' : 0, 'name': 1, 'age' : 2, 'Id_mail_address' : 3,
                'nationality' : 4, 'kind' : 5, 'Id' : 6, 'Id_address' : 7}

    elif table_name == 'Phone_number':
        dict = {'indicatif' : 0, 'phone_number' : 1, 'Id_phone_number':2}

    elif table_name == 'Address':
        dict = {'number' : 0, 'rue' : 1}

    elif table_name == 'Mail_address':
        dict = {'Id_mail_address' : 0, 'mail_address' : 1}

    else :
        dict = {'Id_repertory' : 0, 'phone_number': 1}

    for row in result:
            for i in range(len(values)):
                print(row[dict.get(values[i])], end =' ; ')
            print()



def Filter(table_name, att, values):
    """
    La fonction permet de faire une recherche filtrer en affichant tout les
    données correspondant à la valeur rechercher dans un attribut spécifique

    :param:
        table_name (str)
        att (str)
        values (str/list)
    """
    global cursor, Open_data_base
    req = "SELECT * FROM {}".format(table_name)
    result = cursor.execute(req)

    if table_name == 'Identity':
        dict = {'first_name' : 0, 'name': 1, 'age' : 2, 'Id_mail_address' : 3,
                'nationality' : 4, 'kind' : 5, 'Id' : 6, 'Id_address' : 7}
        for row in result:
            if row[dict.get(att)] == values:
                for i in range(len(dict)):
                    print(row[i])
                print('------------')

    elif table_name == 'Phone_number':
        dict = {'indicatif' : 0, 'phone_number' : 1, 'Id_phone_number':2}
        for row in result:
            if row[dict.get(att)] == values:
                print(row[0], row[1], row[2])
    else :
        if table_name == 'Address':
            dict = {'number' : 0, 'rue' : 1}

        elif table_name == 'Mail_address':
            dict = {'Id_mail_address' : 0, 'mail_address' : 1}

        else :
            dict = {'Id_repertory' : 0, 'phone_number': 1}
        for row in result:
                if row[dict.get(att)] == values:
                    print(row[0], row[1])