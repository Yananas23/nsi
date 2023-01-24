class Date:
    def __init__(self, j, m, a):
        self.jour = j
        self.mois = m
        self.annee = a

    def __str__(self):
        noms_mois = {'1' : 'Janvier', '2' : 'Février', '3' : 'Mars', '4' : 'Avril', '5' : 'Mai', '6' : 'Juin', '7' : 'Juillet', '8' : 'Août', '9' : 'Septembre', '10' : 'Octobre', '11' : 'Novembre', '12' : 'Décembre'}
        return str(self.jour) + ' ' + noms_mois[str(self.mois)] + ' ' + str(self.annee)

    def __lt__(self, d2):
        if self.annee < d2.annee:
            return True
        elif (self.mois < d2.mois) and (self.annee == d2.annee):
            return True
        elif (self.jour < d2.jour) and (self.mois == d2.mois):
            return True
        else:
            return False

    def est_bissextile(self):
        if self.annee % 4 == 0:
            return True
        else:
            return False
