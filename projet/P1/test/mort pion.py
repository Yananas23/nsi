Tableau=[   [0,4,0,4,0],
            [3,5,3,5,3],
            [0,4,0,4,0],
            [3,5,3,5,3],
            [0,4,0,4,0]]

for i in range(5):
    for j in range(5):
        if Tableau[i][j]==0:
            print(' ',end='')
        elif Tableau[i][j]==1:
            print('X',end='')
        elif Tableau[i][j]==2:
            print('O',end='')
        elif Tableau[i][j]==3:
            print('-',end='')
        elif Tableau[i][j]==5:
            print('+',end='')
        else:
            print('|',end='')
    print('')