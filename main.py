'''
Le joueur False est le joueur qui a plateau[0] devant lui
Le joueur True est le joueur qui a plateau[1] devant lui
'''


def initialisationPlateau():
    return [[4,4,4,4,4,4],[4,4,4,4,4,4]]



def jouercoup(coup, plateau):
    pierre = plateau[coup[0]][coup[1]]
    plateau[coup[0]][coup[1]] = 0
    ligne = coup[0]
    colone = coup[1]
    while pierre != 0:
        if colone + 1 <= 5:
            colone += 1
        elif ligne + 1 <= 1:
                colone = 0
                ligne += 1
        else:
            colone = 0
            ligne = 0
        plateau[ligne][colone] += 1
        pierre -= 1
    gain = 0
    while True:
        if plateau[ligne][colone] <= 2 and ligne != coup[0]:
            gain += plateau[ligne][colone]
            plateau[ligne][colone] = 0
            if colone - 1 >= 0:
                colone -= 1
            else :
                return[plateau, gain]
        else:
            return[plateau, gain]


print(jouercoup([1,5,0],[[0,0,0,0,4,4],[4,4,4,0,4,10]]))