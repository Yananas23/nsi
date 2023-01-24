# Créé par hugol, le 16/12/2021 en Python 3.7
import sqlite3
con = ""
cur = ""

def ouverture(source):
    '''
    Fonction qui permet d'ouvrir la base de données
    '''
    global con, cur
    con = sqlite.connect(source)
    cur = con.cursor()

def fermeture(source):
    '''
    Fonction qui permet de fermer la base de données
    '''
    global con
    con.close


def element(source):
    '''
    Créé la table Elements de la base de données
    '''
    global cur
    cur.execute ('''CREATE TABLE Elements(id_element INT PRIMARY KEY,
                    nom,
                    INSERT INTO element VALUES (None),
                    INSERT INTO element VALUES (Eau),
                    INSERT INTO element VALUES (Feu),
                    INSERT INTO element VALUES (Foudre),
                    INSERT INTO element VALUES (Dragon),
                    INSERT INTO element VALUES (Flamme_Noire);
                    ''')

def statuts(source):
    '''
    Crée la table Statuts de la base de données
    '''
    global cur
    cur.exeute ('''CREATE TABLE Statuts(id_statuts INT PRIMARY KEY, nom
                    INSERT INTO statuts VALUES (Paralysie),
                    INSERT INTO statuts VALUES (Poison),
                    INSERT INTO statuts VALUES (Defense basse),
                    INSERT INTO statuts VALUES (Puanteur),
                    INSERT INTO statuts VALUES (Etourdissement),
                    INSERT INTO statuts VALUES (Fleau-Eau),
                    INSERT INTO statuts VALUES (Sommeil),
                    INSERT INTO statuts VALUES (Fleau-Feu),
                    INSERT INTO statuts VALUES (Fleau-Feu Severe),
                    INSERT INTO statuts VALUES (Fleau-Poisse),
                    INSERT INTO statuts VALUES (Fleau-Foudre),
                    INSERT INTO statuts VALUES (Fleau-Foudre Severe),
                    INSERT INTO statuts VALUES (Fleau-Dragon),
                    INSERT INTO statuts VALUES (None);''')

def monstres(source):
    '''
    crée la table monstres de la base de donnéees
    '''
    global cur
    cur.exeute('''CREATE TABLE Monstres(id_monsstres,
                Nom,
                Element REFERENCES id_element,
                Faiblesses REFERENCES id_element,
                Statuts REFERENCES id_statuts;
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Apceros','None', 'Foudre','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Aptonoth','None', 'Feu','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Bullfango','None', 'Foudre, Feu'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Gerprey','None', 'Eau, Foudre, Glace', 'Paralysie'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Hormetaur','None', 'Poison','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Loprey','None', 'Eau','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Kelbi','None','None','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Mosswine','None','None','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Velociprey','None','None','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Vespoid','None', 'Poison', 'Paralysie'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Diablos','None', 'Glace','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Gemdrome','None', 'Foudre, Glace', 'Paralysie'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Gypceros','None', 'Feu', 'Poison , Etourdissement'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Iodrome','None', 'Foudre', 'Poison'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Monoblos','None', 'Foudre','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Velocidrome','None', 'Foudre, Glace', 'Puenteur, Defense Basse'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Luo-Shan Lung','None', 'Dragons','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Diablos Noire','None', 'Glace','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Gypceros Amethyste','None', 'Feu','Poison, Etourdissement'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Monobloss Iugine','None', 'Foudre', 'Paralysie','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Basarios','Feu','Dragon, Eau','Poison, Sommeil, Fleau-Feu, Fleau-Feu Severe'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Gravios','Feu,'Eau','Sommeil, Poison, Fleau-Feu, Fleau-Feu Severe'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Rathalos','Feu','Gace, Eau, Dragon, Foudre','Etourdissement, Poison, Fleau-Feu, Fleau-Feu Severe'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Rathian','Feu','Dragon, Foudre','Poison, Fleau-Feu, Fleau-Feu Severe'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Yian Kut-Ku','Feu','Eau, Glace','Fleau-Feu'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Rathalos Azur','Feu','Dragon, Glace','Etourdissement, Poison, Fleau-Feu, Fleau-Feu Severe'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Gravios Onyx','Feu','Eau','Sommeil'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Yian Kut-Ku Bleu','Feu','Eau, Foudre','Fleau-Feu'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Rathian Sakura','Feu','Dragon, Foudre','Poison'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Rathian d Or','Feu','Foudre, Eau','Fleau-Feu, Poison'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Fatalis Pourpre','Feu','Dragon, Glace','Fleau-Poisse, Fleau-Feu'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Yian Garuga','Feu','Eau','Poison'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Khezu','Foudre',' Feu',' Paralysie, Fleau-Foudre, Fleau-Foudre severe'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Kirin','Foudre','Eau, Feu','Paralysie'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Khezu Grenat','Foudre','Eau','Paralysie'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Luo-Shang Lung cendre','Dragon','Dragon','None',),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Fatalis Pourpre','Dragon','Dragon, Glace','Fleau-Poisse, Fleau-Feu'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Fatalis','Flamme Noire','Dragon','Fleau-Feu, Fleau-Feu severe, Fleau-Dragon'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Popo','None','Feu','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Hermytaur','None','Foudre','None'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Fatalis ancien','Foudre,Dragon','Dragon, Feu','Fleau-Foudre, Fleau-Dragon'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Yama Tsukami','None','Dragon, Glace','Paralysie'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Kushala Daora','Dragon, Glace, Feu','Dragon, Foudre','Bonhomme de neige, Fleau-Glace, Fleau-Glace severe, Defense Basse'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Rajang','Foudre','Glace, Terre','Fleau-Foudre, Fleau-Feu, Fleau-Glace'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Lunastra','Feu, Dragon','Dragon, Glace','Fleau-Feu'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Teostra','Feu, Dragon','Dragon, Eau','Fleau-Feu, Fleau-Poisse'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Nargacuga','None','Foudre, Feu','Poison, Laceration'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Barioth','Glace','Feu, Foudre','Bonhomme de neige, Fleau-Glace'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Tigrex Berserk','None','Eau','Fleau-Feu, Fleau-Feu severe, Fleau-Eau, Fleau-Eau severe, Fleau-Glace, Mort Vivant'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Zinogre','Foudre','Glace, Eau','Fleau-Foudre, Fleau-Foudre severe'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Amatsu','Eau','Dragon, Feu','Fleau-Eau'),
                INSERT INTO monstres (id_monstres, Nom, Element, Faiblesses, Statut) VALUES ('Nargacuga Selenite','None','Glace, Dragon','Poison');'''

def affichage():
    return monstres
    return statuts
    return elements

