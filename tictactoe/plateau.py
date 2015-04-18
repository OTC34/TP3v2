__author__ = 'IFT-1004-H2015'
__date__ = "12 mars 2015"

"""Ce fichier permet de définir la classe Partie permettant de jouer au jeu Tic-Tac-Toe"""

from tictactoe.case import Case
from random import randrange

class Plateau:
    """
    Classe modélisant le plateau du jeu Tic-Tac-Toe.

    Attributes:
        cases (dictionary): Dictionnaire de cases. La clé est une position (ligne, colonne),
                            et la valeur est une instance de la classe Case.
        self.cordonnees_parent (int,int): Une paire contenant les coordonnées du parent du plateau.
        self.n_lignes (int): Le nombre de lignes dans un plateau (par défaut = 3).
        self.n_colonnes (int): Le nombre de colonnes dans un plateau (par défaut = 3).
    """

    def __init__(self, cordonnees_parent, n_lignes=3, n_colonnes=3):
        """
        Méthode spéciale initialisant un nouveau plateau contenant les 9 cases du jeu.
        """

        self.cordonnees_parent = cordonnees_parent
        self.n_lignes = n_lignes
        self.n_colonnes = n_colonnes

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        """
        Initialise le plateau avec des cases vides (contenant des espaces).
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")

    def non_plein(self):
        """
        Retourne si le plateau n'est pas encore plein.
        Il y a donc encore des cases vides (contenant des espaces et non des "X" ou des "O").

        Returns:
            bool: True si le plateau n'est pas plein, False autrement.
        """
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cases[(i,j)].est_vide():
                    return True
        return False

    def position_valide(self, ligne, colonne):
        """
        Vérifie si une position est valide pour jouer.
        La position ne doit pas être occupée.
        Il faut utiliser la méthode est_vide() de la classe Case.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.

        Returns:
            bool: True si la position est valide, False autrement.
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."

        return self.cases[ligne,colonne].est_vide()

    def selectionner_case(self, ligne, colonne, pion):
        """
        Permet de modifier le contenu de la case
        qui a les coordonnées (ligne,colonne) dans le plateau du jeu
        en utilisant la valeur de la variable pion.

        Args:
            ligne (int): Le numéro de la ligne dans le plateau du jeu.
            colonne (int): Le numéro de la colonne dans le plateau du jeu.
            pion (string): Une chaîne de caractères ("X" ou "O").
        """
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert ligne in [0, 1, 2], "Plateau: ligne doit être 0, 1 ou 2."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert colonne in [0, 1, 2], "Plateau: colonne doit être 0, 1 ou 2."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        self.cases[ligne,colonne].contenu = pion


    def est_gagnant(self, pion):
        """
        Permet de vérifier si un joueur a gagné le jeu.
        Il faut vérifier toutes les lignes, colonnes et diagonales du plateau.

        Args:
            pion (string): La forme du pion utilisé par le joueur en question ("X" ou "O").

        Returns:
            bool: True si le joueur a gagné, False autrement.
        """

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        vtest = (pion,pion,pion)
        return  ((self.cases[0,0].contenu,self.cases[0,1].contenu,self.cases[0,2].contenu) == vtest or
                (self.cases[1,0].contenu,self.cases[1,1].contenu,self.cases[1,2].contenu) == vtest or
                (self.cases[2,0].contenu,self.cases[2,1].contenu,self.cases[2,2].contenu) == vtest or
                (self.cases[0,0].contenu,self.cases[1,0].contenu,self.cases[2,0].contenu) == vtest or
                (self.cases[0,1].contenu,self.cases[1,1].contenu,self.cases[2,1].contenu) == vtest or
                (self.cases[0,2].contenu,self.cases[1,2].contenu,self.cases[2,2].contenu) == vtest or
                (self.cases[0,0].contenu,self.cases[1,1].contenu,self.cases[2,2].contenu) == vtest or
                (self.cases[2,0].contenu,self.cases[1,1].contenu,self.cases[0,2].contenu) == vtest)

    def choisir_prochaine_case(self, pion):
        """
        Permet de retourner les coordonnées (ligne, colonne) de la case que l'ordinateur
        peut choisir afin de jouer contre un autre joueur qui est normalement une personne.
        Ce choix doit se faire en fonction de la configuration actuelle du plateau.

        Voici une solution, mais sachez qu'il existe de solutions plus efficaces.
        Vous pouvez bien sûr utiliser votre solution si elle fonctionne bien!

        Args:
            pion (string): La forme du pion de l'adversaire de l'ordinateur ("X" ou "O").

        Returns:
            (int,int): Une paire d'entiers représentant les coordonnées de la case choisie.
        """
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        if pion == "X":
            pion_adverse = "O"
        else:
            pion_adverse = "X"

        # Chercher si l'ordi ou l'adversaire peuvent gagner en choisissant une case.
        # Dans ce cas, on retourne les coordonnées de cette case!
        for i in range(0, 3):
            for j in range(0, 3):
                if self.position_valide(i, j):
                    self.selectionner_case(i, j, pion)
                    # Chercher si l'ordi peut gagner en jouant cette case !
                    if self.est_gagnant(pion):
                        self.cases[(i,j)].contenu = " "
                        return i, j
                    self.cases[(i,j)].contenu = " "
                    self.selectionner_case(i, j, pion_adverse)
                    # Chercher si l'adversaire peut gagner en jouant cette case !
                    if self.est_gagnant(pion_adverse):
                        self.cases[(i,j)].contenu = " "
                        return i, j
                    self.cases[(i,j)].contenu = " "

        # Sinon, retourner au hasard une case parmi celles qui sont vides !
        liste = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.cases[i,j].est_vide():
                    liste += [(i,j)]

        irand = randrange(0,len(liste))
        return liste[irand]