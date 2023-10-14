from fltk import *
from time import *


# def joueur_sur_circuit(
#         x_c1: float,
#         x_c2: float,
#         y_c1: float,
#         y_c2: float,
#         milieuX: float,
#         milieuY: float,
# ) -> int:
#     """
#     Vérifie si le centre du joueur (milieuJ) est sur le circuit.

#     """
#     if x_c1 <= milieuX <= x_c2 and (milieuY == y_c1 or milieuY == y_c1):
#         return True
#     elif (milieuX == x_c1 or milieuX == x_c2) and y_c1 <= milieuY <= y_c2:
#         return True
#     else:
#         return False


if __name__ == "__main__":


    # TODO Style de la fenêtre 

    # Création de la fenêtre
    lFenetre = 600
    hFenetre = 600

    cree_fenetre(lFenetre, hFenetre)
    rectangle(0, 0, lFenetre, hFenetre, 'black', 'black', tag="background")

    # Initialisation du circuit
    espace__autour_circuit = 15
    circuitX1 = espace__autour_circuit
    circuitX2 = lFenetre - espace__autour_circuit
    circuitY1 = 90
    circuitY2 = hFenetre - espace__autour_circuit

    rectangle(circuitX1, circuitY1, circuitX2, circuitY2, 'white', tag='circuit')


    # TODO Création du joueur

    # Dimension du joueur
    tailleJoueur = 8
    joueurX = lFenetre // 2
    joueurY = circuitY2

    cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

    vitesse = 0.05

    
    # TODO Déplacements du joueur

    dep = 5

    while True:

        ev = donne_ev()
        tev = type_ev(ev)

        dx = 0 
        dy = 0

        if tev == 'Quitte':
            break
        if tev == 'Touche':
            nom_touche = touche(ev)

            # Touche 'flèche gauche' pressée
            if nom_touche == 'Left':
                while joueurX >= circuitX1:
                    
                    # Condition si touche pressée -> break le while flèche gauche
                    if touche_pressee('Right') or touche_pressee('Up') or touche_pressee('Down') or touche_pressee('Escape'):
                        break

                    dx = 0
                    dy = 0

                    if joueurX <= circuitX1:
                        pass
                    else:
                        dx = max(-dep, -(joueurX - espace__autour_circuit))

                    # Effectuer le décalage si le déplacement est différent de zéro
                    if dx != 0 or dy != 0:
                        efface('joueur')
                        joueurX += dx
                        joueurY += dy
                        cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

                    sleep(vitesse)
                    mise_a_jour()

            # Touche 'flèche droite' pressée
            elif nom_touche == 'Right':
                while joueurX <= circuitX2:

                    # Condition si touche pressée -> break 
                    if touche_pressee('Left') or touche_pressee('Up') or touche_pressee('Down') or touche_pressee('Escape'):
                        break

                    dx = 0
                    dy = 0

                    if joueurX >= circuitX2:
                        pass
                    else:
                        dx = min(dep, lFenetre - joueurX - espace__autour_circuit)

                    # Effectuer le décalage si le déplacement est différent de zéro
                    if dx != 0 or dy != 0:
                        efface('joueur')
                        joueurX += dx
                        joueurY += dy
                        cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

                    sleep(vitesse)
                    mise_a_jour()

            # Touche 'flèche bas' pressée
            elif nom_touche == 'Down':
                while joueurY <= circuitY2:

                    # Condition si touche pressée -> break 
                    if touche_pressee('Left') or touche_pressee('Up') or touche_pressee('Right') or touche_pressee('Escape'):
                        break

                    dx = 0
                    dy = 0

                    if joueurY >= circuitY2:
                        pass
                    else:
                        dy = min(dep, hFenetre - joueurY - espace__autour_circuit)

                    # Effectuer le décalage si le déplacement est différent de zéro
                    if dx != 0 or dy != 0:
                        efface('joueur')
                        joueurX += dx
                        joueurY += dy
                        cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

                    sleep(vitesse)
                    mise_a_jour()

            # Touche 'flèche haut' pressée
            elif nom_touche == 'Up':
                while joueurY >= circuitY1:

                    # Condition si touche pressée -> break 
                    if touche_pressee('Left') or touche_pressee('Down') or touche_pressee('Right') or touche_pressee('Escape'):
                        break

                    dx = 0
                    dy = 0

                    if joueurY <= circuitY1:
                        pass
                    else:
                        dy = max(-dep, -(joueurY - circuitY1))
                    
                    # Effectuer le décalage si le déplacement est différent de zéro
                    if dx != 0 or dy != 0:
                        efface('joueur')
                        joueurX += dx
                        joueurY += dy
                        cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

                    sleep(vitesse)
                    mise_a_jour()
        
            elif nom_touche =="Escape":
                ferme_fenetre()
            
        mise_a_jour()

    # TODO Les adversaires et leurs déplacements

    # TODO Les vies du joueur 

    # TODO Niveaux et vitesses qui augmentent 

    attend_fermeture()
    