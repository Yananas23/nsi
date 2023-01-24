def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a > 0 :
        bin_a = str(a%2) + bin_a
        a = a // 2
    return bin_a

def nb_repetitions(elt, tab):
    repetitions = 0
    for i in range(len(tab)):
        if elt == tab[i]:
            repetitions = repetitions + 1
    return repetitions