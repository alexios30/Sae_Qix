from fltk import *
from time import *
from math import *
from fonction import *

if __name__ == "__main__":


    # TODO Style de la fenêtre 

    # Création de la fenêtre
    lFenetre = 600
    hFenetre = 600

    cree_fenetre(lFenetre, hFenetre)
    rectangle(0, 0, lFenetre, hFenetre, 'black', 'black', tag="background")

    # Initialisation du circuit
    espace_autour_circuit = 15
    circuitX1 = espace_autour_circuit
    circuitX2 = lFenetre - espace_autour_circuit
    circuitY1 = 90
    circuitY2 = hFenetre - espace_autour_circuit

    rectangle(circuitX1, circuitY1, circuitX2, circuitY2, 'white', tag='circuit')


    # TODO Création du joueur

    # Dimension du joueur
    tailleJoueur = 8
    joueurX = lFenetre // 2
    joueurY = circuitY2

    cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

    
    # TODO Déplacements du joueur et fonctions de jeu

    vitesse = 0.04
    orientation = None
    dep = 5
    dx = 0 
    dy = 0
    entree = 0
    old_orientation = None

    # Segments que le joueur dessine, qui deviennent des chemins possibles (segments du circuit initiaux + segments tracés)
    segments_totaux = segments_initiaux(circuitX1, circuitX2, circuitY1, circuitY2)
    segments_traces = 0
    coordonnee_poly = []


    while True:

        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'Quitte':
            break
        if tev == 'Touche':
            nom_touche = touche(ev)

            if nom_touche == 'Return':
                entree = 1

            # Touche 'flèche gauche' pressée
            if nom_touche == 'Left':
                old_orientation = orientation
                orientation = 180

            # Touche 'flèche droite' pressée
            elif nom_touche == 'Right':
                old_orientation = orientation
                orientation = 0

            # Touche 'flèche bas' pressée
            elif nom_touche == 'Down':
                old_orientation = orientation
                orientation = 270

            # Touche 'flèche haut' pressée
            elif nom_touche == 'Up':
                old_orientation = orientation
                orientation = 90

            # Touche 'échap' pressée
            elif nom_touche =="Escape":
                ferme_fenetre()

        # Test sur tous les segments dessinés si le joueur peut les parcourir 
        for i in segments_totaux:
            x1, y1 = i[0]
            x2, y2 = i[1]

            if entree == 1:

                # Déplacement en fonction de l'orientation du joueur
                new_orientation = orientation_dep(orientation, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, joueurX, joueurY, dx, dy)

                # si changement de trajectoire, prendre les coordonnées du joueur pour calculer son polygone
                if orientation != old_orientation:

                    # enregistrer chaque coin du polygone
                    coordonnee_poly.append([joueurX, joueurY])
                    old_orientation = orientation

                dx = new_orientation[0]
                dy = new_orientation[1]

                # Prépare les nouvelles coordonnées afin de vérifier si le joueur peut se déplacer sans sortir du circuit
                nouveauX = joueurX + dx 
                nouveauY = joueurY + dy

                if ((circuitX1 <= nouveauX <= circuitX2) and (circuitY1 <= nouveauY <= circuitY2)):
                    efface('joueur')
                    # tracé les lignes des futures polygones 
                    ligne(joueurX, joueurY, nouveauX, nouveauY, couleur='white', tag='segment_tracé')

                    joueurX += dx
                    joueurY += dy
                    joueur = cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

                sleep(0.05) ### gérer la vitesse qui sacade 

                # si le joueur revient sur le circuit
                if point_dans_segment(x1, y1, x2, y2, nouveauX, nouveauY):

                    # sortir de la boucle de la touche 'entrée' et du dessin 
                    entree = 0
                    # prendre les coordonnées du point final (celui qui revient sur le circuit)
                    coordonnee_poly.append([joueurX, joueurY])

                    # formation de tuple des segments tracés, qui deviennent des chemins possibles
                    segments_traces = segment_par_coordonnee(coordonnee_poly)
                    for i in segments_traces:
                        segments_totaux.append(i)

                    # tracé le polygone 
                    polygone(coordonnee_poly, 'white', 'green', tag='polygone')

                    coordonnee_poly = []
                    break 

                
            
            # Déplacement en fonction de l'orientation du joueur
            new_orientation = orientation_dep(orientation, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, joueurX, joueurY, dx, dy)
            dx = new_orientation[0]
            dy = new_orientation[1]

            # Prépare les nouvelles coordonnées afin de vérifier si le joueur peut se déplacer sans sortir du circuit
            nouveauX = joueurX + dx 
            nouveauY = joueurY + dy 

            if point_dans_segment(x1, y1, x2, y2, joueurX, joueurY) and point_dans_segment(x1, y1, x2, y2, nouveauX, nouveauY):
                efface('joueur')
                joueurX += dx 
                joueurY += dy 
                joueur = cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')
        sleep(vitesse)



        mise_a_jour()

    # TODO Les adversaires et leurs déplacements

    # TODO Les vies du joueur 

    # TODO Niveaux et vitesses qui augmentent 

    attend_fermeture()
