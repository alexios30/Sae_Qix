from random import *
from fltk import *
from math import *

def segments_initiaux(
        x1: float,
        x2: float,
        y1: float,
        y2: float,
) -> list:
    """
    Regroupe dans une liste les segments du circuit avant dessins du joueur.

    :param float x1: abscisse du coin supérieur gauche du circuit
    :param float x2: abscisse du coin supérieur droit du circuit
    :param float y1: ordonnée du coin supérieur gauche du circuit
    :param float y2: ordonnée du coin inférieur gauche du circuit
    :return: liste contenant les segments du circuit sous forme ``((x1, y1),(x2,y2))``
    """

    liste_total = []
    # Segment inférieur
    lst = (x1, y2),(x2, y2)
    liste_total.append(lst)
    # Segment droit
    lst = (x2, y1),(x2, y2)
    liste_total.append(lst)
    # Segment supérieur
    lst = (x1, y1),(x2, y1)
    liste_total.append(lst)
    # Segment gauche
    lst = (x1, y1),(x1, y2)
    liste_total.append(lst)
    return liste_total


def segment_par_coordonnee(
        lst: list[list]
) -> list:
    """
    Regroupe les coordonnées des changements d'orientation pour en faire des tuples de segments.

    :param list lst: liste des coordonnées de changement de direction
    :return: liste de tuples ``((x1, y1),(x2,y2))`` pour en faire des segments
    """

    liste_total = []
    for i in range(len(lst) -1):
        segment = (tuple(lst[i]), tuple(lst[i+1]))
        liste_total.append(segment)
    return liste_total


def point_dans_segment(
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        px: float,
        py: float,
) -> bool:
    """
    Vérifie si le point ``(px,py)`` appartient aux segments ``((x1,y1),(x2,y2))``.

    :param float x1: abscisse du début du segment
    :param float y1: ordonnée du début du segment
    :param float x2: abscisse de fin du segment
    :param float y2: ordonnée de fin du segment
    :param float px: abscisse du point à vérifier
    :param float py: ordonnée du point à vérifier
    :return: True si le point appartient au segment - False sinon
    """

    if x1 == x2 and x1 == px:
        # Le point est sur le segment vertical
        return y1 <= py <= y2 or y2 <= py <= y1
    elif x1 == x2:
        # Le segment est vertical, mais le point n'est pas sur le même x
        return False
    else:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        y_expected = m * px + b
        return y_expected == py and min(x1, x2) <= px <= max(x1, x2)


def orientation_dep(
        orientation: float,
        dep: float,
        ecart: float,
        lFenetre: float,
        hFenetre: float,
        circuitY1: float,
        x_perso: float,
        y_perso: float,
) -> float:
    """
    Par rapport à l'orientation donné, oriente le déplacement du personnage avec ses coordonnées. 

    :param float orientation: orientation souhaité du personnage
    :param float dep: distance de déplacement
    :param float ecart: espace entre circuit et fenetre
    :param float lFenetre: largeur de la fenetre
    :param float hFenetre: hauteur de la fenetre
    :param float circuitY1: ordonnée du coin supérieur gauche du circuit
    :param float x_joueur: abscisse du personnage
    :param float y_joueur: ordonnée du personnage
    :return: Déplacement finale ``(dxj, dyj)``
    """
    dx = 0
    dy = 0

    if orientation == 180:
        dx = max(-dep, -(x_perso - ecart))
        dy = 0
    elif orientation == 0:
        dx = min(dep, lFenetre - x_perso - ecart)
        dy = 0
    elif orientation == 270:
        dx = 0
        dy = min(dep, hFenetre - y_perso - ecart)
    elif orientation == 90:
        dx = 0
        dy = max(-dep, -(y_perso - circuitY1))
    return dx, dy


def orientation_dispo(
        orientation: float,
) -> list:
    """
    Permet de renvoyer les orientations en excluant le demi-tour.

    :param float orientation: orientation du sparx

    :return: Liste d'orientations.
    """
    
    orientations = [orientation]
    
    if orientation == 0:
        orientations.extend([90, 270])
    elif orientation == 90:
        orientations.extend([0, 180])
    elif orientation == 180:
        orientations.extend([90, 270])
    elif orientation == 270:
        orientations.extend([0, 180])

    return orientations


