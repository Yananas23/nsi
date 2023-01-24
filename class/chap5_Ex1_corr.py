import math

class Angle:
    def __init__(self, m : int) -> None:
        """Constructeur de l'objet Angle
        """
        self.__angle = m

    def mesure(self) -> int:
        """Renvoie la mesure de l'objet Angle
        """
        return self.__angle

    def __str__(self):
        txt = str(self.mesure()) + ' degré'
        if self.mesure() > 1:
            txt = txt + 's'
        return txt

    def ajoute(self, ang) -> None:
        """Ajoute la mesure de l'angle passé en paramètre
        """
        self.__angle = self.__angle + ang.__angle

    def cos(self):
        return math.cos(self.mesure() * math.pi / 180)

    def sin(self):
        return math.sin(self__angle * math.pi / 180)

def cosinus(an):
    return math.cos(an.mesure() * math.pi / 180)