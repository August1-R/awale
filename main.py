"""
format d'un plateau : [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]      (le plateau [0] doit etre inverssé sur l'affichage)
format d'un coup :  [coordonnée X, coordonnée Y, 1 == gain possible/0 == gain impossible, nom du coup]

"""
def copiePlateau(plateau):
    """
    renvoie une copie du plateau
    """
    newplateau = [[t for t in i]for i in plateau]
    return newplateau

def initialisationPlateau():
    """
    retourne le plateau de début de partie
    """
    return [[0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 3, 0]]


def jouercoup(coup, plateau):
    """
    :param coup: les 2 premier paramètres de coup sont les position x et y du coup,
    le 3eme dit à la fonction si elle peut récupérer les pierres
    :param plateau: donne le plateau dans son état initial (avant de jouer le coup)
    :return: r'envoie le plateau une foi le coup jouer, suivi du gain réalisé par le joueur
    """
    pierre = plateau[coup[0]][coup[1]]  #on récupère les pierres du trou
    plateau[coup[0]][coup[1]] = 0   # on dit qu'il n'y a plus de pierres dans le trou

    # on pause les pierre une par une
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

    #si on peut récupérer les pierres, on le fait et on retur le plateau, sinon on reurn le plateau
    gain = 0
    if coup[2] == 1:
        while True:
            if plateau[ligne][colone] == 2 or plateau[ligne][colone] == 3 and ligne != coup[0]:
                gain += plateau[ligne][colone]
                plateau[ligne][colone] = 0
                if colone - 1 >= 0:
                    colone -= 1
                else:
                    plateau.append(gain)
                    return plateau
            else:
                plateau.append(gain)
                return plateau
    else:
        plateau.append(gain)
        return plateau

def defautCoups(joueur):
    """
    Liste de tous les coups que le joueur peut jouer
    """
    if joueur == 0:
        return [[0, 0, 1, 6], [0, 1, 1, 5], [0, 2, 1, 4], [0, 3, 1, 3], [0, 4, 1, 2], [0, 5, 1, 1]]
    else:
        return [[1, 0, 1, 1], [1, 1, 1, 2], [1, 2, 1, 3], [1, 3, 1, 4], [1, 4, 1, 5], [1, 5, 1, 6]]


def plateauAdverseNonVide(coup, plateau):
    """
    simule de jouer le coup et vérifi que le plateau adverse n'est pas vide
    """
    afterPlay = jouercoup(coup, copiePlateau(plateau))
    afterPlay.pop()

    if coup[0] == 1:
        joueurAdverse = 0
    else:
        joueurAdverse = 1

    for i in afterPlay[joueurAdverse]:
        if i != 0:
            return True
    return False


def coupsPossibles(plateau, joueur):
    """
    :param Plateau: etat du plateau avant de jouer le coup
    :param joueur: joueur a qui c'est le tour de jouer
    :return: liste de tous les coups que le joueur peut jouer
    """
    coupsPossibles = []
    defaut = defautCoups(joueur)
    for coup in defaut:
        if plateau[coup[0]][coup[1]] != 0 and plateauAdverseNonVide(coup, copiePlateau(plateau)):
            coupsPossibles.append(coup)
        else:
            coup[2] = 0
            if plateau[coup[0]][coup[1]] != 0 and plateauAdverseNonVide(coup, copiePlateau(plateau)):
                coupsPossibles.append(coup)

    return coupsPossibles

def game():
    joueur = 1
    pierresJoueur0 = 0
    pierresJoueur1 = 0
    plateau = initialisationPlateau()
    while True:
        print(plateau)
        # affichage du plateau
        try:
            coupsPossible = coupsPossibles(copiePlateau(plateau), joueur)
            if len(coupsPossible) > 0:
                nomCoup = int(input("choisissez votre coup :"))
                coupJoué = False  # variable qui vérrifie si le joueur a bien donné un coup valable

                for coup in coupsPossible:
                    if nomCoup == coup[3]:
                        coupJoué = True
                        plateau = jouercoup(coup, copiePlateau(plateau))
                        if joueur == 1:
                            pierresJoueur1 += plateau[2]
                            print("votre score est de : ", pierresJoueur1)
                        else:
                            pierresJoueur0 += plateau[2]
                            print("votre score est de : ", pierresJoueur0)
                        plateau.pop()

                        if joueur == 1:
                            joueur = 0
                        else:
                            joueur = 1

                if not coupJoué:
                    print("vous n'avez pas donné un coup valide, veuillez réessayer")

            else:
                if pierresJoueur0 > pierresJoueur1:
                    print("fin de partie, le joueur 0 à gagné")
                elif pierresJoueur0 < pierresJoueur1:
                    print("fin de partie, le joueur 1 à gagné")
                else:
                    print("fin de partie, il y a égalité")
                break

        except:
            print("vous n'avez pas entré un coup valable")




game()

