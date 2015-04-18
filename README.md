# TP3
IFT-1004 – Introduction à la programmation - Travail Pratique 3

1 Objectifs
Ce travail vous permettra de vous familiariser davantage avec le développement d’applications d’envergure,
via la réutilisation de votre code ou celui d’une autre personne en utilisant le paradigme orienté objet, la
création d’interfaces graphiques et la gestion des exceptions. Malgré qu’une bonne partie de la modélisation
soit déjà faite pour vous, via les modules déjà fournis avec cet énoncé, le reste de la modélisation de votre
programme est libre. Vous pouvez donc créer de nouvelles classes, méthodes, attributs ou modules, ainsi que
modifier les éléments déjà existants.

 Consignes à lire attentivement
 La modélisation que nous vous fournissons tient pour acquis que vous compreniez bien le principe de
l’orienté objet. Souvent une méthode peut être programmée en trois ou quatre lignes lorsqu’on
réutilise les méthodes déjà programmées préalablement.
 Nous vous demandons de travailler en équipe, car c’est un objectif de votre formation académique, et
vous pourrez ainsi vous partager la charge de travail. Chaque coéquipier doit contribuer à parts égales
au développement de ce travail. Laisser son coéquipier faire tout le travail (peu importe les raisons)
est inacceptable: vous passerez à côté des objectifs de ce cours. De la même manière, il ne faut pas
non plus trop en faire. Nous vous conseillons d’utiliser des technologies permettant de partager votre
code avec votre coéquipier comme par exemple SVN ou Git. Vous pouvez d’ailleurs demander un
compte gratuit sur pixel dans la section Applications + Logiciels.
 Un programme Python qui ne s'exécute pas (erreurs de syntaxe ou programme qui plante à
l'exécution) pourrait recevoir une note de 0. Il n'est pas acceptable de remettre un programme que
vous n'avez pas convenablement testé.
 Vous devez commenter vos scripts dans chaque endroit où une explication ou précision est requise.
 Toute communication entre équipes ou avec toute autre personne autre que l’enseignant est
strictement interdite.
 Vous n'êtes pas évalués sur la rapidité d'exécution de votre code. La qualité du code (incluant la
clarté) prime sur la rapidité.
 Les politiques sur le plagiat et le retard énoncées dans le plan de cours sont totalement applicables.
 Il est à noter que 15 points sont donnés pour le respect et la qualité des biens livrables ainsi que pour
la structure générale du programme.

3 Travail à faire
Nous vous demandons dans ce travail pratique de réutiliser le code produit dans le TP2 afin de programmer
le jeu Ultimate Tic-Tac-Toe qui une variante intéressante du jeu classique Tic-Tac-Toe. Si vous ne connaissez
pas ce jeu, vous pouvez l’essayer par exemple ici ou ici. Voici les spécifications du programme que nous
vous demandons d’exécuter en utilisant l’environnement de développement PyCharm et en respectant bien
sûr les normes de programmation vues dans le cours :
Vous devez améliorer une interface graphique permettant de jouer au jeu Ultimate Tic-Tac-Toe, en utilisant
la librairie tkinter. Le code fourni avec cet énoncé vous permet de créer l’interface minimaliste suivante en
utilisant entre autres une solution partielle du TP2 :

Évidemment, cette interface ne permet pas encore de jouer correctement au jeu Utlimate Tic-Tac-Toe. Vous
devez donc ajouter des fonctionnalités afin de respecter premièrement les règles du jeu, mais aussi pour
améliorer éventuellement la convivialité de cette interface. Pour ce faire, un sous ensemble des points est
accordé à des fonctionnalités obligatoires, et le reste des points sera accordé en fonction des fonctionnalités
supplémentaires que vous aurez choisies.
Les prochaines sous-sections donnent la liste des fonctionnalités obligatoires ainsi que la liste des
fonctionnalités facultatives dont vous devez normalement choisir au moins quelques-unes.


3

3.1 Fonctionnalités obligatoires
Ces fonctionnalités doivent être présentes dans le programme que vous remettrez. Les points perdus ici ne
peuvent pas être récupérés en accumulant des fonctionnalités facultatives.
Fonctionnalité obligatoire Pondération
1. L’utilisateur peut choisir entre jouer avec l’ordinateur ou jouer avec une autre personne
(i.e. vous pouvez utiliser par exemple des radiobouttons ou un Combobox).

5 points

2. L’utilisateur peut entrer son nom ainsi le nom de son adversaire si ce dernier est une
personne (i.e. vous pouvez utiliser par exemple des Entries).

5 points

3. L’utilisateur peut choisir son pion (vous pouvez utiliser par exemple des radiobouttons
ou un Combobox).

5 points

4. Le tour des joueurs est alterné correctement en affichant le nom du joueur courant.
D’ailleurs et pendant le jeu, le joueur courant ne peut jouer que dans un des 9 plateaux
selon les règles du jeu (vous pouvez par exemple désactiver les 8 autres plateaux ou
afficher un message d’erreur si le joueur sélectionne un plateau non permis).

10 points

5. Afin de simplifier le jeu, un joueur gagne une partie quand il gagne son premier
plateau parmi les 9 existants selon les règles du jeu classique. De la même façon, une
partie est nulle quand un des plateaux est devenu plein sans qu’un joueur puisse gagner
ce plateau selon toujours les mêmes règles du jeu classique. De ce fait, l’application
des vraies règles du jeu Ultimate Tic-Tac-Toe est une fonctionnalité facultative (voir
plus bas.)

12 points

6. À la fin de chaque partie, vous devez afficher les statistiques du jeu comme c’était le
cas pour le TP2 (vous pouvez utiliser par exemple des Labels ou des messagebox).

