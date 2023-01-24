# Créé par yanis.boulogne, le 08/11/2021 en Python 3.7
class Date :

    def __init__(self, jour, mois, annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def af_FR(self):
        noms_mois = {"1" : "Janvier", "2" : "Février", "3" : "Mars", "4" : "Avril", "5" : "mai", "6" : "juin", "7" : "juillet", "8" : "Aout", "9" : "Septembre", "10" : "Octobre", "11" : "Novembre", "12" : "Décembre"}
        date_FR = str(self.jour) + ' ' + noms_mois[str(self.mois)] + ' ' + str(self.annee)
        return date_FR

    def __lt__(self, d2):
        if self.annee < d2.annee :
            return True
        elif (self.mois < d2.mois) and (self.annee == d2.annee):
            return True
        elif (self.jour < d2.jour) and (self.mois == d2.mois) and (self.annee == d2.annee):
            return True
        else :
            return False


    """def __lt__(self, d2):
        if self.annee > d2.annee :
            return True
        elif (self.mois > d2.mois) and (self.annee == d2.annee):
            return True
        elif (self.jour > d2.jour) and (self.mois == d2.mois) and (self.annee == d2.annee):
            return True
        else :
            return False"""

    def af_ENG(self):
        noms_mois = {"1" : "January", "2" : "February", "3" : "March", "4" : "April", "5" : "mai", "6" : "June", "7" : "july", "8" : "August", "9" : "September", "10" : "October", "11" : "November", "12" : "Décember"}
        date_ENG = noms_mois[str(self.mois)] + ' ' + str(self.jour) + ' ' + str(self.annee)
        return date_ENG

    def __str__(self):
        return self.af_FR() + "\r" + self.af_ENG()