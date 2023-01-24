# Créé par Yanis Boulogne, le 01/11/2021 en Python 3.7
import math

class Angle():
    '''
    Une classe pour représenter un angle.
    '''
    def __init__(self, angle):
        assert isinstance(angle, int) and angle >= 0 and angle < 360

        self.angle = angle

    def __str__(self, angle):

        return (f'{angle} degrés')

    def ajoute(self, a2):
        angle = self + a2
        if angle >= 0 and angle < 360:
            return angle

    def __radian__(angle):
        angle = angle * (pi / 180)
        return angle

    def cosinus(angle):
        __radian__(angle)
        math.cos(angle)

    def sinus(angle):
        __radian__(angle)
        math.sin(angle)