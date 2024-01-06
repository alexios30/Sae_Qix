 I. L'organisation du programme

Le code réalisé par Alexis :

    - les adversaires   
    - les collisions entre adversaires/joueur (+ perte de vie, réinitialisation des positions du joueur, sparx,qix)
    - les textes et image affichés pendant le jeu (Qix, vie, image du Qix)
    Update rendu 2: 
    - reprise de toutes les collisions (vie, sparx, qix) à zéro
    - le bonus des pommes + invincibilité
    - la fonction qui réintisalise tout (reset) reprise à zéro
    - le menu et ses fonctionnalités
    - le mode Difficile
   Update rendu 3:
    -Ajout du mode 2 joueur
    -Ajustement du menu pour choisir le mode de Jeu

   

Le code réalisé par Julien : 

    - le design de la fenêtre
    - les déplacements du joueur (les touches pressées, les conditions de déplacements possibles/impossibles)
    - l'intersection de sa propre ligne pendant le dessin 
    - les dessins du joueur*
    Update rendu 2: 
    - refonte de la base du code, reprise à zéro du code avec des fonctions plus courtes, plus claires et plus efficacent 
    - reprise de la vérification de la position du joueur (se base sur les segments par points pour avoir plus de fluidité) : Une reprise à zéro intermédiaire contenait un test de présence de coordonnées dans une liste à rallonge
    - déplacement interne des sparx sur le circuit
    - les obstacles 
    - la vitesse du joueur lors du dessin
    Update rendu 3:
     -Fait la sauvegardes des paramètres dans un fichier txt
     -Fait la fonction pause

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

Update rendu 2:

Après ce premier rendu, nous avons réalisé une remise à zéro du code et se basant sur la création du liste de coordonnées dont le joueur avait le droit d'y accéder. Cependant cette liste devenait rapidement longue et difficile de manipulation.
Nous avons donc effectuer une troisième reprise à zéro du programme, en créant des fonctions courtes et concises et reprenant la manipulation de segments.


IV. Les bonus / Variantes

Nous avons essayé de trouver, sans succès, la condition qui permettait de faire tester les déplacements des sparx dans les direction perpendiculaire à celle actuelle et ainsi donner la possibilité aux sparx de circuler sur les polygones dessinés par le joueur.
À l'inverse, nous avons réussi à implémenter une apparition d'obstacles sur le passage du joueur, de coordonnées aléatoires et ceux pour chaque point de vie perdue. Cependant, la condition manquante se trouve être celle qui teste (en plus de tous les segments) s'il y a sur le passage un obstacle et auquel cas un arrêt se marque du joueur (et même plus car il se retrouve bloqué : nous avons pensé à réinitialiser la variable orientation en None mais le joueur aurait pu repartir dans la même direction par la suite).

Update rendu 2:

- Score (manquant): Les coins n'étant pas parfaitement maîtrisés lors du dessin, nous avons fait le choix de ne pas rajouter une fonction de score qui se trouverait mal calculée.
- Vitesse : Lors du dessin seulement, le joueur peut presser la touche Espace pour lui permettre de se déplacer plus rapidement, au détriment d'une couleur de polygone modifiée pour indiquée une zone dessinée à grand vitesse. Le fonctionnement est semblable à la touche entrée pour dessiné : si la touche Espace est pressée alors sa variable touche_espace vaut 1, et le polygone se voit colorié en bleu, sinon en vert.
- Obstacles : Une fonction prend en paramètre le circuit (tous les segments, y compris les dessins) et retourne un point aléatoire appartenant aux segments du circuit. Ainsi la fonction spawn_obstacle permet d'afficher chaque obstacle.
- Bonus : Une fonction va créer et retourner une liste de coordonnées aléatoires comprises dans l'air du circuit qui définissent les positions des pommes. Si le joueur touche une pomme (si les coordonnées sont équivalentes, soit leur distance très faible) la liste de pommes est modifiée et la pomme se voit donc disparaître en actionnant le mode invincible. Un décompte est lancé et empêche dans le while de rentrer dans le if des collisions. Ce décompte est vérifié et s'il est supérieur à 3 secondes alors la variable invincible devient False et les collisions sont de nouveaux vérifiées.
- Deux joueurs (manquant): Le défis d'avoir deux joueurs repose principalement, et pour nous, sur le fait de jouer avec toutes les varibles initialement prévu que pour un joueur. 
- Sparx "internes" : La condition de test des sparx a été trouvé, ce qui nous a permit d'implémenter le bonus de sparx interne. il s'agit, dans l'ordre, de lister les directions de chaque sparx en excluant le demi-tour, de tester chacune pour savoir s'il se trouvera encore sur le circuit, et dans ce cas lister ces directions possibles puis en faire un tirage aléatoire (choice).
- Niveaux : Nous avons choisis d'instaurer un menu de démarrage par lequel l'utilisateur va pouvoir déterminer le niveau au lancement du jeux : seuls les rectangles sont cliquables, sinon la boucle while ne permettra pas de lancer le jeu tant qu'un clic n'est pas effectué dans un de ces derniers. Soit le jeu basique, qui est le jeu simple, soit difficile, qui rajoute au jeu un deuxième Qix et un troisème sparx sur le circuit. L'optimisation de ces rajouts reste encore à travailler, mais chaque fonction créer peut être utiliser pour n'importe quel enemi tant que le numéro y est attribué.

Update rendu 3:
- 2 joueurs: Nous avons donc reussi à inserer les 2 joueurs en changeant pas mal de nos ancienne fonction pour qu'elle puisse prendre en paramètre un 2 eme joueur.Pour ce qui les collisions , nous avons réutilisé nos anciennes fonctions de collision sur le 2 eme joueur et pour la collision entre les joueurs, nous avons aussi réutilisé la fonction de collision des sparxs.On a eu aussi besoin de modifier le menu pour accueillir ce nouveau mode et bien séparé les différents mode de jeu.

V.Variante

Pour commencer, nous avons commencer par la variante sparx interne car nous avons refait le déplacement des sparxs.Pour effectuer ceci, nous avons donc décidé que les sparxs puisse vérifier à chaque déplacement si ils peuvent faire haut,bas,droite, gauche et que si il y a un polygone déssiné, ils  puissent le choisir comme direction.Après, nous avons récupéré la variante d'obstacle fait dans la précédente version.Nous avons décidé après de faire la variante pomme, elle fonctionne comme cela: si les coordonnées de la pomme sont les mêmes que celle du joueur, la pomme est supprimée et le mode invincible est activé.Comment marche le mode invincible? Une fois la pomme mangé, un décompte commence, puis dans la boucle, nous entrons dans le if de invicible ce qui nous empêche d'entrer dans le if des collisions avec les différents énnemis.Le décompte est donc à chaque fois vérifié et si le décompte est superieurà 3 secondes, le invicible devient false et on vérifie donc à chaque fois les collision.Nous avons fait après la variantes vitesse, ce qui permet donc d'accélérer et de colorier le polygone d'une différente couleur.Pour la variante d'un nouveau mode de difficulté, nous avons eu comme idée de lancer un menu qui nous propose soit le mode de jeu basique, soit le mode de jeu difficile où il y aura donc 2 qix et 3 sparx.Nous avons donc récupérer les coordonées du clic gauche et voir si sa position était entre les réctangles de qix basique et du qix difficile, puis en fonction du mode choisie, lancé le jeux avec un ou deux qix et 2 ou 3 sparx.


