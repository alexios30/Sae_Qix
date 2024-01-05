from fltk import *
from time import *
from math import *
from random import *


##### Constante utilisées pour le jeu #####

# Fenêtre 
dim_fenetre = 600

##### Mode de jeu choisit #####
choix_jeu = None


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

x_player2 = dim_fenetre - esp_circuit
y_player2 = dim_fenetre // 2
direction2 = None
speed_player2 = 5
life_player2 = 3

# Sparx
sparx_size = player_size
x1_sparx = dim_fenetre // 2     # abscisse du sparx 1
y1_sparx = circuitY1    # ordonnée du sparx 1
dir_sparx1 = 'droite'
x2_sparx = x1_sparx     # abscisse du sparx 2
y2_sparx = y1_sparx     # ordonnée du sparx 2
dir_sparx2 = 'gauche'
x3_sparx = circuitX1
y3_sparx = circuitY1
dir_sparx3 = dir_sparx1

 
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

# Pomme
pomme_size=30
pommes = []

# Invincibilité 
invincible=False
temps_invincible = 0
duree_invincibilite = 3


##### Fonctions d'initialisation du jeu #####

def ready():
    """Affiche le texte de départ"""
    texte(
        dim_fenetre // 2, dim_fenetre // 3,
        "Voici les commandes : \n \n\
            - Les flèches directionnelles pour se déplacer \n \n\
            - Presser la touche Enter puis rentrer \n\
            dans l'air (flèches) pour dessiner \n \n\
            - Espace pendant le dessin pour \n\
            accélerer \n \n\
            - Escape pour quitter \n \n\
            (Appuyer sur une touche pour commencer \n\
            à jouer)", 
        "white", "center", taille=18, tag='texte'
    )
    texte(
        dim_fenetre // 2, dim_fenetre // 1.2,
        "Good luck !", "green", "center", taille=26, tag='texte'
    )
    attend_ev()
    efface('texte')


def ecriture_menu():
    """Affiche les case du menu"""
    texte(300, 100, "Qix Basique", "white", "center", tag='qix_basique')
    rectangle(200, 50, 400, 150, "blue", tag='rectangle1')

    texte(300, 300, "Qix Difficile", "red", "center", tag='qix_difficile')
    rectangle(200, 250, 400, 350, "blue", tag='rectangle1')

    texte(300, 500, "Versus", "purple", "center", tag='versus')
    rectangle(200, 450, 400,550, "blue", tag='rectangle1')


def menu():
    """Renvoi le mode de jeu choisit après le clic"""
    ecriture_menu()
    valid = True
    while valid:
        clicx, clicy = attend_clic_gauche()
        if clicx >= 200 and clicx <= 400 and clicy >= 50 and clicy <= 150:
            efface('rectangle1')
            efface('qix_basique')
            efface('qix_difficile')
            efface('versus')
            choix_jeu = 'Basique'
            valid = False
        
        elif clicx >= 200 and clicx <= 400 and clicy >= 250 and clicy <= 350:
            efface('rectangle1')
            efface('qix_basique')
            efface('qix_difficile')
            efface('versus')
            choix_jeu = "Difficile"
            valid = False

        elif clicx >= 200 and clicx <= 400 and clicy >= 450 and clicy <= 550:
            efface('rectangle1')
            efface('qix_basique')
            efface('qix_difficile')
            efface('versus')
            choix_jeu = "Versus"
            valid = False
    return choix_jeu


def init_circuit():
    """Affiche le circuit"""
    rectangle(circuitX1, circuitY1, circuitX2, circuitY2, 'white', tag='circuit')


def init_player():
    """Affiche le joueur"""
    cercle(x_player, y_player, player_size, 'yellow', '', 2, tag='player')

def init_player2():
    """Affiche le 2 eme joueur"""
    cercle(x_player2, y_player2, player_size, 'purple', '', 2, tag='player2')


def init_sparx():
    """Affiche les sparxs"""
    cercle(x1_sparx, y1_sparx, sparx_size, 'red', '', 2, tag='sparx1')
    cercle(x2_sparx, y2_sparx, sparx_size, 'red', '', 2, tag='sparx2')
    if choix_jeu=='Difficile':
        cercle(x3_sparx, y3_sparx, sparx_size, 'red', '', 2, tag='sparx3')


