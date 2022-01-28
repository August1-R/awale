'''
Le joueur False est le joueur qui a plateau[0] devant lui
Le joueur True est le joueur qui a plateau[1] devant lui
'''


initialisationPlateau = [[4,4,4,4,4,4],
                         [4,4,4,4,4,4]]

def coupsPossibles(plateau, joueur):
    coupsPossibles = []
    if not joueur:
        for i in range(6):
            coupsPossibles.append([0][i])
        return coupsPossibles

coupsPossibles()