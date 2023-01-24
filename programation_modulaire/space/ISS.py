import requests

def personnes():
    '''
    Renvoie la liste des personnes actuellement à bord de l'ISS.
    :return:
    (list of str)
    '''
    url = """http://api.open-notify.org/astros.json"""
    rep = requests.get(url)
    liste_pers = rep.json()['people']
##    rep = {"message": "success", "number": 10, "people": [{"craft": "ISS", "name": "Mark Vande Hei"}, {"craft": "ISS", "name": "Oleg Novitskiy"}, {"craft": "ISS", "name": "Pyotr Dubrov"}, {"craft": "ISS", "name": "Thomas Pesquet"}, {"craft": "ISS", "name": "Megan McArthur"}, {"craft": "ISS", "name": "Shane Kimbrough"}, {"craft": "ISS", "name": "Akihiko Hoshide"}, {"craft": "ISS", "name": "Anton Shkaplerov"}, {"craft": "ISS", "name": "Klim Shipenko"}, {"craft": "ISS", "name": "Yulia Pereslid"}]}
##    liste_pers = rep['people']
    liste_retournee = []
    for pers in liste_pers:
        liste_retournee.append(pers['name'])
    return liste_retournee







def position():
    '''
    Renvoie la position de l'ISS.
    :return:
    (tupple of two floats)
    '''
    url = """http://api.open-notify.org/iss-now.json"""
    rep = requests.get(url)
    pos = rep.json()['iss_position']
##    rep = {"timestamp": 1633523181, "iss_position": {"longitude": "-61.1952", "latitude": "-14.0833"}, "message": "success"}
##    pos = rep['iss_position']
    longitude = float(pos['longitude'])
    latitude = float(pos['latitude'])
    return (latitude, longitude)











