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
life_player = 3
speed_player = 5


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
vitesse_qix = 1
midle_qix = 30

x_qix2=200
y_qix2=200



# Texte du jeu
text_life = 'Vie restante'

# Obstacles 
nb_obstacles = 0

#Pomme
pomme_size=20
pommes = []

#Invincible
invincible=False
temps_invincible = 0
duree_invincibilite = 3

#choix Jeu

##### Fonctions d'initialisation du jeu #####

def ready():
    texte(
        dim_fenetre // 2, dim_fenetre // 2,
        "Tapez sur une touche !", "red", "center",
        tag='texte'
    )
    attend_ev()
    efface('texte')

def ecriture():
        choix_jeu=None
        texte(300, 200,"Qix Basique", "red", "center",tag='qix_basique')
        rectangle(200,150,400,250,"blue",tag='rectangle1')
        texte(300, 400,"Qix Difficile", "red", "center",tag='qix_difficile')
        rectangle(200,350,400,450,"blue",tag='rectangle1')

        clicx,clicy=attend_clic_gauche()
        if clicx>=200 and clicx<=400 and clicy>=150 and clicy<=250:
            efface('rectangle1')
            efface('qix_basique')
            efface('qix_difficile')
            choix_jeu='Basique'
            return choix_jeu
        
        if clicx>=200 and clicx<=400 and clicy>=350 and clicy<=450:
            efface('rectangle1')
            efface('qix_basique')
            efface('qix_difficile')
            choix_jeu="Difficile"
            return choix_jeu

def init_circuit():
    rectangle(circuitX1, circuitY1, circuitX2, circuitY2, 'white', tag='circuit')


def init_player():
    cercle(x_player, y_player, player_size, 'yellow', '', 2, tag='player')


def init_sparx():
    cercle(x1_sparx, y1_sparx, sparx_size, 'red', '', 2, tag='sparx1')
    cercle(x2_sparx, y2_sparx, sparx_size, 'red', '', 2, tag='sparx2')

def init_qix():
    image(x_qix,y_qix,'kong.png',largeur=60,hauteur=60,ancrage="center",tag='kong1')

def init_qix2():
    image(x_qix2,y_qix2,'kong.png',largeur=60,hauteur=60,ancrage="center",tag='kong2')

def init_life(life_player):
    chaine = str(life_player)
    size_life = 17
    # police = 'Stencil'
    texte(570, 10, chaine, 'red', taille=size_life, tag='life')


def init_text_life():
    text_life = 'Vie restante :'
    size__text_life = 17
    # police = 'stencil'
    texte(430, 10, text_life, 'red', taille=size__text_life, tag='text_life')
    init_life(life_player)


def init_text_qix():
    chaine = 'Qix'
    size = 50
    # police = 'Stencil'
    texte(300, 40, chaine, 'blue', taille=size, ancrage='center')

def init_invincible():
    texte_invincible="Invincible"
    size_invicible=17
    texte(60,50,texte_invincible,'green',taille=size_invicible,ancrage='center',tag="Invincible")

def init_pomme():
    global pommes 
    nom = 'pomme'
    for i in range(randint(5, 8)):
        x_pomme = randint(16, 584)
        y_pomme = randint(91, 584)
        tag_pomme = f'{nom}_{i}'
        image(x_pomme, y_pomme, 'pomme.png', largeur=pomme_size, hauteur=pomme_size, ancrage='center', tag=tag_pomme)
        pommes.append({'x': x_pomme, 'y': y_pomme, 'tag': tag_pomme})

def init_text():
    init_text_life()
    init_text_qix()

def init_game(choix_jeu):
    init_circuit()
    init_player()
    init_sparx()
    init_text()
    init_qix()
    init_pomme()
    if choix_jeu=="Difficile":
        init_qix2()

def main():
    cree_fenetre(dim_fenetre, dim_fenetre)
    rectangle(0, 0, dim_fenetre, dim_fenetre, 'black', 'black', tag="background")
    choix_jeu=ecriture()
    return choix_jeu


def init_obstacle(x, y, num_obstacle):
    cercle(x, y, 5, 'red', 'red', tag=f'obstacle{num_obstacle}')


