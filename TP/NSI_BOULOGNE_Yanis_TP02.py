# Exercice 1
# ----------


class Carte:
    def __init__(self, c, v):
        """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
        assert c<4
        assert v<13
        self.Couleur = c
        self.Valeur = v

    def getNom(self):
        """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    def getCouleur(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
        return ['pique', 'coeur', 'carreau', 'trefle'][self.Couleur]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Remplit le paquet de cartes"""
        L=[]
        for c in range(1,5):
            for v in range(1,14):
                L.append((c,v))

        return L


    def getCarteAt(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        assert pos<54
        return L[pos]


# Exercice 2
# ----------

# 1)
# SELECT * FROM departement

# 2)
# SELECT code,nom FROM departement

# 3)
# SELECT SUM(pop_2012) AS population FROM villes

# 4)
# SELECT count(slug) FROM villes

# 5)
# SELECT nom,long FROM villes WHERE long>'40.000'

# 6)
# SELECT nom FROM villes ORDER BY nom ASC

# 7)
# SELECT dept,nom FROM villes WHERE dept='59' or dept='62'

# 8)
# SELECT villes.nom,departement.nom,dept FROM villes ,departement JOIN departement.code AS villes.dept