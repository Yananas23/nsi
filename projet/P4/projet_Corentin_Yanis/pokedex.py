# importation du module tkinter
import tkinter as tk
# Chargement du module font
import tkinter.font as tkFont
# Chargement du module ttk
import tkinter.ttk as ttk
# Chargement du module sqlite3
import sqlite3
# Chargement du module mixer de pygame pour lire mp3
from pygame import mixer
# initialisation de mixer pour lire un mp3
mixer.init()
# ###########################################
#    Base données                           #
# ###########################################

connexion = None
curseur = None

# Création de la connexion
def creer_connection(db_fichier):
    """
    Crée une connection à une base de données spécifiée dans l'argument db_fichier
    :param db_fichier:
        chemin du fichier de la base de données sous la forme d'une chaine de caractères
    :return:
        objet de connection or None
    """
    global connexion
    global curseur
    connexion = sqlite3.connect(db_fichier)
    curseur = connexion.cursor()
    return

# fonction de recherche de la liste des pokemons disponibles
def recherche_pokemons():
    '''
    renvoie la liste des pokemons de la base rangé par ordre alphabetique
    arguments:
        aucun
    return:
        list
    exemple
        return = ['Abo', 'Abra', 'Absol', 'Aflamanoir'......]
    '''
    #possibilite de mettre les nom anglais
    global connexion
    global curseur
    L = []
    creer_connection('pokemon.db')
    curseur.execute('SELECT nom FROM pokemon ORDER BY nom ASC;')
    resultat = curseur.fetchall()
    for ligne in resultat:
        L.append(ligne[0])
    return L


# fonction de recherche du nombre de Pokemons dans le pokedex
def nombre_pokemons():
    """
    renvoie le nombre de pokemons presents dans le pokedex
    argument:
        aucun
    return:
        int
    exemple:
         nombre_pokemons=893
    """
    curseur.execute('SELECT COUNT(*) AS nb_pokemon FROM pokemon;')
    nb_pikomon = curseur.fetchall()
    return nb_pikomon[0]

