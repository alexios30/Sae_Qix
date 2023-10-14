from fltk import *

def dessin_carre(x, y, cote):
    rectangle(x, y, x + cote, y + cote,
               "red", "red", tag='carre')

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
    
    

    # TODO Déplacements du joueur

    # TODO Les adversaires et leurs déplacements

    # TODO Les vies du joueur 

    # TODO Niveaux et vitesses qui augmentent 

    attend_fermeture()
    