def deplacement_qix(
        x_qix: float, 
        y_qix: float, 
        vitesse_qix: float, 
        circuitX1: float, 
        circuitX2: float, 
        circuitY1: float, 
        circuitY2: float, 
        milieu_qix: float,
) -> tuple[int, int]:

    """
    Effectue un déplacement aléatoire du Qix en tenant compte des limites du circuit.
    :param x_qix: Coordonnée x du Qix.
    :param y_qix: Coordonnée y du Qix.
    :param vitesse_qix: Vitesse de déplacement du Qix.
    :param circuitX1: Limite gauche du circuit.
    :param circuitX2: Limite droite du circuit.
    :param circuitY1: Limite supérieure du circuit.
    :param circuitY2: Limite inférieure du circuit.
    :param milieu_qix: Taille du milieu du Qix pour éviter de dépasser les limites.
    :param facteur: Facteur de multiplication pour augmenter la plage de déplacement aléatoire.
    :return: Nouvelles coordonnées du Qix (x_qix, y_qix).
    """
    facteur = 2.0
    plage_deplacement = vitesse_qix  * facteur

    if y_qix <= circuitY1 + milieu_qix:
        x_qix = randint(x_qix - plage_deplacement, x_qix + plage_deplacement)
        y_qix = randint(y_qix, y_qix + plage_deplacement)

    if y_qix >= circuitY2 - milieu_qix:
        x_qix = randint(x_qix - plage_deplacement, x_qix + plage_deplacement)
        y_qix = randint(y_qix - plage_deplacement, y_qix)

    if x_qix <= circuitX1 + milieu_qix:
        x_qix = randint(x_qix, x_qix + plage_deplacement)
        y_qix = randint(y_qix - plage_deplacement, y_qix + plage_deplacement)

    if x_qix >= circuitX2 - milieu_qix:
        x_qix = randint(x_qix - plage_deplacement, x_qix)
        y_qix = randint(y_qix - plage_deplacement, y_qix + plage_deplacement)

    else:
        x_qix = randint(x_qix - plage_deplacement, x_qix + plage_deplacement)
        y_qix = randint(y_qix - plage_deplacement, y_qix + plage_deplacement)
    return x_qix, y_qix


def qix(
        x_qix: float,
        y_qix: float,
)-> float:
    """
    Cela prends les coordonnés du qix et renvoie l'image du qix avec ses nouvelle coordonnées
    :param float x_qix= Où se situe les coordonnés en x du qix
    :param float y_qix= Où se situe les coordonnés en y du qix
    """
    
    image(x_qix,y_qix,'kong.png',largeur=60,hauteur=60,ancrage="center",tag='kong')
    return image


