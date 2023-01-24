def positif(T):
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    print('T = ',T)
    return T2

def maxi(tab):
    max = tab[0]
    occurence = 0
    for i in range(1,len(tab)):
        if max < tab[i]:
            max = tab[i]
    for j in range(len(tab)):
        if tab[j] == max:
            occurence = j
            return (max,occurence)
