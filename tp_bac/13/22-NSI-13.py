class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element)
        nouveau_maillon.suivant = self.dernier_file
        self.dernier_file = nouveau_maillon

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :
            print(maillon.valeur)
            maillon = maillon.suivant

    def defile(self) :
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = self.dernier_file
            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = maillon.suivant.valeur
            maillon.suivant = None
            return resultat
        return None

def rendu(somme_a_rendre):
    argent = [0,0,0]
    while somme_a_rendre != 0:
        if somme_a_rendre >= 5:
            somme_a_rendre = somme_a_rendre - 5
            argent[0] = argent[0] + 1
        elif somme_a_rendre >= 2:
            somme_a_rendre = somme_a_rendre - 2
            argent[1] = argent[1] + 1
        else:
            somme_a_rendre = somme_a_rendre - 1
            argent[2] = argent[2] + 1
    return argent