def init_gameover():
    efface('kong')
    efface('sparx1')
    efface('sparx2')
    efface('player')
    chaine = 'GAME OVER'
    size = 50
    police ="Stencil"
    texte(300, 300, chaine, 'red', 'center', police, size, 'Game Over')


def quitte():
    ev = donne_ev()
    t_ev = type_ev(ev)
    if t_ev == 'Touche':
        return True
    return False

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
        if t == "space":
            nouvelle_dir = 'espace'
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


def dep_sparx(dir_sparx, x_sparx, y_sparx, num_sparx):
    efface(f'sparx{num_sparx}')
    x_sparx, y_sparx = init_deplace(dir_sparx, x_sparx, y_sparx)
    return x_sparx, y_sparx


def choose_dir(dir_sparx):
    lst_dir = [dir_sparx]
    if dir_sparx == 'droite':
        lst_dir.extend(['haut', 'bas'])
    elif dir_sparx == 'haut':
        lst_dir.extend(['gauche', 'droite'])
    elif dir_sparx == 'gauche':
        lst_dir.extend(['haut', 'bas'])
    elif dir_sparx == 'bas':
        lst_dir.extend(['droite', 'gauche'])
    return lst_dir


def test_turn_sparx(lst_directions, x_sparx, y_sparx, num_sparx):
    lst_dispo = []
    for i in lst_directions:
        if (i == 'haut' and y_sparx == circuitY1) or (i == 'bas' and y_sparx == circuitY2) or (i == 'gauche' and x_sparx == circuitX1) or (i == 'droite' and x_sparx == circuitX2):
            pass
        else:
            test_x1_sparx, test_y1_sparx = dep_sparx(i, x_sparx, y_sparx, num_sparx)
            if on_circuit_sparx(i, test_x1_sparx, test_y1_sparx, num_sparx):
                lst_dispo.append(i)
    return lst_dispo


def turn_sparx(dir_sparx1, dir_sparx2):
    lst_dir_1 = choose_dir(dir_sparx1)
    lst_dir_dispo_1 = test_turn_sparx(lst_dir_1, x1_sparx, y1_sparx, 1)

    lst_dir_2 = choose_dir(dir_sparx2)
    lst_dir_dispo_2 = test_turn_sparx(lst_dir_2, x2_sparx, y2_sparx, 2)
    try:
        dir_sparx1 = choice(lst_dir_dispo_1)
    except:
        pass
    try:
        dir_sparx2 = choice(lst_dir_dispo_2)
    except:
        pass
    return dir_sparx1, dir_sparx2


def dep_qix(x_qix, y_qix,num_qix):
    efface(f'kong{num_qix}')
    facteur = 3.0
    plage_deplacement = vitesse_qix * facteur

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Haut, Droite, Bas, Gauche
    dx, dy = choice(directions)

    # Générer un vecteur de déplacement aléatoire
    deplacement_x = dx * plage_deplacement
    deplacement_y = dy * plage_deplacement

    nouvelle_x = x_qix + deplacement_x
    nouvelle_y = y_qix + deplacement_y

    # Assurer que les nouvelles coordonnées restent dans les limites
    nouvelle_x = max(circuitX1 + midle_qix, min(circuitX2 - midle_qix, nouvelle_x))
    nouvelle_y = max(circuitY1 + midle_qix, min(circuitY2 - midle_qix, nouvelle_y))

    return nouvelle_x, nouvelle_y

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
        xA, yA, xB, yB = i[0][0], i[0][1], i[1][0], i[1][1]
        if ((xA == xB == test_x and yA <= test_y <= yB) or (xA == xB == test_x and yB <= test_y <= yA)) or ((yA == yB == test_y and xA <= test_x <= xB) or (yA == yB == test_y and xB <= test_x <= xA)):
            return True
    return False


def on_circuit_sparx(dir_sparx, x, y, num_sparx):
    test_x, test_y = dep_sparx(dir_sparx, x, y, num_sparx)
    for i in liste_points:
        xA, yA, xB, yB = i[0][0], i[0][1], i[1][0], i[1][1]
        if ((xA == xB == test_x and yA <= test_y <= yB) or (xA == xB == test_x and yB <= test_y <= yA)) or ((yA == yB == test_y and xA <= test_x <= xB) or (yA == yB == test_y and xB <= test_x <= xA)):
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


