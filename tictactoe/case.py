__author__ = 'IFT-1004-H2015'
__date__ = "12 mars 2015"

"""Ce fichier permet de définir la classe Case permettant de jouer au jeu Tic-Tac-Toe"""

class Case:
    """
    Classe modélisant une case du jeu Tic-Tac-Toe.

    Attributes:
        contenu (str): Le contenu de la case (" ", "O" ou "X").

    """

    def __init__(self, contenu):
        """
        La méthode spéciale __init__ d'une classe est appelée lorsqu'on instancie
        un nouvel objet. Elle peut prendre des paramètres supplémentaires (ici "contenu").
        Le mot clé "self" permet de stocker des informations dans l'instance de l'objet.
        Chaque instance a son propre espace mémoire et peut donc contenir des valeurs
        différentes dans ses variables membres.

        Args:
            contenu (string): le contenu de la case (" ", "O" ou "X")
        """
        assert isinstance(contenu, str), "Case: contenu doit être une chaîne de caractères."
        assert contenu in [" ", "O", "X"], "Case: contenu doit être ' ', 'O' ou 'X'."

        self.contenu = contenu  # Le contenu de la case (" ", "O" ou "X").

    def est_vide(self):
        """
        Retourne si la case est vide (un espace).

        Returns:
            bool: True si la case est vide, False autrement.
        """
        return self.contenu == " "

    def est_O(self):
        """
        Retourne si la case contient le pion "O".

        Returns:
            bool: True si la case contient le pion "O", False autrement.
        """
        return self.contenu == "O"

    def est_X(self):
        """
        Retourne si la case contient le pion "X".

        Returns:
            bool: True si la case contient le pion "X", False autrement.
        """
        return self.contenu == "X"

    def est_pion(self, pion):
        """
        Retourne si la case contient le pion entré en paramètre.

        Args:
            pion (string): le contenu de la case (" ", "O" ou "X")

        Returns:
            bool: True si la case contient ce pion, False autrement.
        """
        assert isinstance(pion, str), "Case: pion doit être une chaîne de caractères."
        assert pion in [" ", "O", "X"], "Case: pion doit être ' ', 'O' ou 'X'."

        return self.contenu == pion