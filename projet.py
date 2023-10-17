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

    # TODO Déplacements du joueur

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
    while mov ==0:
        #Pour quitter la fênetre
        ev = donne_ev()
        tev = type_ev(ev)
        if supp!=5:
            supp+=1
            qix(x_qix,y_qix,x1_qix,y1_qix)
            #Pour commencer:Il commence donc au milieu
            if x_qix==250 and y_qix==250 and x1_qix==300 and y1_qix==250:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix+vitesse_qix)))
                sleep(0.5)
                mise_a_jour()

            if y_qix<=circuitY1 or y1_qix<=circuitY1: 
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix),(y1_qix+vitesse_qix)))
                sleep(0.5)
                mise_a_jour()
  

            if y_qix>=circuitY2 or y1_qix>=circuitY2:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix)))
                sleep(0.5)
                mise_a_jour()
       
            if x_qix<=circuitX1 or x1_qix<=circuitX1:
                x_qix=(randint((x_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix))) 
                sleep(0.5)               
                mise_a_jour()

            if x_qix>=circuitX2 or x1_qix>=circuitX2:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix+vitesse_qix)))
                sleep(0.5)
                mise_a_jour()
      

            else:
                x_qix=(randint((x_qix-vitesse_qix),(x_qix+vitesse_qix)))
                y_qix=(randint((y_qix-vitesse_qix),(y_qix+vitesse_qix)))
                x1_qix=(randint((x1_qix-vitesse_qix),(x1_qix+vitesse_qix)))
                y1_qix=(randint((y1_qix-vitesse_qix),(y1_qix+vitesse_qix)))           
                sleep(0.5)
                mise_a_jour()

        else:
            efface('qix')
            supp-=1

        if tev == 'Touche':
            nom_touche = touche(ev)
            if nom_touche =="Escape":
                ferme_fenetre()
            



    # TODO Les vies du joueur 

    # TODO Niveaux et vitesses qui augmentent 

    attend_fermeture()
    
