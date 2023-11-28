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


def dep_sparx1(dir_sparx, x1_sparx, y1_sparx):
    efface('sparx1')
    x1_sparx, y1_sparx = init_deplace(dir_sparx, x1_sparx, y1_sparx)
    return x1_sparx, y1_sparx


def dep_sparx2(dir_sparx, x2_sparx, y2_sparx):
    efface('sparx2')
    x2_sparx, y2_sparx = init_deplace(dir_sparx, x2_sparx, y2_sparx)
    return x2_sparx, y2_sparx


def generate_pts_circuit():
    liste_points = []

    for i in range(circuitX1, circuitX2 + 1, dep):    # segment horizontal haut
        liste_points.append((i, circuitY1))
    for i in range(circuitX1, circuitX2 + 1, dep):     # segment horizontal bas
        liste_points.append((i, circuitY2))
    for i in range(circuitY1, circuitY2 + 1, dep):      # segment vertical gauche
        liste_points.append((circuitX1, i))
    for i in range(circuitY1, circuitY2 + 1, dep):      # segment vertical droit
        liste_points.append((circuitX2, i))
    return liste_points


def on_circuit_player(x, y):
    test_x_player, test_y_player = dep_player(direction, x, y)
    if (test_x_player , test_y_player) in liste_points:
        return True
    else:
        return False
    

def on_circuit_sparx1(dir_sparx, x, y):
    test_x1_sparx, test_y1_sparx = dep_sparx1(dir_sparx, x, y)
    if (test_x1_sparx, test_y1_sparx) in liste_points:
        return True
    else:
        return False
    

def on_circuit_sparx2(dir_sparx, x, y):
    test_x2_sparx, test_y2_sparx = dep_sparx2(dir_sparx, x, y)
    if (test_x2_sparx, test_y2_sparx) in liste_points:
        return True
    else:
        return False


def dessin_ligne(x_player, y_player):
    test_x_player, test_y_player = dep_player(direction, x_player, y_player)

    ligne(x_player, y_player, test_x_player, test_y_player, 'white', tag='dessin')
    ligne_lst = [(x_player, y_player), (test_x_player, test_y_player)]
    return ligne_lst


# def choose_dir(dir_sparx):
#     lst_dir = [dir_sparx]
#     if dir_sparx == 'droite':
#         lst_dir.extend(['haut', 'bas'])
#     elif dir_sparx == 'haut':
#         lst_dir.extend(['gauche', 'droite'])
#     elif dir_sparx == 'gauche':
#         lst_dir.extend(['haut', 'bas'])
#     elif dir_sparx == 'bas':
#         lst_dir.extend(['droite', 'gauche'])
#     return lst_dir


# def test_turn_sparx(liste_directions, dir_sparx, x1_sparx, y1_sparx):
#     lst_dispo = []
#     for i in liste_directions:
#         if (i == 'haut' and y1_sparx == circuitY1) or (i == 'bas' and y1_sparx == circuitY2) or (i == 'gauche' and x1_sparx == circuitX1) or (i == 'droite' and x1_sparx == circuitX2):
#             pass
#         else:
#             test_x1_sparx, test_y1_sparx = dep_sparx1(i, x1_sparx, y1_sparx)
#             if on_circuit_sparx1(dir_sparx, test_x1_sparx, test_y1_sparx):
#                 lst_dispo.append(i)
#     return lst_dispo

def turn_sparx():
    pass


if __name__ == "__main__":
    main()

    liste_points = generate_pts_circuit()
    liste_poly = []

    temps = 0
    touche_entree = 0 

    while True:
        direction = mise_a_jour_direction(direction)
        if direction == 'echap':
            ferme_fenetre()
            break

        if temps % 5 == 0 and touche_entree == 0 and on_circuit_player(x_player, y_player):   # déplacement du joueur sur le circuit
            x_player, y_player = dep_player(direction, x_player, y_player)


        if temps % 5 == 0 and on_circuit_sparx1(dir_sparx1, x1_sparx, y1_sparx) and on_circuit_sparx2(dir_sparx2, x2_sparx, y2_sparx):
            x1_sparx, y1_sparx = dep_sparx1(dir_sparx1, x1_sparx, y1_sparx)
            x2_sparx, y2_sparx = dep_sparx2(dir_sparx2, x2_sparx, y2_sparx)

            # lst_dir = choose_dir(dir_sparx1)
            # lst_dir_dispo = test_turn_sparx(lst_dir, dir_sparx1, x1_sparx, y1_sparx)
            # dir_sparx1 = choice(lst_dir_dispo)
            
            init_sparx()

        if direction == 'entree':
            touche_entree = 1

        if temps % 5 == 0 and touche_entree == 1:   # si touche entrée pressée, le joueur se déplace dans l'air complète

            if on_circuit_player(x_player, y_player):     # si le joueur revient sur le circuit, dessiner puis quitter la boucle entree
                liste_poly.extend(dessin_ligne(x_player, y_player))     # ajoute les lignes dessinées à la liste de points du polygone
                x_player, y_player = dep_player(direction, x_player, y_player)  # applique le déplacement

                polygone(liste_poly, 'white', 'green', tag=polygone)    # dessine le polygone
                liste_points.extend(liste_poly)     # ajoute les lignes dessinées à la liste de points

                touche_entree = 0   # pour quitter la boucle entree
                liste_poly = []
            # elif len(liste_poly) != len(set(liste_poly)):    # si le joueur intersecte son dessin
                # break
            else:
                liste_poly.extend(dessin_ligne(x_player, y_player))     # ajoute les lignes dessinées à la liste de points du polygone
                x_player, y_player = dep_player(direction, x_player, y_player)

        temps = temps + 1
        print(temps)
        mise_a_jour()


    attend_ev()
    ferme_fenetre()