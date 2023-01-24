# Créé par yanis.boulogne, le 16/03/2022 en Python 3.7

def chiffrer_secret(txt_cl,cle):
    txt_chf=''
    ltr_chf={}
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    cle_bis = list(cle)
    for i in range(len(cle_bis)):
            ltr_chf[alphabet[i]] = cle_bis[i]
            cle_bis.pop

    for lettre in txt_cl:
        if 65 <= ord(lettre) <= 90:
            txt_chf = txt_chf + ltr_chf[lettre]

        elif 97 <= ord(lettre) <= 122:
            lettre = str.upper(lettre)
            lettre = ltr_chf[lettre]
            lettre = str.lower(lettre)
            txt_chf = txt_chf + lettre

        else :
            txt_chf = txt_chf + lettre

    return txt_chf,cle


def dechiffrer_secret(txt_chf,cle):
    txt_cl=''
    ltr_chf={}
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    cle_bis = list(cle)
    for i in range(len(cle_bis)):
            ltr_chf[cle_bis[i]] = alphabet[i]
            cle_bis.pop

    for lettre in txt_chf:
        if 65 <= ord(lettre) <= 90:
            txt_cl = txt_cl + ltr_chf[lettre]

        elif 97 <= ord(lettre) <= 122:
            lettre = str.upper(lettre)
            lettre = ltr_chf[lettre]
            lettre = str.lower(lettre)
            txt_cl = txt_cl + lettre

        else :
            txt_cl = txt_cl + lettre

    return txt_cl,cle