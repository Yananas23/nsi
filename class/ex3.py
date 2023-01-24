# Créé par Yanis Boulogne, le 08/11/2021 en Python 3.7
class Temps :

    def __init__(self, heure, minute, seconde):
        self.heure = heure
        self.minute = minute
        self.seconde = seconde

    def Horraire_heure(self):
        h = str(self.heure) + ' heure'
        if self.heure > 1:
            h = h + "s"
        h = h + " "
        return h

    def Horraire_minute(self):
        m = str(self.minute) + ' minute'
        if self.minute > 1:
            m = m + "s"
        m = m + " "
        return m

    def Horraire_seconde(self):
        s = str(self.seconde) + ' seconde'
        if self.seconde > 1:
            s = s + "s"
        s = s + " "
        return s

    def __lt__(self, H2):
        if self.seconde < H2.seconde :
            return True
        elif (self.minute < H2.minute) and (self.seconde == H2.seconde):
            return True
        elif (self.heure < H2.jour) and (self.minute == H2.minute) and (self.seconde == H2.seconde):
            return True
        else :
            return False

    def __str__(self ):
        return self.Horraire_heure() + self.Horraire_minute() +" et " + self.Horraire_seconde()
