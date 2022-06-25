from termcolor import colored

"""
format d'un plateau :
[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] (le plateau [0] doit être inversé sur l'affichage)

format d'un coup :
[coordonnée X, coordonnée Y, 1 == gain possible/0 == gain impossible, nom du coup]
"""


def affichage(plateau):
    """
     :param plateau:
     affiche le plateau, en inversant la première ligne
    """

    ligne1 = plateau[0][::-1]
    ligne2 = plateau[1]

    print('|', ligne1[0], '|', ligne1[1], '|', ligne1[2], '|', ligne1[3], '|', ligne1[4], '|', ligne1[5], '|')
    print('|', ligne2[0], '|', ligne2[1], '|', ligne2[2], '|', ligne2[3], '|', ligne2[4], '|', ligne2[5], '|')


def copie_plateau(plateau):
    """
    renvoie une copie du plateau avec une adresse mémoire différente
    """
    newplateau = [[t for t in i] for i in plateau]
    return newplateau


def initialisation_plateau():
    """
 renvoie le plateau de début de partie
    """
    return [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]


def jouercoup(coup, plateau):
    """
    :param coup: les 2 premiers paramètres de coup sont les positions x et y du coup,
    le 3ème dit à la fonction si elle peut récupérer les pierres ou pas
    :param plateau: donne le plateau dans son état initial (avant de jouer le coup)
    :return: renvoie le plateau une fois le coup joué, suivi du gain réalisé par le joueur
    """
    pierre = plateau[coup[0]][coup[1]]  # on récupère les pierres du trou
    plateau[coup[0]][coup[1]] = 0  # on dit qu'il n'y a plus de pierres dans le trou

    # on pose les pierres une par une
    ligne = coup[0]
    colonne = coup[1]
    while pierre != 0:
        if colonne + 1 <= 5:     # si le prochain trou est dans notre ligne
            if colonne + 1 != coup[1] or ligne != coup[0]:   # si le prochain trou n'est pas le trou de départ
                colonne += 1     # on avance d'un trou
            else:       # sinon c'est que le prochain trou est le trou de départ qu'il faut sauter
                if colonne + 2 <= 5:     # on vérifie que le trou d'après est dans notre ligne
                    colonne += 2
                # si ce n'est pas le cas, on change de ligne
                elif ligne + 1 <= 1:
                    colonne = 0
                    ligne += 1
                else:
                    colonne = 0
                    ligne = 0
        # si dès le départ le prochain trou n'est pas dans notre ligne
        # et que nous sommes dans la ligne 0, nous passons dans la ligne 1
        elif ligne + 1 <= 1:
            if 0 != coup[1] or ligne + 1 != coup[0]:    # si le prochain trou n'est pas le trou de départ
                colonne = 0
                ligne += 1      # changement de ligne
            else:       # sinon c'est que le prochain trou est le trou de départ qu'il faut sauter
                colonne = 1  # on ne repart pas au début de la colonne mais un trou après
                ligne += 1
        # Sinon c'est que dès le départ il faut passer dans la ligne 0
        else:
            if coup[1] != 0 or coup[0] != 0:    # si le prochain trou n'est pas le trou de départ
                colonne = 0
                ligne = 0   # changement de ligne
            else:       # sinon c'est que le prochain trou est le trou de départ qu'il faut sauter
                colonne = 1
                ligne = 0   # on ne repart pas au début de la colonne mais un trou après

        # on ajoute une graine dans le trou
        plateau[ligne][colonne] += 1
        pierre -= 1

    # si on peut récupérer les pierres, on le fait et on renvoie le plateau, sinon on renvoie le plateau
    gain = 0
    if coup[2] == 1:    # si le gain est possible
        while True:
            # si la case où l'on se situe contient 2 ou 3 graines et que l'on est dans un trou de l'adversaire
            if (plateau[ligne][colonne] == 2 or plateau[ligne][colonne] == 3) and ligne != coup[0]:
                gain += plateau[ligne][colonne]      # on ajoute le gain
                plateau[ligne][colonne] = 0  # on supprime les graines du plateau
                if colonne - 1 >= 0:     # si le trou précédent est un trou de l'adversaire
                    colonne -= 1     # on recule d'un trou
                # sinon c'est que le trou précédent est un des trous du joueur on sort donc de la fonction
                else:
                    plateau.append(gain)
                    return plateau
            # Sinon c'est qu'on ne peut pas réaliser de gain, on sort donc de la fonction
            else:
                plateau.append(gain)
                return plateau
    # Sinon c'est que la prise n'est pas autorisée, on sort de la fonction
    else:
        plateau.append(gain)
        return plateau


