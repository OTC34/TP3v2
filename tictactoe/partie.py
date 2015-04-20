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

    def tour(self, choix):
        """
        Permet d'exécuter le tour d'un joueur (une personne ou un ordinateur).
        Cette méthode doit afficher le plateau (voir la méthode __str__() de la classe Plateau).
        Si le joueur courant est un ordinateur, il faut calculer la position de la prochaine
        case à jouer par cet ordinateur en utilisant la méthode choisir_prochaine_case().
        Si le joueur courant est une personne, il faut lui demander la position de la prochaine
        case qu'il veut jouer en utilisant la méthode demander_postion().
        Finalement, il faut utiliser la méthode selectionner_case() pour modifier le contenu
        de la case choisie soit par l'ordinateur soit par la personne.

        Args:
            choix (int): Un entier représentant le choix de l'utilisateur dans le menu du jeu (1 ou 2).
        """

        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."

        self.choix = choix

        if self.choix == 1:
            if self.joueur_courant.type == "Personne":
                ligne, colonne = self.demander_postion(self.joueur_courant.nom)
                self.plateau.selectionner_case(ligne, colonne, self.joueur_courant.pion)
            elif self.joueur_courant.type == "Ordinateur":
                ligne, colonne = self.plateau.choisir_prochaine_case(self.joueur_courant.pion)
                self.plateau.selectionner_case(ligne, colonne, self.joueur_courant.pion)
        else:
            ligne, colonne = self.demander_postion(self.joueur_courant.nom)
            self.plateau.selectionner_case(ligne, colonne, self.joueur_courant.pion)