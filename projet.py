from fltk import *
from random import*
from time import*
# Fonction
def dessin_carre(x, y, cote):
    rectangle(x, y, x + cote, y + cote,
               "red", "red", tag='carre')
def qix(x_qix,y_qix,x1_qix,y1_qix):
    ligne(x_qix,y_qix,x1_qix,y1_qix,'white',epaisseur=2,tag='qix')


if __name__ == "__main__":


    # TODO Style de la fenêtre 

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

    #Ecriture de qix
    chaineQix="Qix"
    tailleQix = 20
    policeQix ="Courier"
    texte(40,30,chaineQix,police=policeQix,taille=tailleQix,couleur="blue",ancrage="center")
    
    #Ecriture de Surface
    chaineSurface="Surface"
    tailleSurface=20
    policeTaile='Courier'
    texte(300,20,chaineSurface,police=policeTaile,taille=tailleSurface,couleur='red',ancrage="center")

    # Sparks1
    sparksX = 300
    sparksY = circuitY1
    sparks = cercle(sparksX, sparksY, 4, 'red', '', 2, tag='sparks')

    # Sparks2
    sparksX2 = 300
    sparksY2 = circuitY1
    sparks2 = cercle(sparksX2, sparksY2, 4, 'red', '', 2, tag='sparks2')

    # Vitesse des sparks
    vitesse = 10

    # TODO Les adversaires et leurs déplacements
    mov=0

        #Coordonnée du Qix au départ
    x_qix=250
    y_qix=250
    x1_qix=300
    y1_qix=250 
                
    ev = donne_ev()
    tev = type_ev(ev)

    #Vitesse Qix
    vitesse_qix=15

    #Supprimer qix
    supp=0
    while True:
        #Pour quitter la fênetre
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == 'Touche':
            nom_touche = touche(ev)
            if nom_touche =="Escape":
                ferme_fenetre()

        if supp!=5:
            supp+=1
            qix(x_qix,y_qix,x1_qix,y1_qix)
            #Pour commencer:Il commence donc au milieu
            if x_qix==250 and y_qix==250 and x1_qix==300 and y1_qix==250:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix+vitesse_qix)))
                sleep(0.25)
                mise_a_jour()

            if y_qix<=circuitY1 or y1_qix<=circuitY1: 
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix),(y1_qix+vitesse_qix)))
                sleep(0.25)
                mise_a_jour()
    

            if y_qix>=circuitY2 or y1_qix>=circuitY2:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix)))
                sleep(0.25)
                mise_a_jour()
        
            if x_qix<=circuitX1 or x1_qix<=circuitX1:
                x_qix=(randint((x_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix))) 
                sleep(0.25)               
                mise_a_jour()

            if x_qix>=circuitX2 or x1_qix>=circuitX2:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix+vitesse_qix)))
                sleep(0.25)
                mise_a_jour()
        

            else:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix+vitesse_qix)))           
                sleep(0.25)
                mise_a_jour()

        else:
            efface('qix')
            supp-=1

        #Initialisation postions des Sparks
        nouvelle_x = sparksX
        nouvelle_y = sparksY
        nouvelle_x2 = sparksX2
        nouvelle_y2 = sparksY2

        # Déplacement Sparks1
        if sparksX == circuitX1 and sparksY < circuitY2:
            nouvelle_y = sparksY + vitesse
            if nouvelle_y >= circuitY2:
                nouvelle_y = circuitY2
        elif sparksY == circuitY2 and sparksX < circuitX2:
            nouvelle_x = sparksX + vitesse
            if nouvelle_x >= circuitX2:
                nouvelle_x = circuitX2
        elif sparksX == circuitX2 and sparksY > circuitY1:
            nouvelle_y = sparksY - vitesse
            if nouvelle_y <= circuitY1:
                nouvelle_y = circuitY1
        elif sparksY == circuitY1 and sparksX > circuitX1:
            nouvelle_x = sparksX - vitesse
            if nouvelle_x <= circuitX1:
                nouvelle_x = circuitX1

        # Déplacement Sparks2
        if sparksX2 == circuitX2 and sparksY2 < circuitY2:
            nouvelle_y2 = sparksY2 + vitesse
            if nouvelle_y2 >= circuitY2:
                nouvelle_y2 = circuitY2
        elif sparksY2 == circuitY2 and sparksX2 > circuitX1:
            nouvelle_x2 = sparksX2 - vitesse
            if nouvelle_x2 <= circuitX1:
                nouvelle_x2 = circuitX1
        elif sparksX2 == circuitX1 and sparksY2 > circuitY1:
            nouvelle_y2 = sparksY2 - vitesse
            if nouvelle_y2 <= circuitY1:
                nouvelle_y2 = circuitY1
        elif sparksY2 == circuitY1 and sparksX2 < circuitX2:
            nouvelle_x2 = sparksX2 + vitesse
            if nouvelle_x2 >= circuitX2:
                nouvelle_x2 = circuitX2

        efface('sparks')
        sparksX = nouvelle_x
        sparksY = nouvelle_y
        sparks = cercle(sparksX, sparksY, 4, 'red', '', 2, tag='sparks')
        sleep(0.1)
        mise_a_jour()

        efface('sparks2')
        sparksX2 = nouvelle_x2
        sparksY2 = nouvelle_y2
        sparks2 = cercle(sparksX2, sparksY2, 4, 'red', '', 2, tag='sparks2')
        sleep(0.1)
        mise_a_jour()


    # TODO Les vies du joueur 

    # TODO Niveaux et vitesses qui augmentent 

    




