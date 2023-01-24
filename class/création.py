class Coureur():
    '''
    Une classe pour représenter une personne participant à une course
    de running.
    '''
    def __init__(self, n, p, g, d):
        '''
        Constructeur de la classe Coureur.
        '''
        self.nom = n
        self.prenom = p
        self.genre = g
        self.date_de_naissance = d
        self.dossard = None
        self.temps = None

    def est_arrive(self):
        return not (self.temps == None)


    def temps_en_str(self):
        if self.est_arrive():
            temps_chaine = ("")

            heure = self.temps // 3600
            minute = (self.temps % 3600) // 60
            seconde = self.temps % 60

            heure_str = str(heure)
            if heure < 10 :
                heure_str = "0" + heure_str

            minute_str = str(minute)
            if minute < 10 :
                minute_str = "0" + minute_str

            seconde_str = str(seconde)
            if seconde < 10 :
                seconde_str = "0" + seconde_str

            temps_chaine = str(heure_str
                        ) + ":" + str(minute_str
                        ) + ":" + str(seconde_str)

            return str(temps_chaine)
        else:
            return "le coureur n'est pas arrivé"

    def __str__(self):
        return 'BONJOUR'

    def __repr__(self):
        return 'BONsoir'

    def __sub__(self,c2):
        return self.dossard - c2.dossard



