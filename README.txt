I. L'organisation du programme

Le code réalisé par Alexis :

    - les adversaires   
    - les collisions entre adversaires/joueur(+ perte de vie,réinitialisation des positions du joueur,sparx,qix)
    - les textes et image affichés pendant le jeu (Qix, vie, image du Qix)
Update rendu 2: 
    -Refait toutes les collisions(vie,sparx,qix)
    -Fait le bonus de pomme+ Invincible
    -Refait la fonction qui reintisalise tout
    -Le Menu
    -Le mode Difficile

Le code réalisé par Julien : 

    - le design de la fenêtre
    - les déplacements du joueur (les touches pressées, les conditions de déplacements possibles/impossibles)
    - l'intersection de sa propre ligne pendant le dessin 
    - les dessins du joueur*
Update rendu 2: 
    -Refait le déplacment du joueur(pour avoir plus de fluidité)
    -Fait le bonus sparx interne
    -Fait le bonus obstacle
    -Fait le bonus vitesse

II. Les choix techniques

Nous avons décidés lors de la réalisation de ce projet de se répartir d'abords les tâches de façon équitable.

Concernant les idées de conceptions, le choix de tester chaque segment dessiné pour anticiper les déplacements était naturel selon nous.
Une écriture soignée des fonctions nous permettaient de bien se comprendre ainsi que de bien comprendre le code, et ceux chacun de son côté.
Un bon nombre de commentaires permet aussi de clarifier les différentes parties du code.

III. Les problèmes rencontrés

Sur le plan des déplacements du joueur, nous avons principalement bloqué un peu de temps sur la touche 'entrée'. Nous voulons bien faire, et c'est pourquoi nous souhaitions que le joueur n'aurait pu sortir du circuit seulement si la touche 'entrée' était pressée.
Nous voulions aussi que les déplacements soient autonomes, c'est-à-dire qu'il suffit d'appuyer une fois sur une flèche pour permettre le déplacement du joueur sans y rester appuyé.
Un second problème est apparu lors des déplacements du joueur : le déplacement du joueur sacade visuellement. Nous pensons que nos test prennent peut-être beaucoup de temps lors d'une réalisation du while, ou encore qu'une boucle de test regroupe trop d'informations (boucle for qui teste pour chaque segment du circuit), mais nous n'avons pas trouvé d'optimisation du code plus poussée que celle du premier rendu.

Pour la partie du Qix, nous voulions reproduire exacement le même qix que dans le vrai jeu avec l'animation et la supression retardée des lignes, mais il nous a manqué la méthode de supression, nous ne l'avons donc pas fait pour nous concentrer sur le jeu Qix en globalité plutôt que sur le design de l'ennemi. Nous allons peut-être reprendre cette idéé pour les rendus futurs. 

IV. Les bonus

Nous avons essayé de trouver, sans succès, la condition qui permettait de faire tester les déplacements des sparx dans les direction perpendiculaire à celle actuelle et ainsi donner la possibilité aux sparx de circuler sur les polygones dessinés par le joueur.
À l'inverse, nous avons réussi à implémenter une apparition d'obstacles sur le passage du joueur, de coordonnées aléatoires et ceux pour chaque point de vie perdu. Cependant, la condition manquante se trouve être celle qui teste (en plus de tous les segments) s'il y a sur le passage un osbtacle et auquel cas un arrêt se marque du joueur (et même plus car il se retrouve bloqué : nous avons pensé à réinitialiser la variable orientation en None mais le joueur aurait pu repartir dans la même direction par la suite).

Second Rendu:

Pour ce deuxième rendu, nous avons décidé de recommencer à 0 les déplacements du joueur car nous avons beaucoup trop de latence dans notre jeu ce qui le rendait pas très amusant.Nous avons donc réussi à mieux optimiser le déplacement du joueur pour le rendre beaucoup plus fluide et plus agréable à jouer.Nous avons aussi décidé de revoir les déplacments du Qix, qui lui aussi rendait le jeu pas fluide.Nous sommes donc repartit de quasi rien et avons tout refait.

V.Variante

Pour commencer, nous avons commencer par la variante sparx interne car nous avons refait le déplacement des sparxs.Pour effectuer ceci, nous avons donc décidé que les sparxs puisse vérifier à chaque déplacement si ils peuvent faire haut,bas,droite, gauche et que si il y a un polygone déssiné, ils  puissent le choisir comme direction.Après, nous avons récupéré la variante sparx 
