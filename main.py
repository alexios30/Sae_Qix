from fltk import *
from time import *
from math import *
from fonction import *
from random import *

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

    # Dimensions du joueur
    tailleJoueur = 8
    joueurX = lFenetre // 2
    joueurY = circuitY2

    cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

    # Création des adversaires

    # Dimensions des adversaires
    tailleSparx = 8

    # sparx 1
    sparx_X1 = lFenetre // 2
    sparx_Y1 = circuitY1
    orientation_S1 = 0
    dep_S1_x = 0
    dep_S1_y = 0
    cercle(sparx_X1, sparx_Y1, tailleSparx, 'red', '', 2, tag='sparx1')

    
    # sparx 2
    sparx_X2 = lFenetre // 2
    sparx_Y2 = circuitY1
    orientation_S2 = 180
    dep_S2_x = 0
    dep_S2_y = 0
    cercle(sparx_X2, sparx_Y2, tailleSparx, 'red', '', 2, tag='sparx2')

    
    # TODO Déplacements du joueur et fonctions de jeu

    vitesse = 0.04
    orientation_j = None
    dep = 5
    dxj = 0 
    dyj = 0
    entree = 0
    old_orientation_j = None
    depart = 0

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
                old_orientation_j = orientation_j
                orientation_j = 180

            # Touche 'flèche droite' pressée
            elif nom_touche == 'Right':
                old_orientation_j = orientation_j
                orientation_j = 0

            # Touche 'flèche bas' pressée
            elif nom_touche == 'Down':
                old_orientation_j = orientation_j
                orientation_j = 270

            # Touche 'flèche haut' pressée
            elif nom_touche == 'Up':
                old_orientation_j = orientation_j
                orientation_j = 90

            # Touche 'échap' pressée
            elif nom_touche =="Escape":
                ferme_fenetre()

        # Test sur tous les segments dessinés si le joueur peut les parcourir 
        for i in segments_totaux:
            x1, y1 = i[0]
            x2, y2 = i[1]

            if entree == 1: 

                # if depart == 0:
                #     x_depart, y_depart = i
                #     depart += 1

                # Déplacement en fonction de l'orientation du joueur
                new_orientation_j = orientation_dep_joueur(orientation_j, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, joueurX, joueurY, dxj, dyj)

                # si changement de trajectoire, prendre les coordonnées du joueur pour calculer son polygone
                if orientation_j != old_orientation_j:

                    # enregistrer chaque coin du polygone
                    coordonnee_poly.append([joueurX, joueurY])
                    old_orientation_j = orientation_j
                    
                    # # formation de tuple des segments tracés, qui deviennt des chemins possibles
                    # segments_traces = segment_par_coordonnee(coordonnee_poly)
                    # for i in segments_traces:
                    #     segments_totaux.append(i)
                    # segment_totaux = segment_sans_doublons(segments_totaux)

                dxj = new_orientation_j[0]
                dyj = new_orientation_j[1]

                # Prépare les nouvelles coordonnées afin de vérifier si le joueur peut se déplacer sans sortir du circuit
                nouveauX_j = joueurX + dxj
                nouveauY_j = joueurY + dyj

                if ((circuitX1 <= nouveauX_j <= circuitX2) and (circuitY1 <= nouveauY_j <= circuitY2)):
                    efface('joueur')
                    # tracé les lignes des futures polygones 
                    ligne(joueurX, joueurY, nouveauX_j, nouveauY_j, couleur='white', tag='segment_tracé')

                    joueurX += dxj
                    joueurY += dyj
                    joueur = cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

                sleep(0.03) ### gérer la vitesse qui sacade 

                # si le joueur revient sur le circuit
                if point_dans_segment(x1, y1, x2, y2, nouveauX_j, nouveauY_j):

                    # sortir de la boucle de la touche 'entrée' et du dessin 
                    entree = 0
                    # prendre les coordonnées du point final (celui qui revient sur le circuit)
                    coordonnee_poly.append([joueurX, joueurY])

                    # formation de tuple des segments tracés, qui deviennt des chemins possibles
                    segments_traces = segment_par_coordonnee(coordonnee_poly)
                    for i in segments_traces:
                        segments_totaux.append(i)
                    print(segments_totaux)

                    # tracé le polygone en vérifiant si des coins du circuit sont à rajouter                    
                    polygone(coordonnee_poly, 'white', 'green', tag='polygone')


                    coordonnee_poly = []
                    sortie = 0
                    break 
                
            
            # Déplacement en fonction de l'orientation du joueur
            new_orientation_j = orientation_dep_joueur(orientation_j, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, joueurX, joueurY, dxj, dyj)
            dxj = new_orientation_j[0]
            dyj = new_orientation_j[1]

            # Prépare les nouvelles coordonnées 
            nouveauX_j = joueurX + dxj 
            nouveauY_j = joueurY + dyj 


            # Vérifier si le joueur peut se déplacer sans sortir du circuit
            if point_dans_segment(x1, y1, x2, y2, joueurX, joueurY) and point_dans_segment(x1, y1, x2, y2, nouveauX_j, nouveauY_j):
                efface('joueur')
                joueurX += dxj 
                joueurY += dyj 
                joueur = cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')


            # Déplacement du sparx 1 en fonction de l'orientation
            new_orientation_s = orientation_dep_sparx(orientation_S1, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, sparx_X1, sparx_Y1)
            dep_S1_x = new_orientation_s[0]
            dep_S1_y = new_orientation_s[1]

            # Prépare les nouvelles coordonnées du sparx 1
            nouveauX_S1 = sparx_X1 + dep_S1_x
            nouveauY_S1 = sparx_Y1 + dep_S1_y


            # Vérifier si les sparx peuvent se déplacer en restant sur le circuit
            # premier sparx
            if point_dans_segment(x1, y1, x2, y2, sparx_X1, sparx_Y1) and point_dans_segment(x1, y1, x2, y2, nouveauX_S1, nouveauY_S1):
                efface('sparx1')
                sparx_X1 += dep_S1_x
                sparx_Y1 += dep_S1_y
                sparx1 = cercle(sparx_X1, sparx_Y1, tailleSparx, 'red', '', 2, tag='sparx1')

            # deuxième sparx
            if point_dans_segment(x1, y1, x2, y2, sparx_X2, sparx_Y2) :
                efface('sparx2')
                sparx_X2 -= 5
                # sparx_Y += randrange(10, 15)
                sparx2 = cercle(sparx_X2, sparx_Y2, tailleSparx, 'red', '', 2, tag='sparx2')

        sleep(vitesse)



        mise_a_jour()

    # TODO Les adversaires et leurs déplacements

    # TODO Les vies du joueur 

    # TODO Niveaux et vitesses qui augmentent 

    attend_fermeture()