def init_qix():
    """Affiche le premier qix"""
    image(x_qix,y_qix,'kong.png',largeur=60,hauteur=60,ancrage="center",tag='kong1')


def init_qix2():
    """Affiche le qix numéro 2"""
    image(x_qix2, y_qix2, 'kong.png',largeur=60,hauteur=60,ancrage="center",tag='kong2')


def init_life(life_player: int):
    """Affiche le nombre de vie"""
    chaine = str(life_player)
    size_life = 17
    texte(570, 10, chaine, 'yellow', taille=size_life, tag='life')

def init_life2(life_player2: int):
    """Affiche le nombre de vie"""
    chaine = str(life_player2)
    size_life = 17
    texte(175, 10, chaine, 'yellow', taille=size_life, tag='life2')

def init_text_life():
    """Affiche le texte `Vie restante`"""
    text_life = 'Vie Joueur 1:'
    size__text_life = 17
    texte(430, 10, text_life, 'red', taille=size__text_life, tag='text_life')
    init_life(life_player)

def init_text_life2():
    """Affiche le texte `Vie restante`"""
    text_life = 'Vie Joueur 2 :'
    size__text_life = 17
    texte(30, 10, text_life, 'red', taille=size__text_life, tag='text_life')
    init_life2(life_player2)

def init_text_qix():
    """Affiche le texte `Qix`"""
    chaine = 'Qix'
    size = 50
    texte(300, 40, chaine, 'blue', taille=size, ancrage='center')


def init_text_invincible():
    """Affiche le texte `Invincible`"""
    texte_invincible="Invincible"
    size_invicible=17
    texte(60,50,texte_invincible,'green',taille=size_invicible,ancrage='center',tag="Invincible")


def init_pomme():
    """Affiche les pommes"""
    global pommes 
    nom = 'pomme'
    for i in range(randint(5, 8)):
        x_pomme = randint(circuitX1 + 1, dim_fenetre-(circuitX1+1))
        y_pomme = randint(circuitY1 + 1, dim_fenetre-(circuitX1+1))
        tag_pomme = f'{nom}_{i}'
        image(x_pomme, y_pomme, 'pomme.png', largeur=pomme_size, hauteur=pomme_size, ancrage='center', tag=tag_pomme)
        pommes.append({'x': x_pomme, 'y': y_pomme, 'tag': tag_pomme})


def init_text():
    """Affiche l'ensemble des textes après lancement du jeu"""
    init_text_life()
    init_text_qix()


def init_game(choix_jeu):
    """Affiche tout le jeu"""
    init_circuit()
    init_player()
    init_text()
    init_sparx()
    init_qix()
    if choix_jeu=="Versus":
        init_player2()
        init_text_life2()
    else:
        init_pomme()
        if choix_jeu=="Difficile":
            init_qix2()

        


def main():
    """Permet de lancer le début du jeu"""
    cree_fenetre(dim_fenetre, dim_fenetre)
    rectangle(0, 0, dim_fenetre, dim_fenetre, 'black', 'black', tag="background")
    choix_jeu = menu()
    return choix_jeu


def init_obstacle(x: int, y: int, num_obstacle: int):
    """Affiche les obstacles"""
    cercle(x, y, 5, 'red', 'red', tag=f'obstacle{num_obstacle}')


def init_gameover():
    """Fonction de fin de jeu s'il est perdu"""
    efface('kong')
    efface('sparx1')
    efface('sparx2')
    efface('player')
    chaine = 'GAME OVER'
    size = 50
    police ="Stencil"
    texte(300, 300, chaine, 'red', 'center', police, size, 'Game Over')

def init_joueur1perdu():
    """Fonction de fin de jeu s'il est perdu"""
    efface('kong')
    efface('sparx1')
    efface('sparx2')
    efface('player')
    efface('player2')
    chaine = 'JOUEUR 1 A PERDU'
    size = 50
    police ="Stencil"
    texte(300, 300, chaine, 'red', 'center', police, size, 'Joueur1Perdu')

