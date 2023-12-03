from fltk import *
from time import *
from math import *
from random import *

##### Constante utilisées pour le jeu #####

# Fenêtre 
dim_fenetre = 600


# Circuit
esp_circuit = 15
circuitX1 = esp_circuit
circuitY1 = 90      # ordonnée du premier coin du circuit (=hauteur du début du rectangle)
circuitX2 = dim_fenetre - esp_circuit
circuitY2 = dim_fenetre - esp_circuit


# Joueur
player_size = 8
x_player = dim_fenetre // 2
y_player = dim_fenetre - esp_circuit
# x_player = 400
# y_player = 400
direction = None
dep = 5


# Sparx
sparx_size = player_size
x1_sparx = dim_fenetre // 2     # abscisse du sparx 1
y1_sparx = circuitY1    # ordonnée du sparx 1
dir_sparx1 = 'droite'
x2_sparx = x1_sparx     # abscisse du sparx 2
y2_sparx = y1_sparx     # ordonnée du sparx 2
dir_sparx2 = 'gauche'

 
# Qix
x_qix = dim_fenetre // 2
y_qix = x_qix


# Texte du jeu
life = 'Vie restante'


##### Fonctions d'initialisation du jeu #####

def ready():
    texte(
        dim_fenetre // 2, dim_fenetre // 2,
        "Tapez sur une touche !", "red", "center",
        tag='texte'
    )
    attend_ev()
    efface('texte')


def init_circuit():
    rectangle(circuitX1, circuitY1, circuitX2, circuitY2, 'white', tag='circuit')


def init_player():
    cercle(x_player, y_player, player_size, 'yellow', '', 2, tag='player')


def init_sparx():
    cercle(x1_sparx, y1_sparx, sparx_size, 'red', '', 2, tag='sparx1')
    cercle(x2_sparx, y2_sparx, sparx_size, 'red', '', 2, tag='sparx2')


def init_text_life():
    life = 'Vie restante :'
    size_life = 17
    police = 'Stencil'
    texte(430, 10, life, 'red', police=police, taille=size_life)


def init_text_qix():
    chaine = 'Qix'
    size = 50
    police = 'Stecil'
    texte(300, 40, chaine, 'blue', police=police, taille=size, ancrage='center')


def init_text():
    init_text_life()
    init_text_qix()


def init_game():
    init_circuit()
    init_player()
    init_sparx()
    init_text()


def main():
    cree_fenetre(dim_fenetre, dim_fenetre)
    rectangle(0, 0, dim_fenetre, dim_fenetre, 'black', 'black', tag="background")
    ready()
    init_game()

##### Fonctions du jeu #####

##### Les déplacements #####

def mise_a_jour_direction(direction):
    nouvelle_dir = direction
    ev = donne_ev()
    t_ev = type_ev(ev)
    if t_ev == "Touche":
        t = touche(ev)
        if t == "Right":
            nouvelle_dir = 'droite'
        elif t == "Left":
            nouvelle_dir = 'gauche'
        if t == "Up":
            nouvelle_dir = 'haut'
        elif t == "Down":
            nouvelle_dir = 'bas'
        if t == "Return":
            nouvelle_dir = 'entree'
        elif t == "Escape":
            nouvelle_dir = 'echap'
    return nouvelle_dir


def quitte():
    ev = donne_ev()
    t_ev = type_ev(ev)
    if t_ev == 'Quitte':
        return True
    return False


def init_deplace(direction, x, y):
    if direction == 'droite' and x < circuitX2:
        x += dep
    elif direction == 'gauche' and x > circuitX1:
        x -= dep
    elif direction == 'haut' and y > circuitY1:
        y -= dep
    elif direction == 'bas' and y < circuitY2:
        y += dep
    return x, y


def dep_player(direction, x_player ,y_player):
    efface('player')
    x_player, y_player = init_deplace(direction, x_player, y_player)
    init_player()
    return x_player, y_player


def dep_sparx(dir_sparx, x_sparx, y_sparx, num_sparx):
    efface(f'sparx{num_sparx}')
    x_sparx, y_sparx = init_deplace(dir_sparx, x_sparx, y_sparx)
    return x_sparx, y_sparx

##### Fonctions sur les bases du circuit #####

