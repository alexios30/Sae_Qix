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


def directions_libres(
        x: float, 
        y: float,
        segments: list,
) -> list:
    """
    Définit les 2 directions perpendiculaires au segments actuel.

    :param float x: abscisse du point
    :param float y: ordonnée du point
    :param list segments: liste des segments à vérifier (segments totaux)
    :return: list de 2 directions
    """

    # À partir de la position (x, y), déterminez les directions où il n'y a pas de segments

    directions = []  # Stockez les directions libres ici

    # Vérifiez si le joueur peut se déplacer vers le haut
    if all(not point_dans_segment(x1, y1, x2, y2, x, y - 1) for (x1, y1), (x2, y2) in segments):
        directions.append(90)

    # Vérifiez si le joueur peut se déplacer vers le bas
    if all(not point_dans_segment(x1, y1, x2, y2, x, y + 1) for (x1, y1), (x2, y2) in segments):
        directions.append(270)

    # Vérifiez si le joueur peut se déplacer vers la gauche
    if all(not point_dans_segment(x1, y1, x2, y2, x - 1, y) for (x1, y1), (x2, y2) in segments):
        directions.append(180)

    # Vérifiez si le joueur peut se déplacer vers la droite
    if all(not point_dans_segment(x1, y1, x2, y2, x + 1, y) for (x1, y1), (x2, y2) in segments):
        directions.append(0)

    return directions


def orientation_dep(
        orientation: float,
        dep: float,
        ecart: float,
        lFenetre: float,
        hFenetre: float,
        circuitY1: float,
        x_joueur: float,
        y_joueur : float,
        dx: float,
        dy: float,
) -> float:
    """
    Par rapport à l'orientation donné, oriente le déplacement du joueur avec ses coordonnées. 

    :param float orientation: orientation souhaité du joueur
    :param float dep: distance de déplacement
    :param float ecart: espace entre circuit et fenetre
    :param float lFenetre: largeur de la fenetre
    :param float hFenetre: hauteur de la fenetre
    :param float circuitY1: ordonnée du coin supérieur gauche du circuit
    :param float x_joueur: abscisse du joueur
    :param float y_joueur: ordonnée du joueur
    :param float dx: déplacement en abscisse dans la direction finale
    :param float dy: déplacement en ordonnée dans la direction finale
    :return: Déplacement finale ``(dx, dy)``
    """

    if orientation == 180:
        dx = max(-dep, -(x_joueur - ecart))
        dy = 0
    elif orientation == 0:
        dx = min(dep, lFenetre - x_joueur - ecart)
        dy = 0
    elif orientation == 270:
        dx = 0
        dy = min(dep, hFenetre - y_joueur - ecart)
    elif orientation == 90:
        dx = 0
        dy = max(-dep, -(y_joueur - circuitY1))

    return dx, dy
