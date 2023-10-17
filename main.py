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

    vitesse = 0.03
    orientation = None
    dep = 5
    dx = 0 
    dy = 0
    entree = 0

    # Segments que le joueur dessine, qui deviennent des chemins possibles (segments du circuit initiaux + segments tracés)
    segments_totaux = segments_initiaux(circuitX1, circuitX2, circuitY1, circuitY2)
    segments_trace = []


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
                orientation = 180

            # Touche 'flèche droite' pressée
            elif nom_touche == 'Right':
                orientation = 0

            # Touche 'flèche bas' pressée
            elif nom_touche == 'Down':
                orientation = 270

            # Touche 'flèche haut' pressée
            elif nom_touche == 'Up':
                orientation = 90

            # Touche 'échap' pressée
            elif nom_touche =="Escape":
                ferme_fenetre()

        # Test sur tous les segments dessinés si le joueur peut les parcourir 
        for i in segments_totaux:
            x1, y1 = i[0]
            x2, y2 = i[1]

            if entree == 1:

                # Trouvez les segments proches de la position actuelle du joueur
                segments_proches = []
                for element in segments_totaux:
                    x1_segment, y1_segment = element[0]
                    x2_segment, y2_segment = element[1]

                    if point_dans_segment(x1_segment, y1_segment, x2_segment, y2_segment, joueurX, joueurY):
                        segments_proches.append(i)

                if segments_proches:
                    # Sélectionnez un segment proche 
                    segmentProche = segments_proches[0]
                    x1, y1 = segmentProche[0]
                    x2, y2 = segmentProche[1]

                    # Déterminez les directions libres à partir de la position actuelle du joueur
                    dirs_libres = directions_libres(joueurX, joueurY, segments_totaux)
                    print(dirs_libres, 'direction libre')

                    # Choisir l'une des directions libres 
                    nouvelle_orientation = dirs_libres[0] ### réfléchir sur la façon du choix de l'orientation 

                    # Mettez à jour l'orientation du joueur
                    orientation = nouvelle_orientation
                
                # Déplacement en fonction de l'orientation du joueur
                new_orientation = orientation_dep(orientation, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, joueurX, joueurY, dx, dy)
                dx = new_orientation[0]
                dy = new_orientation[1]

                # Prépare les nouvelles coordonnées afin de vérifier si le joueur peut se déplacer sans sortir du circuit
                nouveauX = joueurX + dx
                nouveauY = joueurY + dy
                print(dx, dy)

                if ((circuitX1 <= nouveauX <= circuitX2) and (circuitY1 <= nouveauY <= circuitY2)):
                    efface('joueur')
                    joueurX += dx
                    joueurY += dy
                    joueur = cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')
                    sleep(vitesse) ### gérer la vitesse qui sacade 

                if point_dans_segment(x1, y1, x2, y2, nouveauX, nouveauY):
                    entree = 0
                    break ### gérer les fin de boucles pour revenir sur le circuit depuis tous les côtés
            
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