def defaut_coups(joueur):
    """
    Liste de tous les coups que le joueur peut jouer par défaut.
    """
    if joueur == 0:
        return [[0, 0, 1, 6], [0, 1, 1, 5], [0, 2, 1, 4], [0, 3, 1, 3], [0, 4, 1, 2], [0, 5, 1, 1]]
    else:
        return [[1, 0, 1, 1], [1, 1, 1, 2], [1, 2, 1, 3], [1, 3, 1, 4], [1, 4, 1, 5], [1, 5, 1, 6]]


def plateau_adverse_non_vide(coup, plateau):
    """
    simule de jouer le coup et vérifie que le plateau adverse n'est pas vide
    """
    after_play = jouercoup(coup, copie_plateau(plateau))  # on simule de jouer le coup
    after_play.pop()

    # on regarde qui est le joueur
    if coup[0] == 1:
        joueur_adverse = 0
    else:
        joueur_adverse = 1

    # on vérifie qu'il y ait au moins 1 trou de l'adversaire qui ne soit pas vide
    for i in after_play[joueur_adverse]:
        if i != 0:
            return True
    return False


def fonc_coups_possibles(plateau, joueur):
    """
    :param plateau: état du plateau avant de jouer le coup
    :param joueur: joueur à qui c'est le tour de jouer
    :return: liste de tous les coups que le joueur peut jouer
    """
    coups_possibles = []
    defaut = defaut_coups(joueur)
    # on récupère tous les coups réalisables
    for coup in defaut:
        if plateau[coup[0]][coup[1]] != 0 and plateau_adverse_non_vide(coup, copie_plateau(plateau)):
            coups_possibles.append(coup)
        else:
            coup[2] = 0
            if plateau[coup[0]][coup[1]] != 0 and plateau_adverse_non_vide(coup, copie_plateau(plateau)):
                coups_possibles.append(coup)

    return coups_possibles


def ia_min(plateau, gain_joueur1, gain_joueur0, profondeur):
    # si on a atteint la profondeur maximale ou que la partie est finie on renvoie la difference de gain
    if profondeur == 0:
        return float(gain_joueur1 - gain_joueur0)

    coups_possibles = fonc_coups_possibles(copie_plateau(plateau), 1)

    if len(coups_possibles) == 0:
        if gain_joueur1 > gain_joueur0:
            return 1000
        elif gain_joueur1 < gain_joueur0:
            return -1000
        else:
            return 0

    # sinon on simule de jouer tous les coups et on renvoie la valeur minimale de la difference de gain
    mini = None
    for coup in coups_possibles:
        plateautmp = jouercoup(coup, copie_plateau(plateau))
        coups_possibles = plateautmp[2] + gain_joueur0
        plateautmp.pop()
        tmp = ia_max(plateautmp, gain_joueur1, coups_possibles, profondeur - 1)
        if mini is None:
            mini = tmp
        elif tmp < mini:
            mini = tmp

    return mini


def ia_max(plateau, gain_joueur1, gain_joueur0, profondeur):
    # si on a atteint la profondeur maximale ou que la partie est finie on renvoie la difference de gain
    if profondeur == 0:
        return float(gain_joueur1 - gain_joueur0)

    coups_possibles = fonc_coups_possibles(copie_plateau(plateau), 1)

    if len(coups_possibles) == 0:
        if gain_joueur1 > gain_joueur0:
            return 1000
        elif gain_joueur1 < gain_joueur0:
            return -1000
        else:
            return 0

    # sinon on simule de jouer tous les coups et on renvoie la valeur maximale de la difference de gain
    maxi = None
    for coup in coups_possibles:
        plateautmp = jouercoup(coup, copie_plateau(plateau))
        gain_joueur1_tmp = plateautmp[2] + gain_joueur1
        plateautmp.pop()
        tmp = ia_min(plateautmp, gain_joueur1_tmp, gain_joueur0, profondeur - 1)
        if maxi is None:
            maxi = tmp
        elif tmp > maxi:
            maxi = tmp

    return maxi


