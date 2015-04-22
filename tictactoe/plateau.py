__author__ = 'IFT-1004-H2015'
__date__ = "12 mars 2015"

"""Ce fichier permet de définir la classe Partie permettant de jouer au jeu Tic-Tac-Toe"""

from tictactoe.case import Case
from random import randrange
from tkinter import messagebox

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

    def choisir_prochaine_case(self, pion, force_ordi):
        """
        Permet de retourner les coordonnées (ligne, colonne) de la case que l'ordinateur
        peut choisir afin de jouer contre un autre joueur qui est normalement une personne.
        Ce choix doit se faire en fonction de la configuration actuelle du plateau.

        Voici une solution, mais sachez qu'il existe de solutions plus efficaces.
        Vous pouvez bien sûr utiliser votre solution si elle fonctionne bien!

        Args:
            pion (string): La forme du pion de l'adversaire de l'ordinateur ("X" ou "O").
            force_ordi(int): Détermine le niveau de difficulté de l'ordinateur.

        Returns:
            (int,int): Une paire d'entiers représentant les coordonnées de la case choisie.
        """
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."

        self.pion = pion
        self.good = False
        self.combines = []
        i , j, k = 0 , 0 , 0
        valide = False
        liste_possibilite_2 = []
        liste_possibilite_2_adv = []
        liste_possibilite_1 = []
        liste_possibilite_1_adv = []
        liste_vides = []
        irand = 0

        # Déterminer la force de l'ordinateur.
        if force_ordi == 1:
            difficulte = 50
        elif force_ordi == 2:
            difficulte = 75
        else:
            difficulte = 100

        #procédure qui créer une liste des lignes, colonnes et diagonales actuelles servant à comparer et
        #à permettre à l'ordinateur de savoir où placer son pion.

        for l in range(0,3):
            lignePion = ''
            for c in range(0,3):
                lignePion += self.cases[(l,c)].contenu
            self.combines.append(lignePion)
        for c in range(0,3):
            lignePion = ''
            for l in range(0,3):
                lignePion += self.cases[(l,c)].contenu
            self.combines.append(lignePion)
        lignePion = ''
        l = 3
        for c in range(0,3):
            l -= 1
            lignePion += self.cases[(l,c)].contenu
        self.combines.append(lignePion)
        lignePion = ''
        for cl in range(0,3):
            lignePion += self.cases[(cl,cl)].contenu
        self.combines.append(lignePion)

        # Création d'une liste de toutes les cases vides
        for li in range(0,3):
            for co in range(0,3):
                if self.cases[(li, co)].est_vide():
                    liste_vides.append((li, co))

        if self.pion == "O":
            self.pion2 = "X"
        else:
            self.pion2 = "O"

        #procédure permettant de définir la force de l'ordinateur selon la difficulté. Si le nombre est compris entre
        #0 et le niveau difficulté, l'ordinateur sera fort. Si le nombre est compris entre le niveau de difficulté
        #et 100 l'ordinateur joueura n'importe quelle case sans tenir compte d'une possible victoire ou défaite.
        brain = randrange (0,100)
        if brain <= difficulte:
            self.good = True

        if self.good:
            for combine in self.combines: #parcours chaque combine possible
                #parcours les lignes
                if i <= 2:
                    if combine.replace(" ","") == self.pion * 2:
                        for j in range(0,3):
                            if self.cases[(i,j)].est_vide():
                                liste_possibilite_2.append((i, j))
                    if combine.replace(" ","") == self.pion2 * 2:
                        for j in range(0,3):
                            if self.cases[(i,j)].est_vide():
                                liste_possibilite_2_adv.append((i, j))
                    if combine.replace(" ","") == self.pion:
                        for j in range(0,3):
                            if self.cases[(i,j)].est_vide():
                                liste_possibilite_1.append((i, j))
                    if combine.replace(" ","") == self.pion2:
                        for j in range(0,3):
                            if self.cases[(i,j)].est_vide():
                                liste_possibilite_1_adv.append((i, j))
                #parcours les colonnes
                elif i > 2 and i <= 5:
                    if combine.replace(" ","") == self.pion * 2:
                        for j in range(0,3):
                            if self.cases[(j,k)].est_vide():
                                liste_possibilite_2.append((j, k))
                    if combine.replace(" ","") == self.pion2 * 2:
                        for j in range(0,3):
                            if self.cases[(j,k)].est_vide():
                                liste_possibilite_2_adv.append((j, k))
                    if combine.replace(" ","") == self.pion:
                        for j in range(0,3):
                            if self.cases[(j,k)].est_vide():
                                liste_possibilite_1.append((j, k))
                    if combine.replace(" ","") == self.pion2:
                        for j in range(0,3):
                            if self.cases[(j,k)].est_vide():
                                liste_possibilite_1_adv.append((j, k))
                    k += 1
                #parcours la première diagonale
                elif i == 6:
                    l = 3
                    if combine.replace(" ","") == self.pion * 2:
                        for j in range(0,3):
                            l -= 1
                            if self.cases[(j,l)].est_vide():
                                liste_possibilite_2.append((j, l))
                    l = 3
                    if combine.replace(" ","") == self.pion2 * 2:
                        for j in range(0,3):
                            l -= 1
                            if self.cases[(j,l)].est_vide():
                                liste_possibilite_2_adv.append((j, l))
                    l = 3
                    if combine.replace(" ","") == self.pion:
                        for j in range(0,3):
                            l -= 1
                            if self.cases[(j,l)].est_vide():
                                liste_possibilite_1.append((j, l))
                    l = 3
                    if combine.replace(" ","") == self.pion2:
                        for j in range(0,3):
                            l -= 1
                            if self.cases[(j,l)].est_vide():
                                liste_possibilite_1_adv.append((j, l))
                #parcours la deuxième diagonale
                elif i == 7:
                    if combine.replace(" ","") == self.pion * 2:
                        for j in range(0,3):
                            if self.cases[(j,j)].est_vide():
                                liste_possibilite_2.append((j, j))
                    if combine.replace(" ","") == self.pion2 * 2:
                        for j in range(0,3):
                            if self.cases[(j,j)].est_vide():
                                liste_possibilite_2_adv.append((j, j))
                    if combine.replace(" ","") == self.pion:
                        for j in range(0,3):
                            if self.cases[(j,j)].est_vide():
                                liste_possibilite_1.append((j, j))
                    if combine.replace(" ","") == self.pion2:
                        for j in range(0,3):
                            if self.cases[(j,j)].est_vide():
                                liste_possibilite_1_adv.append((j, j))
                i += 1

            # Vérifie à travers les possibilités celle qui est la plus
            # avantageuse et renvoie les coordonnées de la case.
            if liste_possibilite_2:
                irand = randrange(0, len(liste_possibilite_2))
                ligne, colonne = liste_possibilite_2[irand]
            elif liste_possibilite_2_adv:
                irand = randrange(0, len(liste_possibilite_2_adv))
                ligne, colonne = liste_possibilite_2_adv[irand]
            elif liste_possibilite_1:
                irand = randrange(0, len(liste_possibilite_1))
                ligne, colonne = liste_possibilite_1[irand]
            elif liste_possibilite_1_adv:
                irand = randrange(0, len(liste_possibilite_1_adv))
                ligne, colonne = liste_possibilite_1_adv[irand]
            else:
                irand = randrange(0, len(liste_vides))
                ligne, colonne = liste_vides[irand]
        else:
            irand = randrange(0, len(liste_vides))
            ligne, colonne = liste_vides[irand]

        return ligne , colonne