8 points

7. L’utilisateur peut recommencer une partie ou terminer le jeu comme c’était le cas pour
le TP2 (vous pouvez utiliser par exemple des boutons).

5 points
8. Gestion des erreurs (aucune exception laissée passée en console). 5 points
Total 60 points
3.2 Fonctionnalités facultatives
Choisissez parmi les fonctionnalités suivantes celles que vous désirez intégrer à votre jeu. Certaines
fonctionnalités sont plus difficiles à réaliser que d’autres, et vous ne pouvez pas dépasser 100%. Vous
pouvez par contre récupérer des points qui auraient pu être perdus dans une autre fonctionnalité facultative !


4

Fonctionnalité facultative Pondération
1. Centrer la fenêtre principale du jeu par rapport à l’écran (chercher la méthode geometry). 4 points
2. Redimensionner automatiquement l’interface du jeu après chaque modification de la taille de
la fenêtre principale (e.g. augmenter la taille des cases suite par exemple à l’agrandissement
de la fenêtre sur toute la surface de l’écran). Vous pouvez vous inspirer du laboratoire 11 de
la semaine 13.

6 points

3. Option de lire les règlements du jeu (vous pouvez utiliser par exemple un bouton et un
messagebox).

5 points

4. Affichage de l’historique des cases sélectionnées (vous pouvez utiliser par exemple une
listbox ou les widgets Text et Scrollbar).

5 points

5. L’utilisateur peut choisir de commencer le jeu ou laisser l’adversaire le faire (vous pouvez
utiliser par exemple des radiobouttons ou un Combobox).

3 points

6. Affichage du pion du joueur courant dans la case avant même sa sélection (La position du
pion affiché change avec le mouvement de la sourie).

5 points

7. Pendant le jeu, le programme change la couleur du prochain plateau afin de le mettre en
évidence et faciliter ainsi le choix du joueur courant.

5 points

8. Implanter les vraies règles du jeu Ultimate Tic-Tac-Toe. Un joueur ne peut gagner donc que
s’il gagne trois plateaux sur une ligne, une colonne ou une diagonale du grand plateau parent.
Si un joueur envoie son adversaire à un plateau déjà gagné ou ayant un résultat nul, cet
adversaire peut choisir le plateau qu’il veut pour son prochain coup. Sinon, vous pouvez
considérer un plateau ayant un résultat nul soit qu’il appartient aux deux joueurs soit qu’il
n’appartient à aucun des deux joueurs.

10 points

9. Annuler le dernier choix effectué (vous pouvez utiliser par exemple un bouton).

5 points
10. On peut sauvegarder une partie (vous pouvez le faire par exemple dans un fichier texte). 5 points
11. On peut charger une partie (vous pouvez le faire par exemple à partir d’un fichier texte). 5 points
12. On peut interrompre le jeu pour créer une nouvelle partie en remettant les statistiques à zéro. 5 points
13. On peut revoir une partie qui a été déjà sauvegardée en faisant une simulation. 8 points
14. Demander au programme de nous proposer le prochain coup afin de savoir ce que
l’ordinateur va jouer s’il était à notre place.

3 points

15. Proposer des niveaux différents (i.e. simple, intermédiaire, avancé, etc.) pour les choix de
l’ordinateur. Il serait donc plus difficile de gagner contre un ordinateur si son niveau est
élevé.

7 points
16. Afficher la date et l’heure ainsi que le temps écoulé depuis le début de la partie. 5 points
17. Une autre fonctionnalité (à faire valider par l’enseignant avant de l’implanter. Elle peut être
éventuellement ajoutée dans la liste des précisions sur le site Web du cours afin que les autres
équipes puissent également la choisir).

-


5

4 Éléments fournis
Nous vous fournissons un projet contenant les répertoires et fichiers suivants :
tictactoe/
__init__.py
case.py
joueur.py
partie.py
plateau.py
interface/
__init__.py
jeu_utictactoe.py
principal.py
Les fichiers __init__.py sont des fichiers spéciaux indiquant à Python que le dossier est un « package », c’est
à dire un dossier contenant des modules qui peuvent être importés à l’aide de :
from nom_package.nom_module import nom_classe
Le fichier principal.py est le programme principal à partir duquel exécuter le TP. Il ne fait que démarrer
l’interface à partir du bon répertoire. Il est à noter que vous devez compléter les commentaires de chaque
fichier (auteurs, date, description, Attributes, etc.) et chaque méthode existante ou ajoutée (Args, Returns,
etc.).
5 Ce que vous devez rendre
À l’aide de l’intranet (pixel), vous devez rendre un fichier .zip comportant uniquement les fichiers suivants :
 Les répertoires et fichiers (.py) de votre projet contenant l’implantation de votre application.
 Le fichier NoteTp3-IFT1004-H2015.xls contenant le barème utilisé pour la correction. Vous devez
ajouter les noms des membres de votre équipe et également enlever les fonctionnalités facultatives
que vous n’avez pas implémentées (supprimer les lignes du fichier Excel) afin de faciliter le travail
des correcteurs.
 Ne remettez aucun autre fichier ou dossier que ce qui est mentionné ci-haut.
Le nom du .zip doit respecter le format suivant : TP3-Matricule.zip où Matricule est le numéro de matricule
de la personne qui va envoyer le travail sur pixel (un seul travail par équipe doit être envoyé sur pixel,
sinon vous risquez d’avoir une pénalité).
De plus, il est de votre responsabilité de vérifier après la remise que vous nous avez envoyé les bons fichiers
(non vides et non corrompus), sinon vous pouvez avoir un zéro.

Bon travail !