def init_joueur2perdu():
    """Fonction de fin de jeu s'il est perdu"""
    efface('kong')
    efface('sparx1')
    efface('sparx2')
    efface('player')
    efface('player2')
    chaine = 'JOUEUR 2 A PERDU'
    size = 50
    police ="Stencil"
    texte(300, 300, chaine, 'red', 'center', police, size, 'Joueur2Perdu')

##### Fonctions du jeu #####

##### Les déplacements #####

def mise_a_jour_direction(direction: str, direction2:str):
    """Renvoie la touche préssée (direction ou action)"""
    nouvelle_dir = direction
    nouvelle_dir2 = direction2
    ev = donne_ev()
    t_ev = type_ev(ev)
    if t_ev == "Touche":
        t = touche(ev)
        if t == "Right" :
            nouvelle_dir = 'droite'
        elif t == "Left":
            nouvelle_dir = 'gauche'
        if t == "Up" :
            nouvelle_dir = 'haut'
        elif t == "Down" :
            nouvelle_dir = 'bas'
        if t =="d" :
            nouvelle_dir2 = 'droite'
        elif t == "q":
            nouvelle_dir2 = 'gauche'
        if t == "z" :
            nouvelle_dir2 = 'haut'
        elif t == "s" :
            nouvelle_dir2 = 'bas'
        if t == "Return":
            nouvelle_dir = 'entree'
        if t=="f":
            nouvelle_dir2= 'entree'
        if t == "space":
            nouvelle_dir = 'espace'
        if t=='x':
            nouvelle_dir2= 'espace'
        elif t == "Escape":
            nouvelle_dir = 'echap'
    return nouvelle_dir,nouvelle_dir2


def init_deplace(direction: str, x: int, y: int):
    """Renvoie les coordonnées comprises dans l'air du circuit après déplacement dans la direction donnée"""
    if direction == 'droite' and x < circuitX2:
        x += dep
    elif direction == 'gauche' and x > circuitX1:
        x -= dep
    elif direction == 'haut' and y > circuitY1:
        y -= dep
    elif direction == 'bas' and y < circuitY2:
        y += dep
    return x, y

def init_deplace2(direction2: str, x: int, y: int):
    """Renvoie les coordonnées comprises dans l'air du circuit après déplacement dans la direction donnée"""
    if direction2 == 'droite' and x < circuitX2:
        x += dep
    elif direction2 == 'gauche' and x > circuitX1:
        x -= dep
    elif direction2 == 'haut' and y > circuitY1:
        y -= dep
    elif direction2 == 'bas' and y < circuitY2:
        y += dep
    return x, y



def dep_player(direction: str, x_player: int ,y_player: int):
    """Déplace le joueur en lui affectant ses nouvelles coordonnées"""
    efface('player')
    x_player, y_player = init_deplace(direction, x_player, y_player)
    init_player()
    return x_player, y_player

def dep_player2(direction2: str, x_player2: int ,y_player2: int):
    """Déplace le joueur en lui affectant ses nouvelles coordonnées"""
    efface('player2')
    x_player2, y_player2 = init_deplace2(direction2, x_player2, y_player2)
    init_player2()
    return x_player2, y_player2

def dep_sparx(dir_sparx: str, x_sparx: int, y_sparx: int, num_sparx: int):
    """Déplace le sparx en lui affectant ses nouvelles coordonnées"""
    efface(f'sparx{num_sparx}')
    x_sparx, y_sparx = init_deplace(dir_sparx, x_sparx, y_sparx)
    return x_sparx, y_sparx


def choose_dir(dir_sparx: str):
    """Renvoie les trois directions possibles du sparx en excluant le demi-tour"""
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


def test_turn_sparx(lst_directions: list, x_sparx: int, y_sparx: int, num_sparx: int):
    """Retourne la liste des directions que peut prendre le sparx en restant sur le circuit"""
    lst_dispo = []
    for i in lst_directions:
        if (i == 'haut' and y_sparx == circuitY1) or (i == 'bas' and y_sparx == circuitY2) or (i == 'gauche' and x_sparx == circuitX1) or (i == 'droite' and x_sparx == circuitX2):
            pass
        else:
            test_x1_sparx, test_y1_sparx = dep_sparx(i, x_sparx, y_sparx, num_sparx)
            if on_circuit_sparx(i, test_x1_sparx, test_y1_sparx, num_sparx):
                lst_dispo.append(i)
    return lst_dispo