def segments_initiaux():
    lst = [((circuitX1, circuitY2), (circuitX2, circuitY2)), # segment inférieur
           ((circuitX2, circuitY1), (circuitX2, circuitY2)), # segment droit
           ((circuitX1, circuitY1), (circuitX2, circuitY1)), # segment supérieur
           ((circuitX1, circuitY1), (circuitX1, circuitY2))] # segment gauche
    return lst


def on_circuit_player(x, y):
    test_x, test_y = dep_player(direction, x, y)
    for i in liste_points:
        if ((i[0][0] == i[1][0] == test_x and i[0][1] <= test_y <= i[1][1]) or (i[0][0] == i[1][0] == test_x and i[1][1] <= test_y <= i[0][1])) or ((i[0][1] == i[1][1] == test_y and i[0][0] <= test_x <= i[1][0]) or (i[0][1] == i[1][1] == test_y and i[1][0] <= test_x <= i[0][0])):
            return True
    return False


def on_circuit_sparx(dir_sparx, x, y, num_sparx):
    test_x, test_y = dep_sparx(dir_sparx, x, y, num_sparx)
    for i in liste_points:
        if ((i[0][0] == i[1][0] == test_x and i[0][1] <= test_y <= i[1][1]) or (i[0][0] == i[1][0] == test_x and i[1][1] <= test_y <= i[0][1])) or ((i[0][1] == i[1][1] == test_y and i[0][0] <= test_x <= i[1][0]) or (i[0][1] == i[1][1] == test_y and i[1][0] <= test_x <= i[0][0])):
            return True
    return False


def segments_par_coords():
    liste_total = []
    for i in range(len(coords_poly) -1):
        segment = (tuple(coords_poly[i]), tuple(coords_poly[i+1]))
        liste_total.append(segment)
    return liste_total


def dessin_ligne(x, y):
    test_x, test_y = dep_player(direction, x, y)
    ligne(x, y, test_x, test_y, 'white', tag='ligne')


if __name__ == "__main__":
    main()

    liste_points = segments_initiaux()      # liste des segments du circuit
    coords_poly = []        # liste des coordonnées du futur polygone à dessiner

    temps = 0
    touche_entree = 0 

    while True:
        old_direction = direction   # enregistre l'ancienne direction avant MAJ
        direction = mise_a_jour_direction(direction)

        if direction == 'echap':
            ferme_fenetre()
            break

        #### Déplacement du joueur ####
        if temps % 5 == 0 and touche_entree == 0 and on_circuit_player(x_player, y_player):     # si joueur sur circuit, le faire déplacer
            x_player, y_player = dep_player(direction, x_player, y_player)

        #### Déplacement du sparx ####
        if temps % 5 == 0 and on_circuit_sparx(dir_sparx1, x1_sparx, y1_sparx, 1) and on_circuit_sparx(dir_sparx2, x2_sparx, y2_sparx, 2):      # si les sparxs sont sur le circuit, les faires se déplacer
            x1_sparx, y1_sparx = dep_sparx(dir_sparx1, x1_sparx, y1_sparx, 1)
            x2_sparx, y2_sparx = dep_sparx(dir_sparx2, x2_sparx, y2_sparx, 2)
            init_sparx()    # affiche les sparxs après leur déplacement 

        #### Dessins ####
        if direction == 'entree':
            touche_entree = 1

        if touche_entree == 1 and old_direction != direction:   # si changement de direction pendant le dessin
            coords_poly.append(tuple((x_player, y_player)))

        if temps % 5 == 0 and touche_entree == 1:   # si touche entrée pressée, le joueur se déplace dans l'air complète
           
            if on_circuit_player(x_player, y_player):   # si joueur revient sur circuit, dessin du polygone et ajout des lignes au circuit
                x_player, y_player = dep_player(direction, x_player, y_player)

                coords_poly.append(tuple((x_player, y_player)))

                polygone(coords_poly, 'white', 'green', tag='polygone')
                liste_points.extend(segments_par_coords())
                coords_poly = []
                efface('ligne')     # évite d'avoir les lignes dessinés en plus des lignes du polygone (qui sont les mêmes)

                touche_entree = 0   # permet de ressortir de la boucle 'entrée'
            else:
                dessin_ligne(x_player, y_player)
                x_player, y_player = dep_player(direction, x_player, y_player)
            
        
        if quitte():    ## ne fonctionne pas ##
            ferme_fenetre()
            break

        temps = temps + 1
        mise_a_jour()


    attend_ev()
    ferme_fenetre()