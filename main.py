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
    vie_joueur = 3

    # Création des adversaires

    # Dimensions des adversaires
    tailleSparx = 8

    # sparx 1
    sparx_X1 = lFenetre // 2
    sparx_Y1 = circuitY1
    orientation_S1 = 0
    dep_S1_x = 1
    dep_S1_y = 1
    cercle(sparx_X1, sparx_Y1, tailleSparx, 'red', '', 2, tag='sparx1')
    
    # sparx 2
    sparx_X2 = lFenetre // 2
    sparx_Y2 = circuitY1
    orientation_S2 = 180
    dep_S2_x = 1
    dep_S2_y = 1
    cercle(sparx_X2, sparx_Y2, tailleSparx, 'red', '', 2, tag='sparx2')

    # Qix
    x_qix=300
    y_qix=300
    #Vitesse Qix
    vitesse_qix=10
    #Milieu du Qix
    milieu_qix=30
    qix(x_qix, y_qix)

    #Ecriture de vie restante
    chaineQix="Vie Restante: "
    tailleQix = 15
    policeQix ="Courier"
    texte(490,30,chaineQix,police=policeQix,taille=tailleQix,couleur="red",ancrage="center")

    #Ecriture de qix
    chaineQix="Qix"
    tailleQix = 50
    policeQix ="Stencil"
    texte(300,50,chaineQix,police=policeQix,taille=tailleQix,couleur="blue",ancrage="center")

    #Ecriture de 3
    chaineQix="3"
    tailleQix = 15
    policeQix ="Courier"
    texte(570,30,chaineQix,police=policeQix,taille=tailleQix,couleur="red",ancrage="center",tag='vie')

    # Obstacles
    nb_obstacle = 0
    
    # TODO Déplacements du joueur et fonctions de jeu

    vitesse = 0.04
    orientation_j = None
    dep = 5
    dxj = 0 
    dyj = 0
    entree = 0
    old_orientation_j = None

    # Segments que le joueur dessine, qui deviennent des chemins possibles (segments du circuit initiaux + segments tracés)
    segments_totaux = segments_initiaux(circuitX1, circuitX2, circuitY1, circuitY2)
    segments_traces = 0
    coordonnee_poly = []
    liste_lignes = []


    while vie_joueur > 0:

        ev = donne_ev()
        tev = type_ev(ev)

        if tev == 'Quitte':
            break
        if tev == 'Touche':
            nom_touche = touche(ev)

            # Touche 'entrée' pressée
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

                # Déplacement en fonction de l'orientation du joueur
                new_orientation_j = orientation_dep(orientation_j, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, joueurX, joueurY)

                # si changement de trajectoire, prendre les coordonnées du joueur pour calculer son polygone
                if orientation_j != old_orientation_j:

                    # enregistrer chaque coin du polygone
                    coordonnee_poly.append([joueurX, joueurY])
                    old_orientation_j = orientation_j
                    try:
                        liste_lignes.pop(-1)
                    except:
                        pass    

                dxj = new_orientation_j[0]
                dyj = new_orientation_j[1]

                # Prépare les nouvelles coordonnées afin de vérifier si le joueur peut se déplacer sans sortir du circuit
                nouveauX_j = joueurX + dxj
                nouveauY_j = joueurY + dyj

                if ((circuitX1 <= nouveauX_j <= circuitX2) and (circuitY1 <= nouveauY_j <= circuitY2)):

                    efface('joueur')

                    # Collision qix / joueur
                    if collision_qix(x_qix, y_qix, joueurX, joueurY, tailleJoueur):
                        efface('segment_tracé')
                        orientation_j = None
                        joueurX = lFenetre // 2
                        joueurY = circuitY2
                        #Remets les sparx a leur point de départ
                        sparx_X1 = lFenetre // 2
                        sparx_Y1 = circuitY1
                        orientation_S1 = 0
                        dep_S1_x = 1 
                        dep_S1_y = 1
                        sparx_X2 = lFenetre // 2
                        sparx_Y2 = circuitY1    
                        orientation_S2 = 180  
                        dep_S2_x = 1  
                        dep_S2_y = 1
                        #Remets le qix a son point de départ
                        x_qix = 300
                        y_qix = 300
                        efface('vie')
                        vie_joueur-=1
                        # sortir de la boucle entrée car le joueur revient sur le circuit
                        entree = 0
                        if nombre_vie(vie_joueur):
                            break

                    # Collision entre le qix et les lignes que dessine le joueur
                    if intersection_qix(liste_lignes,x_qix,y_qix,60):
                        #Remets le joueur a son point de départ
                        orientation_j = None
                        joueurX = lFenetre // 2
                        joueurY = circuitY2
                        dxj = 0
                        dyj = 0
                        #Remets les sparx a leur point de départ
                        sparx_X1 = lFenetre // 2
                        sparx_Y1 = circuitY1
                        orientation_S1 = 0  
                        dep_S1_x = 1 
                        dep_S1_y = 1
                        sparx_X2 = lFenetre // 2
                        sparx_Y2 = circuitY1    
                        orientation_S2 = 180  
                        dep_S2_x = 1  
                        dep_S2_y = 1
                        #Remets le qix a son point de départ
                        x_qix = 300
                        y_qix = 300
                        # sortir de la boucle entrée car le joueur revient sur le circuit
                        entree = 0
                        efface('segment_tracé')
                        #Enlève une vie 
                        efface('vie')
                        vie_joueur-=1
                        if nombre_vie(vie_joueur):
                            break

                    # Le joueur dessine mais repasse sur sa ligne non-finie
                    if intersection_lignes_presentes(liste_lignes):
                        liste_lignes = []
                        # Remettre le joueur au point de départ
                        efface('joueur')
                        joueurX = lFenetre // 2
                        joueurY = circuitY2
                        orientation_j = None
                        cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')
                        # Efface le tracé actuel (qui se coupe donc)
                        efface('segment_tracé')
                        #Enlève une vie 
                        efface('vie')
                        vie_joueur-=1
                        # sortir de la boucle entrée car le joueur revient sur le circuit
                        entree = 0
                        if nombre_vie(vie_joueur):
                            break
                        break

                    if nombre_vie(vie_joueur):
                        break

                    # tracé les lignes des futures polygones 
                    ligne(joueurX, joueurY, nouveauX_j, nouveauY_j, couleur='white', tag='segment_tracé')
                    liste_lignes.append(tuple(((joueurX, joueurY),(nouveauX_j, nouveauY_j))))

                    joueurX += dxj
                    joueurY += dyj
                    joueur = cercle(joueurX, joueurY, tailleJoueur, 'yellow', '', 2, tag='joueur')

                sleep(0.03) ### gérer la vitesse qui sacade 

                # si le joueur revient sur le circuit
                if point_dans_segment(x1, y1, x2, y2, nouveauX_j, nouveauY_j):

                    # sortir de la boucle de la touche 'entrée' et du dessin 
                    entree = 0
                    # prendre les coordonnées du point final (celui qui se trouve sur le circuit)
                    coordonnee_poly.append([joueurX, joueurY])

                    # formation de tuples des segments tracés, qui deviennt des chemins possibles
                    segments_traces = segment_par_coordonnee(coordonnee_poly)
                    for i in segments_traces:
                        segments_totaux.append(i)

                    # tracé le polygone en vérifiant si des coins du circuit sont à rajouter                    
                    polygone(coordonnee_poly, 'white', 'green', tag='polygone')

                    coordonnee_poly = []
                    break 
            
            # Déplacement en fonction de l'orientation du joueur
            new_orientation_j = orientation_dep(orientation_j, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, joueurX, joueurY)
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
            
            
            # Si le sparx rencontre une intersection, il choisit au hasard parmit celles disponibles
            # liste des orientations disponibles 
            possibles_S1 = orientation_dispo(orientation_S1)
            if dep_S1_x == 0 and dep_S1_y == 0:
                orientation_S1 = choice(possibles_S1)
            else:
                pass

            # Déplacement du sparx 1 en fonction de l'orientation
            new_orientation_s1 = orientation_dep(orientation_S1, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, sparx_X1, sparx_Y1)
            dep_S1_x = new_orientation_s1[0]
            dep_S1_y = new_orientation_s1[1]

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

            # Si le sparx rencontre une intersection, il choisit au hasard parmit celles disponibles
            # liste des orientations disponibles 
            possibles_S2 = orientation_dispo(orientation_S2)
            if dep_S2_x == 0 and dep_S2_y == 0: ### Trouver la bonne condition pour faire rentrer les sparx sur les segments totaux
                orientation_S2 = choice(possibles_S2)
            else:
                pass

            # Déplacement du sparx 2 en fonction de l'orientation
            new_orientation_s2 = orientation_dep(orientation_S2, dep, espace_autour_circuit, lFenetre, hFenetre, circuitY1, sparx_X2, sparx_Y2)
            dep_S2_x = new_orientation_s2[0]
            dep_S2_y = new_orientation_s2[1]

            # Prépare les nouvelles coordonnées du sparx 2
            nouveauX_S2 = sparx_X2 + dep_S2_x
            nouveauY_S2 = sparx_Y2 + dep_S2_y

            # deuxième sparx
            if point_dans_segment(x1, y1, x2, y2, sparx_X2, sparx_Y2) and point_dans_segment(x1, y1, x2, y2, nouveauX_S2, nouveauY_S2):
                efface('sparx2')
                sparx_X2 += dep_S2_x
                sparx_Y2 += dep_S2_y
                sparx2 = cercle(sparx_X2, sparx_Y2, tailleSparx, 'red', '', 2, tag='sparx2')

        # Collision Sparx / joueur
        if (distance(sparx_X1, sparx_Y1, joueurX, joueurY) <= tailleJoueur) or (distance(sparx_X2, sparx_Y2, joueurX, joueurY) <= tailleJoueur):
            #Remets le joueur a son point de départ
            orientation_j = None
            joueurX = lFenetre // 2
            joueurY = circuitY2
            #Remets les sparx a leur point de départ
            sparx_X1 = lFenetre // 2
            sparx_Y1 = circuitY1
            orientation_S1 = 0  
            dep_S1_x = 1 
            dep_S1_y = 1
            sparx_X2 = lFenetre // 2
            sparx_Y2 = circuitY1    
            orientation_S2 = 180  
            dep_S2_x = 1  
            dep_S2_y = 1
            #Remets le qix a son point de départ
            x_qix = 300
            y_qix = 300
            #Enlève une vie 
            efface('vie')
            vie_joueur-=1
            if nombre_vie(vie_joueur):
                break

        if vie_joueur == 2 and nb_obstacle == 0:
            coords_obstacle = point_au_milieu_aleatoire(segments_totaux)
            obstacle_X1, obstacle_Y1 = coords_obstacle
            cercle(obstacle_X1, obstacle_Y1, 5, 'red', 'red', tag='obstacle1')
            nb_obstacle = 1

        if vie_joueur == 1 and nb_obstacle == 1:
            coords_obstacle = point_au_milieu_aleatoire(segments_totaux)
            obstacle_X2, obstacle_Y2 = coords_obstacle
            cercle(obstacle_X2, obstacle_Y2, 5, 'red', 'red', tag='obstacle2')
            nb_obstacle = 2

        sleep(vitesse)
        x_qix,y_qix=deplacement_qix(x_qix,y_qix,vitesse_qix,circuitX1,circuitX2,circuitY1,circuitY2,milieu_qix)
        efface('kong')
        qix(x_qix,y_qix)
        sleep(0.01)

        mise_a_jour()

    # TODO Niveaux et vitesses qui augmentent 

    efface('joueur')
    efface('sparx1')
    efface('sparx2')
    efface('kong')

    attend_fermeture()