def turn_sparx(dir_sparx: str, x_sparx: int, y_sparx: int, num_sparx: int):
    """Choisi et renvoie aléatoirement une direction que peut prendre le sparx sur le circuit"""
    lst_dir = choose_dir(dir_sparx)
    lst_dir_dispo = test_turn_sparx(lst_dir, x_sparx, y_sparx, num_sparx)
    try:
        dir_sparx = choice(lst_dir_dispo)
    except:
        pass
    return dir_sparx


def dep_qix(x_qix: int, y_qix: int, num_qix: int):
    """Test et renvoi les coordonnées de déplacement du qix en restant dans l'air du circuit"""
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

def segments_initiaux() -> list[tuple]:
    """Renvoie une liste comportant les segments du circuit sous forme `((xA, yA),(xB, yB))`"""
    lst = [((circuitX1, circuitY2), (circuitX2, circuitY2)), # segment inférieur
           ((circuitX2, circuitY1), (circuitX2, circuitY2)), # segment droit
           ((circuitX1, circuitY1), (circuitX2, circuitY1)), # segment supérieur
           ((circuitX1, circuitY1), (circuitX1, circuitY2))] # segment gauche
    return lst


def on_circuit_player(x: int, y: int):
    """Renvoie True si les coordonnées du joueur se trouvent sur le circuit, False sinon"""
    test_x, test_y = dep_player(direction, x, y)
    for i in liste_points:
        xA, yA, xB, yB = i[0][0], i[0][1], i[1][0], i[1][1]
        if ((xA == xB == test_x and yA <= test_y <= yB) or (xA == xB == test_x and yB <= test_y <= yA)) or ((yA == yB == test_y and xA <= test_x <= xB) or (yA == yB == test_y and xB <= test_x <= xA)):
            return True
    return False

def on_circuit_player2(x: int, y: int):
    """Renvoie True si les coordonnées du joueur se trouvent sur le circuit, False sinon"""
    test_x, test_y = dep_player2(direction2, x, y)
    for i in liste_points:
        xA, yA, xB, yB = i[0][0], i[0][1], i[1][0], i[1][1]
        if ((xA == xB == test_x and yA <= test_y <= yB) or (xA == xB == test_x and yB <= test_y <= yA)) or ((yA == yB == test_y and xA <= test_x <= xB) or (yA == yB == test_y and xB <= test_x <= xA)):
            return True
    return False

def on_circuit_sparx(dir_sparx: str, x: int, y: int, num_sparx: int):
    """Renvoie True si les coordonnées du sparx se trouvent sur le circuit, False sinon"""
    test_x, test_y = dep_sparx(dir_sparx, x, y, num_sparx)
    for i in liste_points:
        xA, yA, xB, yB = i[0][0], i[0][1], i[1][0], i[1][1]
        if ((xA == xB == test_x and yA <= test_y <= yB) or (xA == xB == test_x and yB <= test_y <= yA)) or ((yA == yB == test_y and xA <= test_x <= xB) or (yA == yB == test_y and xB <= test_x <= xA)):
            return True
    return False


def segments_par_coords() -> list[tuple]:
    """Renvoie une liste de segment en fonction des coins que le joueur à dessiné"""
    liste_total = []
    for i in range(len(coords_poly) -1):
        segment = (tuple(coords_poly[i]), tuple(coords_poly[i+1]))
        liste_total.append(segment)
    return liste_total


