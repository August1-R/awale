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

def defautCoups(joueur):
    if joueur == 0:
        return [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5]]
    else:
        return [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5]]

def plateauAdverseNonVide(coup, plateau):
    afterPlay = jouercoup(coup, plateau)
    joueur = coup[1]
    for i in afterPlay[joueur]:
        if i != 0:
            return True
    return False

def coupsPossibles(Plateau, joueur):
    coupsPossibles = []
    defaut = defautCoups(joueur)
    for coup in defaut:
        if Plateau[coup[0], coup[1]] != 0 and plateauAdverseNonVide():
            coupsPossibles.append(coup)



print(coupsPossibles(initialisationPlateau(),1))