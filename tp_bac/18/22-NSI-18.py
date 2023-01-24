def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

def mini(releve, date):
    mini = releve[0]
    imini = 0
    for i in range(len(releve)):
        if mini > releve[i]:
            mini = releve[i]
            imini = i
    return(mini,date[imini])

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]