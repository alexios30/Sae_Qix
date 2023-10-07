from fltk import *


def carre(x, y, cote):
    rectangle(x, y, x + cote, y + cote,
              "red", "red", tag='carre')


cree_fenetre(400, 400)

# dessin initial du carré
cx, cy, taille = 200, 400, 10
carre(cx, cy, taille)

# déplacement en pixels à chaque flèche pressée
dep = 20

while True:
    ev = donne_ev()
    tev = type_ev(ev)

    # déplacement du carré
    dx = 0
    dy = 0
    if tev == 'Quitte':
        break
    if tev == 'Touche':
        nom_touche = touche(ev)
        if nom_touche == 'Left':
            dx = max(-dep, -cx)
        elif nom_touche == 'Right':
            dx = min(dep, 399 - cx - taille)
        elif nom_touche == 'Down':
            dy = min(dep, 399 - cy - taille)
        elif nom_touche == 'Up':
            dy = max(-dep, -cy)
        if dx != 0 or dy != 0:
            efface('carre')
            cx = cx + dx
            cy = cy + dy
            carre(cx, cy, taille)
        elif nom_touche =="Esc":
            ferme_fenetre()
    mise_a_jour()
ferme_fenetre()