def reset():
    global x_qix, y_qix, x_player, y_player, x1_sparx, y1_sparx, x2_sparx, y2_sparx, touche_entree, dir_sparx1, dir_sparx2, direction,invincible
    touche_entree = 0 
    x_qix = 300
    y_qix = 300
    x_player = dim_fenetre // 2
    y_player = dim_fenetre - esp_circuit
    direction = None
    x1_sparx = dim_fenetre // 2     # abscisse du sparx 1
    y1_sparx = circuitY1    # ordonnée du sparx 1          
    x2_sparx = x1_sparx     
    y2_sparx = y1_sparx
    dir_sparx1 = 'droite'
    dir_sparx2 = 'gauche'
    invincible=False

    efface('ligne')

##### Collisions #####

def collision_qix_player(x_qix,y_qix,x_player,y_player):
    distance = sqrt((x_qix - x_player) ** 2 + (y_qix - y_player) ** 2)
    return distance < player_size


def intersection_ligne_qix(x_qix, y_qix, coords_ligne):
    """
    Vérifie si le Qix touche la ligne dessinée.
    :param float x_qix: Coordonnée x du Qix.
    :param float y_qix: Coordonnée y du Qix.
    :param list[tuple[float, float]] coords_ligne: Coordonnées de la ligne.
    :return: True si le Qix touche la ligne, sinon False.
    """
    global coords_poly
    for i in range(len(coords_ligne) - 1):
        x1, y1 = coords_ligne[i]
        x2, y2 = coords_ligne[i + 1]
        distance1 = sqrt((x_qix - x1) ** 2 + (y_qix - y1) ** 2)
        distance2 = sqrt((x_qix - x2) ** 2 + (y_qix - y2) ** 2)
        longueur_segment = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        marge = 5
        if distance1 + distance2 - marge <= longueur_segment:
            return True
    return False


def collision_sparx(x_sparx, y_sparx, x_player, y_player):
    if sqrt((x_sparx - x_player) ** 2 + (y_sparx - y_player) ** 2)<= player_size:
        return True
    return False


def collision_obstacles(lst_osbtacles, x_player, y_player):
    for i in lst_osbtacles:
        if sqrt((i[0] - x_player) ** 2 + (i[1] - y_player) ** 2)<= player_size:
            return True
    return False

def collision_joueur_pomme():
    global pommes,invincible,temps_invincible
    for i in pommes[:]: 
        x_pomme, y_pomme, tag_pomme = i['x'], i['y'], i['tag']
        distance = sqrt((x_pomme - x_player) ** 2 + (y_pomme - y_player) ** 2)
        if distance < player_size + pomme_size / 2:
            pommes.remove(i)
            efface(tag_pomme)
            invincible = True
            temps_invincible = time()



##### Obstacles #####
def point_random_on_segment(segment):
    """ Renvoi un point appartenant à un segment donné """
    x1, y1 = segment[0]
    x2, y2 = segment[1]
    x = uniform(min(x1, x2), max(x1, x2))
    y = uniform(min(y1, y2), max(y1, y2))
    return (x, y)


def segment_random(liste_points):
    """ Renvoi un point aléatoire appartenant au circuit entier """
    if not liste_points:
        return None
    segment_choisi = choice(liste_points)
    return point_random_on_segment(segment_choisi)


def spawn_obstacle():
    x, y = segment_random(liste_points)
    init_obstacle(x, y, nb_obstacles)
    return x, y


