# Créé par yanis.boulogne, le 04/10/2021 en Python 3.7
import requests


def positions_iss():
    '''
    donne la positions de l'ISS à un instant T

    aucun paramètre
    renvoi:
        rep = positions de l'ISS
    '''
    URL = """http://api.open-notify.org/iss-now.json"""
    rep = requests.get(URL)
    return (rep.json())

def personne_iss():
    '''
    donne les personnes présentes dans l'ISS à un instant T

    aucun paramètre
    renvoi:
        rep = personnes de l'ISS
    '''
    URL = """http://api.open-notify.org/astros.json"""
    rep = requests.get(URL)
    return (rep.json())

def passage_iss(pos1, pos2):
    '''
    vérifie la positions de l'ISS

    paramètre:
        pos1 (float) = longitude sur la Terre
        pos2 (float) = latitude sur la Terre
    renvoi:
        rep = True or False
    '''
    #URL = """http://api.open-notify.org/iss-now.json"""
    #rep = requests.get(URL)

    rep = {"timestamp": 1633338245, "iss_position": {"longitude": "-62.7459", "latitude": "-50.8150"}, "message": "success"}

    if rep["iss_position", "iss_position":"longitude"] == pos1 and rep["iss_position", "iss_positions":"latitude"] == pos2:
        return True
    else:
        return False