def coin_manquant(coords_poly: list):
    """Renvoie le coin manquant du polygone (seulement les 4 coins du circuit)"""
    x_debut, y_debut = coords_poly[0]
    x_fin, y_fin = coords_poly[-1]
    if (x_fin == circuitX2 and y_debut == circuitY2) or (x_debut == circuitX2 and y_fin == circuitY2):       # coin inférieur droit
        coords_poly.append((circuitX2, circuitY2))
    elif (x_fin == circuitX1 and y_debut == circuitY2) or (x_debut == circuitX1 and y_fin == circuitY2):     # coin inférieur gauche
        coords_poly.append((circuitX1, circuitY2))
    if (x_fin == circuitX1 and y_debut == circuitY1) or (x_debut == circuitX1 and y_fin == circuitY1):      # coin supérieur gauche
        coords_poly.append((circuitX1, circuitY1))
    elif (x_fin == circuitX2 and y_debut == circuitY1) or (x_debut == circuitX2 and y_fin == circuitY1):       # coin supérieur droit
        coords_poly.append((circuitX2, circuitY1))
    else:
        pass


def dessin_ligne(x, y):
    """Dessine une ligne avec ses coordonnées et celles futures"""
    test_x, test_y = dep_player(direction, x, y)
    ligne(x, y, test_x, test_y, 'white', tag='ligne')

def dessin_ligne2(x, y):
    """Dessine une ligne avec ses coordonnées et celles futures"""
    test_x, test_y = dep_player(direction2, x, y)
    ligne(x, y, test_x, test_y, 'white', tag='ligne2')

def reset():
    """Réinitialise toutes les variables de départ"""
    global x_qix, y_qix, x_qix2, y_qix2, x_player, y_player, x1_sparx, y1_sparx, x2_sparx, y2_sparx, x3_sparx, y3_sparx, touche_entree, touche_espace, speed_player, dir_sparx1, dir_sparx2, dir_sparx3, direction, invincible,touche_entree2,touche_espace2,speed_player2,x_player2,y_player2,direction2
    touche_entree = 0 
    touche_espace = 0   # permet de remettre la vitesse initiale du joueur
    touche_entree2 = 0 
    touche_espace2 = 0  
    speed_player = 5
    speed_player2 = 5
    invincible = False
    x_qix = 300
    y_qix = 300
    x_qix2 = 200
    y_qix2 = 200
    x_player = dim_fenetre // 2
    y_player = dim_fenetre - esp_circuit
    x_player2 =  dim_fenetre - esp_circuit
    y_player2 =  dim_fenetre // 2
    direction = None
    direction2 = None
    x1_sparx = dim_fenetre // 2     # abscisse du sparx 1
    y1_sparx = circuitY1    # ordonnée du sparx 1
    x2_sparx = x1_sparx     
    y2_sparx = y1_sparx
    x3_sparx = circuitX1     
    y3_sparx = circuitY1
    dir_sparx1 = 'droite'
    dir_sparx2 = 'gauche'
    dir_sparx3 = dir_sparx1
    efface('ligne')
    efface('ligne2')

##### Collisions #####

def collision_qix_player(x_qix: int, y_qix: int, x_player: int, y_player: int):
    """True si le qix est en collision avec le joueur, False sinon"""
    distance = sqrt((x_qix - x_player) ** 2 + (y_qix - y_player) ** 2)
    return distance < player_size


def intersection_ligne_qix(x_qix, y_qix, coords_ligne):
    """True si le Qix touche la ligne de dessin du joueur, False sinon"""
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
    """True si le sparx est en collision avec le joueur, False sinon"""
    if sqrt((x_sparx - x_player) ** 2 + (y_sparx - y_player) ** 2)<= player_size:
        return True
    return False


def collision_obstacles(lst_osbtacles, x_player, y_player):
    """True si le joueur est en collision avec un obstacle, False sinon"""
    for i in lst_osbtacles:
        if sqrt((i[0] - x_player) ** 2 + (i[1] - y_player) ** 2)<= player_size:
            return True
    return False


def collision_joueur_pomme():
    """Renvoie si le joueur est invincible et le temps restant lorsqu'il mange une pomme"""
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
    """Renvoie un point `(x, y)` appartenant à un segment donné"""
    x1, y1 = segment[0]
    x2, y2 = segment[1]
    x = uniform(min(x1, x2), max(x1, x2))
    y = uniform(min(y1, y2), max(y1, y2))
    return (x, y)