def distance(x1, y1, x2, y2):
    """
    Calcul la distance entre 2 point
    :param float x1 = Où se situe les coordonnés en x du premier point
    :param float y1 = Où se situe les coordonnés en y du premier point
    :param float x2 = Où se situe les coordonnés en x du deuxième point
    :param float y2 = Où se situe les coordonnés en y du deuxième point
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def collision_qix(
        x_qix:float,
        y_qix:float,
        joueurX:float, 
        joueurY:float,
        tailleJoueur:float,
)->float:
    """
    Calcule la distance du qix et du joueur et renvoye si ils sont touchés
    :param float x_qix= Où se situe les coordonnés en x du qix
    :param float y_qix= Où se situe les coordonnés en y du qix
    :param float joueurX= Où se situe les coordonnés en x du joueur
    :param float joueurY= Où se situe les coordonnés en y du joueur
    :param float tailleJoueur=la taille du joueur
    """
    dist = distance(x_qix, y_qix, joueurX, joueurY)
    return dist <= tailleJoueur


def nombre_vie(
        vie_joueur:float,
)->float:
    """
    Prend en compte la vie du joueur et modifie l'écriture sur le jeux et si la vie est a 0, affiche Game over
    :param vie_float=nombre de vie du joueur
    """
    if vie_joueur==2:
        chaineQix= '2'
        tailleQix = 15
        policeQix ="Courier"
        texte(570,30,chaineQix,police=policeQix,taille=tailleQix,couleur="red",ancrage="center",tag="vie")
    if vie_joueur==1:
        chaineQix= '1'
        tailleQix = 15
        policeQix ="Courier"
        texte(570,30,chaineQix,police=policeQix,taille=tailleQix,couleur="red",ancrage="center",tag="vie")
    if vie_joueur==0:
        chaineQix= '0'
        tailleQix = 15
        policeQix ="Courier"
        texte(570,30,chaineQix,police=policeQix,taille=tailleQix,couleur="red",ancrage="center",tag="vie")
        chaineQix= 'GAME OVER'
        tailleQix = 50
        policeQix ="STENCIL"
        texte(300,300,chaineQix,police=policeQix,taille=tailleQix,couleur="purple",ancrage="center",tag="game over")
        return True
    return False


def intersection_lignes_presentes(
        lignes: list,
) -> bool:
    """
    Vérifie si les lignes que dessine le joueur s'intersectent.

    :param list lignes: liste des lignes de dessins actuel
    :return: True s'il y a une intersection, False sinon

    """

    for i in range(len(lignes) - 1):
        ligne1 = lignes[i]
        for j in range(i + 1, len(lignes)):
            ligne2 = lignes[j]

            x1, y1 = ligne1[0]
            x2, y2 = ligne1[1]
            x3, y3 = ligne2[0]
            x4, y4 = ligne2[1]

            det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

            if det == 0:
                continue

            intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det
            intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det

            if min(x1, x2) <= intersection_x <= max(x1, x2) and min(y1, y2) <= intersection_y <= max(y1, y2) and min(x3, x4) <= intersection_x <= max(x3, x4) and min(y3, y4) <= intersection_y <= max(y3, y4):
                return True

    return False


def intersection_qix(
        lignes: list, 
        x_qix: float, 
        y_qix: float, 
        taille_qix: float,
) -> bool:
    """
    Vérifie si les lignes que dessine le joueur s'intersectent avec le Qix.

    :param list lignes: liste des lignes de dessins actuelles
    :param float x_qix: abscisse du Qix
    :param float y_qix: ordonnée du Qix
    :param float taille_qix: taille du Qix
    :return: True s'il y a une intersection, False sinon
    """

    for ligne in lignes:
        (x1, y1), (x2, y2) = ligne
        # Calculer la distance entre le centre du Qix et le segment de ligne
        denominateur = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if denominateur == 0:
            continue
        distance = ((x2 - x1) * (y1 - y_qix) - (x1 - x_qix) * (y2 - y1)) / denominateur
        if abs(distance) <= taille_qix / 2:
            # Calculer la distance entre le centre du Qix et les extrémités du segment
            distance1 = sqrt((x1 - x_qix) ** 2 + (y1 - y_qix) ** 2)
            distance2 = sqrt((x2 - x_qix) ** 2 + (y2 - y_qix) ** 2)
            if distance1 <= taille_qix / 2 or distance2 <= taille_qix / 2:
                return True
            # Vérifier si le centre du Qix se trouve sur la ligne
            if (min(x1, x2) <= x_qix <= max(x1, x2)) and (min(y1, y2) <= y_qix <= max(y1, y2)):
                return True

    return False


def point_au_milieu(
        segment: list,
) -> tuple[float, float]:
    """
    Choisi un point au hasard dans un segment.

    :param list segment: coordonnées du début et fin du segment

    :return: Points aléatoires ``(x, y)`` appartenant au segment
    """

    x1, y1 = segment[0]
    x2, y2 = segment[1]

    x = uniform(min(x1, x2), max(x1, x2))
    y = uniform(min(y1, y2), max(y1, y2))

    return (x, y)


def point_au_milieu_aleatoire(
        liste_segments: list,
) -> tuple[float, float]:
    """
    Choisi un segment aléatoire dans la liste donnée

    :param list liste_segments: liste des segments totaux

    :return: Points aléatoires ``(x, y)`` appartenant au segment
    """

    if not liste_segments:
        return None

    segment_choisi = choice(liste_segments)
    point_choisi = point_au_milieu(segment_choisi)

    return point_choisi