# fonction de recherche des attributs d'un pokemon
def recherche_attributs_pokemon(nom_pokemon):
    """
    crée une classe de type Pokemon avec les attributs
            self.id:int
            self.name:str
            self.nom:str
            self.pv : int
            self.attaque :int
            self.defense :int
            self.attaque_speciale :int
            self.defense_speciale :int
            self.vitesse:int
            self.evolution_de:str (Le nom du pokemon et pas son identifiant)
            self.description:str
    et
    renvoie un objet de type Pokemon avec les atributs instanciés
    en fonction du nom du pokemon donné en argument
    argument:
        nom_pokemon: string
    return:
        pokemon: Pokemon

    """
    creer_connection('pokemon.db')
    global curseur
    global connexion

    while type(nom_pokemon) != str:
        nom_pokemon = nom_pokemon[0]

    curseur.execute('SELECT id FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    id_p1 = curseur.fetchall()
    id_p2 = list(id_p1[0])
    id_p = id_p2[0]

    curseur.execute('SELECT name FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    name_p1 = curseur.fetchall()
    name_p2 = list(name_p1[0])
    name_p = name_p2[0]

    curseur.execute('SELECT nom FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    nom_p1 = curseur.fetchall()
    nom_p2 = list(nom_p1[0])
    nom_p = nom_p2[0]

    curseur.execute('SELECT pv FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    pv_p1 = curseur.fetchall()
    pv_p2 = list(pv_p1[0])
    pv_p = pv_p2[0]

    curseur.execute('SELECT attaque FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    att_p1 = curseur.fetchall()
    att_p2 = list(att_p1[0])
    att_p = att_p2[0]

    curseur.execute('SELECT defense FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    def_p1 = curseur.fetchall()
    def_p2 = list(def_p1[0])
    def_p = def_p2[0]

    curseur.execute('SELECT attaque_speciale FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    att_spe_p1 = curseur.fetchall()
    att_spe_p2 = list(att_spe_p1[0])
    att_spe_p = att_spe_p2[0]

    curseur.execute('SELECT defense_speciale FROM pokemon WHERE nom=' + "'" + nom_pokemon +"'" + ';')
    def_spe_p1 = curseur.fetchall()
    def_spe_p2 = list(def_spe_p1[0])
    def_spe_p = def_spe_p2[0]

    curseur.execute('SELECT vitesse FROM pokemon WHERE nom=' + "'" + nom_pokemon + "'" + ';')
    vit_p1 = curseur.fetchall()
    vit_p2 = list(vit_p1[0])
    vit_p = vit_p2[0]

    curseur.execute('SELECT evolution_de FROM pokemon WHERE nom=' + "'" + nom_pokemon + "'" + ';')
    id_evo = curseur.fetchall()
    if id_evo == [(None,)]:
        curseur.execute('SELECT nom FROM pokemon WHERE id=' + str(id_p) + ';')
        evo_p = '---'
    else :
        id_evo1 = list(id_evo[0])
        id_evo2 = id_evo1[0]
        curseur.execute('SELECT nom FROM pokemon WHERE id=' + str(id_evo2) + ';')
        evo_p1 = curseur.fetchall()
        evo_p2 = list(evo_p1[0])
        evo_p = evo_p2[0]

    curseur.execute('SELECT description FROM pokemon WHERE nom=' + "'" + nom_pokemon + "'" + ';')
    desc_p1 = curseur.fetchall()
    desc_p2 = list(desc_p1[0])
    desc_p = desc_p2[0]


    class pokemon():
        def __init__(self,id_p,name,nom,pv,attaque,defense,attaque_spe,defense_spe,vitesse,evolution_de,description):
            self.id = id_p
            self.name = name_p
            self.nom = nom_p
            self.pv = pv_p
            self.attaque = att_p
            self.defense = def_p
            self.attaque_speciale = att_spe_p
            self.defense_speciale = def_spe_p
            self.vitesse = vit_p
            self.evolution_de = evo_p #(Le nom du pokemon et pas son identifiant)
            self.description = desc_p

    pokemon_a_afficher = pokemon(id_p,name_p,nom_p,pv_p,att_p,def_p,att_spe_p,def_spe_p,vit_p,evo_p,desc_p)

    return pokemon_a_afficher


# fonction recherche des évolutions du pokemon
def recherche_evolutions(nom_pokemon):
    """
    renvoie la liste des évolutions d'un pokemon
    Argument:
        nom_pokemon:str
    Return:List
    exemple:
        return =['Aquali', 'Givrali', 'Mentali', 'Noctali', 'Nymphali', 'Phyllali', 'Pyroli', 'Voltali']
    """
    creer_connection('pokemon.db')
    global curseur
    global connexion
    list_evo = []
    pokemon=recherche_attributs_pokemon(nom_pokemon)
    id_p=pokemon.id

    curseur.execute('SELECT nom FROM pokemon WHERE evolution_de=' + str(id_p) +' ORDER BY nom ASC;')
    evo_poke = curseur.fetchall()
    for i in range(len(evo_poke)):
        list_evo.append(evo_poke[i][0])
    return list_evo

def recherche_types(nom_pokemon):
    """
    Cette fonction renvoie la liste des types du pokemon spécifié en argument
    argument:
        nom_pokemon:str
    return:
        list
    exemple:
        liste=['Acier', 'Vol']
    """
    creer_connection('pokemon.db')
    global curseur
    global connexion
    Liste=[]
    pokemon=recherche_attributs_pokemon(nom_pokemon)
    id_p=pokemon.id

    curseur.execute('SELECT id_type FROM est_de_type WHERE id_pokemon=' + "'" + str(id_p) + "'" + ';')
    id_type=curseur.fetchall()

    for i in range(len(id_type)):
        curseur.execute('SELECT nom FROM type WHERE id=' + "'" + str(id_type[i][0]) + "'" + ';')
        type_poke=curseur.fetchall()
        Liste.append(type_poke[0][0])
    return Liste


# ###########################################
#    Interface TKinter                      #
# ###########################################
# Création de la fenetre en mémoire
fenetre = tk.Tk()
# réglage taille de la fenetre
# fenetre.geometry('largeur x hauteur')
fenetre.geometry("1300x900")
# Titre de la fenêtre
fenetre.title("POKEDEX")
# couleur de fond (voir liste des couleurs)
fenetre['background']="white"
# fenetre non redimensionnable en largeur,hauteur
fenetre.resizable(False, False)
# Création d'un Canvas
monCanvas = tk.Canvas(fenetre, width=1300, height=900, bg="white")
monCanvas.place(x=0,y=0)
# Chargement d'une image
monFond=tk.PhotoImage(file="img/fond.png")
# Transfert et placement de l'image dans le canvas
monItem=monCanvas.create_image(0,0,image=monFond, anchor="nw")
# Création d'une fonte
maFont= tkFont.Font(family='Arial', size=18)
# création listebox
maListeBox=tk.Listbox(fenetre,width=39,height=10,borderwidth=0,selectborderwidth =0,selectmode='single',font=maFont,highlightthickness=0)
# placement dans la fenetre
maListeBox.place(x=44,y=217)
# recherche de la liste des pokemons
liste_pokemons=recherche_pokemons()
# remplissage de la listebox
if liste_pokemons != None:
    for nom in liste_pokemons:
        maListeBox.insert('end',nom)
maListeBox_flag=True

# fonction boutonVert_clic
def boutonVert_clic(event):
    # Si la listbox est active
    if maListeBox_flag==True:
        # On récupère le nom de pokemon sélectionné
        valeur=maListeBox.curselection()
        # S'il n'y avait rien de sélectionné
        if valeur==():
            # On affiche un message d'erreur dans la console
            print("rien n'a été sélectionné")
        # S'il y a bien un nom séléctionné
        else:
            # On récupère le nom du pokemon sélectionné
            nom_pokemon=maListeBox.get(valeur[0])
            # On lance l'affichage du pokemon
            affiche_pokemon(nom_pokemon)

# doubleclic sur la liste box
maListeBox.bind('<Double-Button-1>',boutonVert_clic)

# un bouton vert
img_bouton_vert = tk.PhotoImage(file='img/bouton_vert.png')
boutonVert = tk.Button(fenetre, image=img_bouton_vert)
boutonVert.place(x=80,y=550)
maFontBouton=tkFont.Font(family='Arial', size=12, weight='bold')
label_boutonVert=tk.Label(fenetre, text="Pokedex", font=maFontBouton, background="#DC0A2D",foreground="white")
label_boutonVert.place(x=85,y=640)
# evenement clic sur boutonVert
boutonVert.bind('<Button-1>',boutonVert_clic)

# objet graphique de la fenêtre d'affichage
# les fontes
maFont2= tkFont.Font(family='Arial', size=20, weight='bold')
maFont3= tkFont.Font(family='Arial', size=15, weight='bold')
# Les objets
# Chargement d'une image
image_face=tk.PhotoImage(file="img/fond_pokemon.png")
image_dos=tk.PhotoImage(file="img/fond_pokemon.png")
image_face_pokemon=monCanvas.create_image(730,50,image=image_face, anchor="nw")
image_dos_pokemon=monCanvas.create_image(890,50,image=image_dos, anchor="nw")
image_art=tk.PhotoImage(file="img/fond_art_pokemon.png")
image_art_pokemon=monCanvas.create_image(900,640,image=image_art, anchor="nw")
image_type1_file=tk.PhotoImage(file="img/fond_type.png")
image_type2_file=tk.PhotoImage(file="img/fond_type.png")
image_type1=monCanvas.create_image(1100,70,image=image_type1_file, anchor="nw")
image_type2=monCanvas.create_image(1100,100,image=image_type2_file, anchor="nw")
# Creation des labels du pokedex en mémoire
label_nom=tk.Label(fenetre, text="Nom:", font=maFont2, foreground="black", background="white")
label_nom.place(x=730,y=150)
label_nom_anglais=tk.Label(fenetre, text="Nom anglais:", font=maFont2, foreground="black", background="white")
label_nom_anglais.place(x=730,y=190)
label_pv=tk.Label(fenetre, text="PV:", font=maFont2, foreground="black", background="white")
label_pv.place(x=730,y=230)
label_attaque=tk.Label(fenetre, text="Attaque:", font=maFont2, foreground="black", background="white")
label_attaque.place(x=730,y=270)
label_defense=tk.Label(fenetre, text="Défense:", font=maFont2, foreground="black", background="white")
label_defense.place(x=730,y=310)
label_attaque_speciale=tk.Label(fenetre, text="Attaque spéciale:", font=maFont2, foreground="black", background="white")
label_attaque_speciale.place(x=730,y=350)
label_defense_speciale=tk.Label(fenetre, text="Défense spéciale:", font=maFont2, foreground="black", background="white")
label_defense_speciale.place(x=730,y=390)
label_vitesse=tk.Label(fenetre, text="Vitesse:", font=maFont2, foreground="black", background="white")
label_vitesse.place(x=730,y=430)
label_evolution=tk.Label(fenetre, text="Evolution de:", font=maFont2, foreground="black", background="white")
label_evolution.place(x=730,y=470)
label_description=tk.Label(fenetre, text="Description:", font=maFont2, foreground="black", background="white")
label_description.place(x=730,y=510)
label_zone_description = tk.Label ( fenetre, font=maFont3, foreground="black",width=42, height= 4, background="white",borderwidth=0)
label_zone_description.place(x=730,y=540)
# Création des labels pour recevoir les infos du pokemon sélectionné
label_attribut_nom=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_nom.place(x=980,y=150)
label_attribut_nom_anglais=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_nom_anglais.place(x=980,y=190)
label_attribut_pv=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_pv.place(x=980,y=230)
label_attribut_attaque=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_attaque.place(x=980,y=270)
label_attribut_defense=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_defense.place(x=980,y=310)
label_attribut_attaque_speciale=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_attaque_speciale.place(x=980,y=350)
label_attribut_defense_speciale=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_defense_speciale.place(x=980,y=390)
label_attribut_vitesse=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_vitesse.place(x=980,y=430)
label_attribut_evolution=tk.Label(fenetre, text="...", font=maFont2, foreground="black", background="white")
label_attribut_evolution.place(x=980,y=470)

def affiche_pokemon(nom_pokemon):
    global image_type2_file,image_type1_file,image_type1,image_type2,image_dos,image_dos_pokemon,image_face,image_face_pokemon,image_art,image_art_pokemon,pokemon
    # On demande l'objet pokemon correspondant à son nom
    pokemon=recherche_attributs_pokemon(nom_pokemon)
    # Si le pokemon obtenu n'est pas vide
    if pokemon!=None :
        # On remplit les labels du pokedex avec les attributs du pokemon
        label_attribut_nom['text']=pokemon.nom
        label_attribut_nom_anglais['text']=pokemon.name
        label_attribut_pv['text']=pokemon.pv
        label_attribut_attaque['text']=pokemon.attaque
        label_attribut_defense['text']=pokemon.defense
        label_attribut_attaque_speciale['text']=pokemon.attaque_speciale
        label_attribut_defense_speciale['text']=pokemon.defense_speciale
        label_attribut_vitesse['text']=pokemon.vitesse
        label_attribut_evolution['text']=pokemon.evolution_de
        label_zone_description["text"]=pokemon.description
        # recherche des images
        try:
            chemin_image_face="img_front/"+str(pokemon.id)+".png"
            image_face=tk.PhotoImage(file=chemin_image_face)
            monCanvas.itemconfig(image_face_pokemon,image=image_face)
        except:
            chemin_image_face="img/fond_pokemon.png"
            image_face=tk.PhotoImage(file=chemin_image_face)
            monCanvas.itemconfig(image_face_pokemon,image=image_face)
        try:
            chemin_image_dos="img_back/"+str(pokemon.id)+".png"
            image_dos=tk.PhotoImage(file=chemin_image_dos)
            monCanvas.itemconfig(image_dos_pokemon,image=image_dos)
        except:
            chemin_image_face="img/fond_pokemon.png"
            image_face=tk.PhotoImage(file=chemin_image_face)
            monCanvas.itemconfig(image_face_pokemon,image=image_face)
        try:
            chemin_image_dos="img_art/"+str(pokemon.id)+".png"
            image_art=tk.PhotoImage(file=chemin_image_dos)
            monCanvas.itemconfig(image_art_pokemon,image=image_art)
        except:
            chemin_image_art="img/fond_art_pokemon.png"
            image_art=tk.PhotoImage(file=chemin_image_art)
            monCanvas.itemconfig(image_art_pokemon,image=image_art)
        # recherche des types
        liste=recherche_types(nom_pokemon)
        # On écrase les images précendentes par l'image vierge du type
        # Création chemin image
        chemin_image_type="img/fond_type.png"
        # Chargement image
        image_type1_file=tk.PhotoImage(file=chemin_image_type)
        image_type2_file=tk.PhotoImage(file=chemin_image_type)
        # On transfere l'image dans l'item du canvas
        monCanvas.itemconfig(image_type1,image=image_type1_file)
        monCanvas.itemconfig(image_type2,image=image_type2_file)
        # Si la liste contient un seul type
        if len(liste)==1:
            # Chemin de l'image du type
            chemin_image_type1=f"img_types/{liste[0]}.png"
            # Chargement de l'image du type
            image_type1_file=tk.PhotoImage(file=chemin_image_type1)
            # On transfère l'image du type dans l'item du canvas
            monCanvas.itemconfig(image_type1,image=image_type1_file)
        # Si la liste contient 2 types
        elif len(liste)==2:
            # Chemin de l'image du type
            chemin_image_type1=f"img_types/{liste[0]}.png"
            # Chargement de l'image du type
            image_type1_file=tk.PhotoImage(file=chemin_image_type1)
            # On transfère l'image du type dans l'item du canvas
            monCanvas.itemconfig(image_type1,image=image_type1_file)
            # Chemin de l'image du type
            chemin_image_type2=f"img_types/{liste[1]}.png"
            # Chargement de l'image du type
            image_type2_file=tk.PhotoImage(file=chemin_image_type2)
            # On transfère l'image du type dans l'item du canvas
            monCanvas.itemconfig(image_type2,image=image_type2_file)



# fonction quand le bouton bleu est cliqué
def boutonBleu_clic(event):
    # on récupère le contenu de evolution_de
    evolution_de=label_attribut_evolution["text"]
    if evolution_de!="..." and evolution_de!="---":
        # si il y a une évolution à chercher
        affiche_pokemon(evolution_de)
        # on efface la listeBox
        maListeBox.delete(0,'end')
        # On insère le nom du pokemon dans la listbox
        maListeBox.insert('end',evolution_de)
        # On force la selection de l'item dans la listbox
        maListeBox.selection_set(0)


# un bouton bleu
# Cahrgement de l'image
img_bouton_bleu = tk.PhotoImage(file='img/bouton_bleu.png')
# Création de l'image en mémoire
boutonBleu = tk.Button(fenetre, image=img_bouton_bleu)
# Placement dans la fenêtre
boutonBleu.place(x=260,y=550)
# Création du texte du bouton en mémoire
label_boutonBleu=tk.Label(fenetre, text="Evolution de", font=maFontBouton, background="#DC0A2D",foreground="white")
# Placement dans la fenêtre
label_boutonBleu.place(x=250,y=640)

# evenement clic sur boutonBleu
boutonBleu.bind('<Button-1>',boutonBleu_clic)

# fonction quand le bouton rouge est cliqué
def boutonRouge_clic(event):
    global maListeBox_flag
    # Quel est le nom du pokemon courant ?
    nom_pokemon=label_attribut_nom["text"]
    # Si le nom est bien renseigné
    if nom_pokemon!="..." :
        # On cherche à obtenir la liste des évolutions du pokemon
        liste_evolutions=recherche_evolutions(nom_pokemon)
        # On efface la listeBox
        maListeBox.delete(0,'end')
        # Si la liste est vide
        if liste_evolutions==[]:
            # on insère un message dans la listbox
            maListeBox.insert('end',"Ce pokemon n'a pas d'évolution")
            # On désactive la listbox pour le clic en changeant son drapeau
            maListeBox_flag=False
        # Si La liste des évolutions est pleine
        else:
            # Pour chaque évolution
            for nom in liste_evolutions:
                # On l'insère dans la listbox
                maListeBox.insert('end',nom)
            # On active la listebox
            maListeBox_flag=True

# Pour faire un bouton rouge
# Chargement de l'image en mémoire
img_bouton_rouge= tk.PhotoImage(file='img/bouton_rouge.png')
# Création du bouton en mémoire
boutonRouge= tk.Button(fenetre, image=img_bouton_rouge)
# placement du bouton
boutonRouge.place(x=440,y=550)
# Création du texte du bouton en mémoire
label_boutonRouge=tk.Label(fenetre, text="Evolue en", font=maFontBouton, background="#DC0A2D",foreground="white")
# placement du texte
label_boutonRouge.place(x=440,y=640)

# evenement clic sur boutonRouge
boutonRouge.bind('<Button-1>',boutonRouge_clic)

# fonction quand le gros bouton est cliqué
def bouton_gros_clic(event):
    global maListeBox_flag
    # vidage de la listebox
    maListeBox.delete(0,'end')
    # remplissage de la listebox
    # Si la liste n'est pas vide
    if liste_pokemons != None:
        # Pour chaque nom dans la liste
        for nom in liste_pokemons:
            # On l'insère dans la listbox
            maListeBox.insert('end',nom)
        # On active la liste_box grace au drapeau
        maListeBox_flag=True

# Pour faire un gros bouton
# Chargement de l'image en mémoire
img_bouton_gros= tk.PhotoImage(file='img/gros_bouton.png')
# Création du bouton en mémoire
bouton_gros= tk.Button(fenetre, image=img_bouton_gros)
# Placement
bouton_gros.place(x=30,y=20)
# Création texte sous le bouton
label_bouton_gros=tk.Label(fenetre, text="Start", font=maFontBouton, background="#DC0A2D",foreground="white", borderwidth=0)
# placement du label
label_bouton_gros.place(x=67,y=140)

# evenement clic sur boutonRouge
bouton_gros.bind('<Button-1>',bouton_gros_clic)


# Pour faire un bouton_play
# Chargement de l'image
img_bouton_play= tk.PhotoImage(file='img/bouton_play.png')
# Création du bouton en mémoire
bouton_play= tk.Button(fenetre, image=img_bouton_play)
# Placement du bouton
bouton_play.place(x=275,y=690)

# fonction quand le bouton play est cliqué
def bouton_play_clic(event):
    # Quel est le nom anglais du pokemon courant
    name_pokemon=label_attribut_nom_anglais["text"]
    # Si le nom anglais est bien renseigné
    if name_pokemon!="..." :
        try :
            # Chemin du mp3
            chemin_mp3="mp3/"+name_pokemon+".mp3"
            # Chargement du mp3 en mémoire
            mixer.music.load(chemin_mp3)
            # On joue le mp3
            mixer.music.play()
        except:
            # Si erreur de chargement car pas de fichier (il en manque)
            print("Pas de fichier mp3 dans la base")


# evenement clic sur boutonRouge
bouton_play.bind('<Button-1>',bouton_play_clic)

# nombre de pokemons dans le pokedex
# Création label en mémoire
label_nbr_pokemons_texte=tk.Label(fenetre, text="Nombre de pokemons dans le pokedex", font=maFont, foreground="black", background="white")
# Placement
label_nbr_pokemons_texte.place(x=80,y=780)
# On calcule le nombre de pokemon
s=nombre_pokemons()
# création label en mémoire pour afficher s
label_nbr_pokemons=tk.Label(fenetre, text=s, font=maFont2, foreground="black", background="white")
# placement
label_nbr_pokemons.place(x=260,y=807)

# Lancement de la fenetre
fenetre.mainloop()
# Quand on ferme, on interrompt la fenetre
fenetre.quit()
