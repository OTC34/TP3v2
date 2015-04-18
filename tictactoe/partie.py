__author__ = 'IFT-1004-H2015'
__date__ = "05 avril 2015"

"""Ce fichier permet de définir la classe Partie permettant de jouer au jeu Ultimate Tic-Tac-Toe"""

from tictactoe.plateau import Plateau

class Partie:
    """
    Classe modélisant une partie du jeu Ultimate Tic-Tac-Toe utilisant
    9 plateaux et deux joueurs (deux personnes ou une personne et un ordinateur).

    Attributes:
        uplateau (dictionary): Le dictionnaire contenant les 9 plateaux du jeu.
                               La clé est une position (ligne, colonne),
                               et la valeur est une instance de la classe Plateau.
        joueurs (Joueur list): La liste des deux joueurs (initialement une liste vide).
        joueur_courant (Joueur): Le joueur courant (initialisé à une valeur nulle: None).
        nb_parties_nulles (int): Le nombre de parties nulles.
    """

    def __init__(self):
        """
        Méthode spéciale initialisant une nouvelle partie du jeu Ultimate Tic-Tac-Toe.
        """
        # Le plateau de ultimate Tic-Tac-Toe contenant les 9 plateaux Tic-Tac-Toe.
        self.uplateau = {}


        self.joueurs = []   # La liste des deux joueurs (initialement une liste vide).
                            # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
                                    # Pendant le jeu et à chaque tour d'un joueur,
                                    # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

        self.initialiser()

    def initialiser(self):
        """
        Initialise la partie avec des plateaux contenant des cases vides.
        """

        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.uplateau.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Plateau.
        for i in range(0, 3):
            for j in range(0, 3):
                self.uplateau[i,j] = Plateau((i,j))