if __name__ == "__main__":
    choix_jeu=main()
    ready()
    print(choix_jeu)
    init_game(choix_jeu)
        
    liste_points = segments_initiaux()      # liste des segments du circuit
    coords_poly = []        # liste des coordonnées du futur polygone à dessiner
    liste_osbtacles = []        # liste des coordonnées des osbtacles

    temps = 0
    touche_entree = 0       # touche qui permet le dessin
    touche_espace = 0       # touche qui permet l'accélération du joueur



    
    while True:
        old_direction = direction   # enregistre l'ancienne direction avant MAJ
        direction = mise_a_jour_direction(direction)

        if direction == 'echap':
            ferme_fenetre()
            break

        #### Déplacement du joueur ####
        if temps % speed_player == 0 and touche_entree == 0 and on_circuit_player(x_player, y_player):     # si joueur sur circuit, le faire déplacer
            x_player, y_player = dep_player(direction, x_player, y_player)

        #### Déplacement des sparx ####
        if temps % 5 == 0 and (on_circuit_sparx(dir_sparx1, x1_sparx, y1_sparx, 1) or on_circuit_sparx(dir_sparx2, x2_sparx, y2_sparx, 2)):      # si les sparxs sont sur le circuit, les faires se déplacer
            dir_sparx1, dir_sparx2 = turn_sparx(dir_sparx1, dir_sparx2)
            
            x1_sparx, y1_sparx = dep_sparx(dir_sparx1, x1_sparx, y1_sparx, 1)
            x2_sparx, y2_sparx = dep_sparx(dir_sparx2, x2_sparx, y2_sparx, 2)

        init_sparx()    # affiche les sparxs après leur déplacement 

        #### Déplacement du qix ####
        x_qix, y_qix = dep_qix(x_qix, y_qix,1)
        init_qix()
        
        if choix_jeu=="Difficile":
            x_qix2,y_qix2=dep_qix(x_qix2,y_qix2,2)
            init_qix2()

        #### Dessins ####
        if direction == 'entree':
            touche_entree = 1

        if touche_entree == 1 and old_direction != direction:   # si changement de direction pendant le dessin
            coords_poly.append(tuple((x_player, y_player)))

        if temps % speed_player == 0 and touche_entree == 1:   # si touche entrée pressée, le joueur se déplace dans l'air complète
        
            if direction == 'espace' and touche_espace == 0:
                speed_player //= 2
                touche_espace = 1

            if on_circuit_player(x_player, y_player):   # si joueur revient sur circuit, dessin du polygone et ajout des lignes au circuit
                x_player, y_player = dep_player(direction, x_player, y_player)

                coords_poly.append(tuple((x_player, y_player)))

                polygone(coords_poly, 'white', 'green', tag='polygone')
                liste_points.extend(segments_par_coords())
                coords_poly = []

                efface('ligne')     # évite d'avoir les lignes dessinés en plus des lignes du polygone (qui sont les mêmes)
                touche_entree = 0   # permet de ressortir de la boucle 'entrée'
                touche_espace = 0   # permet de remettre la vitesse initiale du joueur
                speed_player = 5
            else:
                dessin_ligne(x_player, y_player)
                x_player, y_player = dep_player(direction, x_player, y_player)

        #### Collisions ####
        collision_joueur_pomme()
        if invincible:
            init_invincible()
            temps_actuel = time()
            temps_ecoule_invincible = temps_actuel - temps_invincible

            if temps_ecoule_invincible >= duree_invincibilite:
                invincible = False  
        if invincible:
            pass
        else:
            efface('Invincible')
            if collision_qix_player(x_qix,y_qix,x_player,y_player)or collision_qix_player(x_qix2,y_qix2,x_player,y_player) or intersection_ligne_qix(x_qix2,y_qix2,coords_poly) or collision_sparx(x1_sparx,y1_sparx,x_player,y_player) or collision_sparx(x2_sparx,y2_sparx,x_player,y_player):
                life_player -= 1
                coords_poly = []
                reset()
                efface('life')
                init_life(life_player)

        if life_player == 2 and nb_obstacles == 0:
            liste_osbtacles.append(spawn_obstacle())
            nb_obstacles += 1
        if life_player == 1 and nb_obstacles == 1:
            liste_osbtacles.append(spawn_obstacle())
            nb_obstacles += 1


        if collision_obstacles(liste_osbtacles, x_player, y_player):
            direction = None

        
        if life_player == 0:
            init_gameover()
            break

        if quitte():    ## ne fonctionne pas ##
            print('oui')
            ferme_fenetre()
            break

        temps = temps + 1
        mise_a_jour()


    attend_ev()
    ferme_fenetre()


     