def rendu_money_mem(P, V):
    mem = [0] * (len(P))
    print(mem)
    V = int(V * 100)
    return rendu_money_rec(P, V, mem)

def rendu_money_rec(P, V, m):
    nb_piece = 0
    print(V)
    print(m)

    if V <= 2:
        return nb_piece, V


    #elif m[V] > 0 :
       # return m[V]


    else :
        if V > 100 :
            m[P[0]] = rendu_money_rec(P, V - 100, m)
            return m[P[0]]

        elif V > 50 :
            m[P[1]] = rendu_money_rec(P, V - 50, m)
            return m[P[1]]

        elif V > 10 :
            m[P[2]] = rendu_money_rec(P, V - 10, m)
            return m[P[2]]

        elif V > 5 :
            m[P[3]] = rendu_money_rec(P, V - 5, m)
            return m[P[3]]

        elif V > 2 :
            m[P[4]] = rendu_money_rec(P, V - 2, m)
            return m[P[4]]