def ia(plateau, profondeur):
    maxi = None
    coup_jouer = None
    # Pour chaque coup possible on simule de jouer sur une profond1eur donnée et on récupère le meilleur coup
    coups_possibles = fonc_coups_possibles(copie_plateau(plateau), 1)
    for coup in coups_possibles:
        plateautmp = jouercoup(coup, copie_plateau(plateau))
        gain_joueur1 = plateautmp[2]
        plateautmp.pop()
        tmp = ia_min(plateautmp, gain_joueur1, 0, profondeur - 1)
        # on met à jour la difference de gain maximale et le meilleur coup
        if maxi is None:
            maxi = tmp
            coup_jouer = coup[3]
        elif tmp > maxi:
            maxi = tmp
            coup_jouer = coup[3]
    print("L'ia joue : ", colored(str(coup_jouer), 'red'))
    return coup_jouer


def affichage_score(pierres_joueur1, pierres_joueur0):
    if pierres_joueur0 > pierres_joueur1:
        print("fin de partie, le joueur 0 à gagné")
    elif pierres_joueur0 < pierres_joueur1:
        print("fin de partie, l'ia' à gagné")
    else:
        print("fin de partie, il y a égalité")


def game():
    """
    fonction principale qui fait jouer les joueurs
    """
    joueur = 0  # par défaut le joueur 0 commence
    pierres_joueur0 = 0  # pierres gagnées par le joueur 0
    pierres_joueur1 = 0  # pierres gagnées par le joueur 0
    derniers_coups = list()
    plateau = initialisation_plateau()

    # boucle qui dure tout le long de la partie
    while True:
        affichage(plateau)
        # affichage du plateau

        try:    # on vérifie que le joueur donne bien un entier comme coup
            coups_possible = fonc_coups_possibles(copie_plateau(plateau),
                                                  joueur)  # on récupère la liste de tous les coups possibles

            if len(coups_possible) > 0:  # on vérifie que ce n'est pas la fin de la partie
                if joueur == 0:
                    nom_coup = int(input("choisissez votre coup :"))  # le joueur choisit son coup
                else:
                    nom_coup = ia(copie_plateau(plateau), 9)
                coup_joue = False  # variable qui vérifie si le joueur a bien donné un coup valable

                # on cherche quel est le coup que le joueur a choisi et on le joue
                for coup in coups_possible:
                    if nom_coup == coup[3]:
                        coup_joue = True
                        plateau = jouercoup(coup, copie_plateau(plateau))

                        # on regarde si le plateau a déjà été dans cette position. Si oui on termine la partie
                        if plateau[:2] in derniers_coups:
                            print("Le plateau a déjà été dans cette position.")
                            affichage_score(pierres_joueur0, pierres_joueur1)
                            return
                        derniers_coups.append(plateau)

                        # affichage des scores
                        if joueur == 1:
                            pierres_joueur1 += plateau[2]
                            print(colored("Score de l'ia : ", 'red'), colored(str(pierres_joueur1), 'red'))

                        else:
                            pierres_joueur0 += plateau[2]
                            print(colored("votre score est de :", 'green'), colored(str(pierres_joueur0), 'green'))
                        plateau.pop()

                        # on change de joueur
                        if joueur == 1:
                            joueur = 0
                        else:
                            joueur = 1

                # si la valeur donnée ne correspond à aucun coup on demande au joueur de réessayer
                if not coup_joue:
                    print("vous n'avez pas donné un coup valide, veuillez réessayer")

            # quand la partie est finie on indique le gagnant
            else:
                affichage_score(pierres_joueur1, pierres_joueur0)
                break

        except:  # si le joueur n'a pas donné un entier
            print("vous n'avez pas entré un coup valable")


game()