def segment_random(liste_points):
    """Renvoi un point `(x, y)` aléatoire appartenant au circuit entier"""
    if not liste_points:
        return None
    segment_choisi = choice(liste_points)
    return point_random_on_segment(segment_choisi)


def spawn_obstacle():
    """Affiche et retourne les coordonnées `(x, y)` d'un obstacle appartenant à la liste de points"""
    x, y = segment_random(liste_points)
    init_obstacle(x, y, nb_obstacles)
    return x, y




if __name__ == "__main__":
    choix_jeu = main()
    ready()
    init_game(choix_jeu)

    liste_points = segments_initiaux()      # liste des segments du circuit
    coords_poly = []        # liste des coordonnées du futur polygone à dessiner
    liste_osbtacles = []        # liste des coordonnées des osbtacles

    temps = 0
    touche_entree = 0       # touche qui permet le dessin
    touche_espace = 0       # touche qui permet l'accélération du joueur

    coords_poly2 = []
    touche_entree2 = 0       # touche qui permet le dessin
    touche_espace2 = 0       # touche qui permet l'accélération du joueur

    while True:
        old_direction = direction   # enregistre l'ancienne direction avant MAJ
        old_direction2 = direction2   # enregistre l'ancienne direction avant MAJ
        direction, direction2 = mise_a_jour_direction(direction,direction2)

        
        if direction == 'echap':
            ferme_fenetre()
            break
        #### Déplacement du joueur ####
        if temps % speed_player == 0 and touche_entree == 0 and on_circuit_player(x_player, y_player):     # si joueur sur circuit, le faire déplacer
            x_player, y_player = dep_player(direction, x_player, y_player)
        if choix_jeu=="Versus":
            if temps % speed_player2 == 0 and touche_entree2 == 0 and on_circuit_player2(x_player2, y_player2):     # si joueur sur circuit, le faire déplacer
                x_player2, y_player2 = dep_player2(direction2, x_player2, y_player2)
    
        #### Déplacement des sparx ####
        if temps % 5 == 0 and (on_circuit_sparx(dir_sparx1, x1_sparx, y1_sparx, 1) or on_circuit_sparx(dir_sparx2, x2_sparx, y2_sparx, 2)):      # si les sparxs sont sur le circuit, les faires se déplacer
            
            dir_sparx1 = turn_sparx(dir_sparx1, x1_sparx, y1_sparx, 1)
            dir_sparx2 = turn_sparx(dir_sparx2, x2_sparx, y2_sparx, 2)
            
            x1_sparx, y1_sparx = dep_sparx(dir_sparx1, x1_sparx, y1_sparx, 1)
            x2_sparx, y2_sparx = dep_sparx(dir_sparx2, x2_sparx, y2_sparx, 2)

            if choix_jeu == 'Difficile':
                dir_sparx3 = turn_sparx(dir_sparx3, x3_sparx, y3_sparx, 3)
                x3_sparx, y3_sparx = dep_sparx(dir_sparx3, x3_sparx, y3_sparx, 3)
            
        elif temps % 5 == 0:
            x1_sparx, y1_sparx = dim_fenetre // 2, circuitY1
            x2_sparx, y2_sparx = x1_sparx, y1_sparx
            dir_sparx1 = 'droite'
            dir_sparx2 = 'gauche'
        init_sparx()    # affiche les sparxs après leur déplacement 


        #### Déplacement du qix ####
        x_qix, y_qix = dep_qix(x_qix, y_qix, 1)
        init_qix()

        if choix_jeu == 'Difficile':
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

                ### fonction sur les coins
                coin_manquant(coords_poly)


                if touche_espace == 0:
                    polygone(coords_poly, 'white', 'green', tag='polygone')
                else:
                    polygone(coords_poly, 'white', 'blue', tag='polygone')
                liste_points.extend(segments_par_coords())
                coords_poly = []

                efface('ligne')     # évite d'avoir les lignes dessinés en plus des lignes du polygone (qui sont les mêmes)
                touche_entree = 0   # permet de ressortir de la boucle 'entrée'
                touche_espace = 0   # permet de remettre la vitesse initiale du joueur
                speed_player = 5
            else:
                dessin_ligne(x_player, y_player)
                x_player, y_player = dep_player(direction, x_player, y_player)

        if choix_jeu=="Versus":       
            if direction2 == 'entree':
                touche_entree2 = 1

            if touche_entree2 == 1 and old_direction2 != direction2:   # si changement de direction pendant le dessin
                coords_poly2.append(tuple((x_player2, y_player2)))

            if temps % speed_player2 == 0 and touche_entree2 == 1:   # si touche entrée pressée, le joueur se déplace dans l'air complète
            
                if direction2 == 'espace' and touche_espace2 == 0:
                    speed_player2 //= 2
                    touche_espace2 = 1

                if on_circuit_player2(x_player2, y_player2):   # si joueur revient sur circuit, dessin du polygone et ajout des lignes au circuit
                    x_player2, y_player2 = dep_player2(direction2, x_player2, y_player2)

                    coords_poly2.append(tuple((x_player2, y_player2)))

                    ### fonction sur les coins
                    coin_manquant(coords_poly2)


                    if touche_espace2 == 0:
                        polygone(coords_poly2, 'white', 'white', tag='polygone')
                    else:
                        polygone(coords_poly2, 'white', 'orange', tag='polygone')
                    liste_points.extend(segments_par_coords())
                    coords_poly2 = []

                    efface('ligne2')     # évite d'avoir les lignes dessinés en plus des lignes du polygone (qui sont les mêmes)
                    touche_entree2 = 0   # permet de ressortir de la boucle 'entrée'
                    touche_espace2 = 0   # permet de remettre la vitesse initiale du joueur
                    speed_player2 = 5
                else:
                    dessin_ligne2(x_player2, y_player2)
                    x_player2, y_player2 = dep_player2(direction2, x_player2, y_player2)
        

        #### Collisions ####
        collision_joueur_pomme()
        
        if invincible:
            init_text_invincible()
            temps_actuel = time()
            temps_ecoule_invincible = temps_actuel - temps_invincible

            if temps_ecoule_invincible >= duree_invincibilite:
                invincible = False
        else:
            efface('Invincible')
            if collision_qix_player(x_qix, y_qix, x_player, y_player) or \
                intersection_ligne_qix(x_qix, y_qix, coords_poly) or \
                collision_qix_player(x_qix2, y_qix2, x_player, y_player) or \
                intersection_ligne_qix(x_qix2, y_qix2, coords_poly) or \
                collision_sparx(x1_sparx, y1_sparx, x_player, y_player) or \
                collision_sparx(x2_sparx, y2_sparx, x_player, y_player) or \
                collision_sparx(x3_sparx, y3_sparx, x_player, y_player): 
                life_player -= 1
                coords_poly = []
                reset()
                efface('life')
                init_life(life_player)

            if choix_jeu=='Versus':
                if collision_qix_player(x_qix, y_qix, x_player2, y_player2) or \
                    intersection_ligne_qix(x_qix, y_qix, coords_poly2) or \
                    collision_qix_player(x_qix2, y_qix2, x_player2, y_player2) or \
                    intersection_ligne_qix(x_qix2, y_qix2, coords_poly2) or \
                    collision_sparx(x1_sparx, y1_sparx, x_player2, y_player2) or \
                    collision_sparx(x2_sparx, y2_sparx, x_player2, y_player2):
                    life_player2 -= 1
                    coords_poly2 = []
                    reset()
                    efface('life2')
                    init_life2(life_player2)

            elif collision_obstacles(liste_osbtacles, x_player, y_player):
                direction = None


        ##### Obstacles #####
        if life_player == 2 and nb_obstacles == 0:
            liste_osbtacles.append(spawn_obstacle())
            nb_obstacles += 1
        if life_player == 1 and nb_obstacles == 1:
            liste_osbtacles.append(spawn_obstacle())
            nb_obstacles += 1

        if choix_jeu=="Basique"or choix_jeu=="Difficile":
            if life_player == 0:
                init_gameover()
                break
        if choix_jeu=="Versus":
            if life_player==0:
                init_joueur1perdu()
                break
            if life_player2==0:
                init_joueur2perdu()
                break

        temps = temps + 1
        mise_a_jour()


    attend_ev()
    ferme_fenetre()