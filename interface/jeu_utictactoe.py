__authors__ = 'Olivier Cardinal et Éric Laflamme'
__date__ = "Ajoutez la date de remise"

"""Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire ! """

from tkinter import Tk, Canvas, Label, Entry, Checkbutton, IntVar, Frame, GROOVE, RAISED, messagebox, Button, E, W
from tictactoe.partie import Partie
from tictactoe.joueur import Joueur
from modules.ModulesPerso import centreFen

class ErreurChoixCase(Exception):
    pass

class EstGagnant(Exception):
    pass

class CanvasPlateau(Canvas):
    """
        Canvas sur lequel sera dessiné le plateau de jeu du Tic-Tac-Toe Ultime
    """
    def __init__(self, parent, plateau, taille_case=60):

        # Une instance d'un des 9 plateaux du jeu ultimate Tic-Tac-Toe.
        self.plateau = plateau

        # Nombre de pixels par case.
        self.taille_case = taille_case

        # Appel du constructeur de la classe de base (Canvas).
        super().__init__(parent, width=self.plateau.n_lignes * taille_case,
                         height=self.plateau.n_colonnes * self.taille_case)

        # Dessiner le plateau du jeu ultimate Tic-Tac-Toe.
        self.dessiner_plateau()


    def dessiner_plateau(self):
        """
            À completer !.
        """
        for i in range(self.plateau.n_lignes):
            for j in range(self.plateau.n_colonnes):
                debut_ligne = i * self.taille_case
                fin_ligne = debut_ligne + self.taille_case
                debut_colonne = j * self.taille_case
                fin_colonne = debut_colonne + self.taille_case
                # On dessine le rectangle représentant une case!
                self.create_rectangle(debut_colonne, debut_ligne, fin_colonne, fin_ligne,
                                      fill='#e1e1e1', width = 2, outline = "white")


class Fenetre(Tk):
    """
        À completer !.
    """
    def __init__(self):
        """
            À completer !.
        """
        super().__init__()

        # Nom de la fenêtre.
        self.title("Ultimate Tic-Tac-Toe")

        # La partie de ultimate Tic-Tac-Toe
        self.partie = Partie()

        # Un ditionnaire contenant les 9 canvas des 9 plateaux du jeu
        self.canvas_uplateau = {}

		# Bouton pour quitter le match
        Button(self.canvas_uplateau, text = 'Quitter', command = self.quit).grid(row = 5, column = 4, sticky = E)
		
        # Création des frames et des canvas du jeu
        for i in range(0, 3):
            for j in range(0, 3):
                cadre = Frame(self, borderwidth=5, relief=GROOVE)
                cadre.grid(row=i, column=j, padx=5, pady=5)
                self.canvas_uplateau[i,j] = CanvasPlateau(cadre, self.partie.uplateau[i,j])
                self.canvas_uplateau[i,j].grid()
                # On lie un clic sur le Canvas à une méthode.
                self.canvas_uplateau[i,j].bind('<Button-1>', self.selectionner)

        # Ajout d'une étiquette d'information.
        self.messages = Label(self)
        self.messages.grid(columnspan=3)

        # Création de deux joueurs. Ce code doit être bien sûr modifié,
        # car il faut chercher ces infos dans les widgets de la fenêtre.
        # Vous pouvez également déplacer ce code dans une autre méthode selon votre propre solution.
        #p1 = Joueur("VotreNom", "Personne", 'X')
        #p2 = Joueur("Colosse", "Ordinateur", 'O')
        #self.partie.joueurs = [p1,p2]
        #self.partie.joueur_courant = p1

        # Centrer la fenêtre. Détermine la taille de la fenêtre.
        self.width_fen, self.height_fen = 670, 800
        centreFen(self, self.width_fen, self.height_fen)

    def selectionner(self, event):
        """
            À completer !.
        """
        print (self.partie.joueur_courant.nom)
		
		
        try:
            # On trouve le numéro de ligne/colonne en divisant par le nombre de pixels par case.
            # event.widget représente ici un des 9 canvas !
            ligne = event.y // event.widget.taille_case
            colonne = event.x // event.widget.taille_case

            if not self.partie.uplateau[event.widget.plateau.cordonnees_parent].cases[ligne, colonne].est_vide():
                raise ErreurChoixCase ("La case est déjà sélectionné !")

            self.afficher_message("Case sélectionnée à la position (({},{}),({},{}))."
                                  .format(event.widget.plateau.cordonnees_parent[0],
                                          event.widget.plateau.cordonnees_parent[1],
                                          ligne, colonne))

            # On dessine le pion dans le canvas, au centre de la case.
            # On utilise l'attribut "tags" pour être en mesure de récupérer
            # les éléments dans le canvas afin de les effacer par exemple.
            coordonnee_y = ligne * event.widget.taille_case + event.widget.taille_case // 2
            coordonnee_x = colonne * event.widget.taille_case + event.widget.taille_case // 2
            event.widget.create_text(coordonnee_x, coordonnee_y, text=self.partie.joueur_courant.pion,
                                     font=('Helvetica', event.widget.taille_case//2), tags='pion')

            # Mettre à jour la case sélectionnée
            self.partie.uplateau[event.widget.plateau.cordonnees_parent]\
                .selectionner_case(ligne, colonne, self.partie.joueur_courant.pion)

            try:
                # On vérifie si le joueur courant est gagnant
                    if event.widget.plateau.est_gagnant(self.partie.joueur_courant.pion):
                        raise EstGagnant (" Bravo {}, Vous avez gagné un plateau !!!".format (self.partie.joueur_courant.nom))
            except EstGagnant as e:
                messagebox.showwarning("Terminé", str(e))

            # Changer le joueur courant.
            # Vous pouvez modifier ou déplacer ce code dans une autre méthode selon votre propre solution.
            if self.partie.joueur_courant == self.partie.joueurs[0]:
                self.partie.joueur_courant = self.partie.joueurs[1]
            else:
                self.partie.joueur_courant = self.partie.joueurs[0]

            # Effacer le contenu du widget (canvas) et du plateau (dictionnaire) quand ce dernier devient plein.
            # Vous pouvez modifier ou déplacer ce code dans une autre méthode selon votre propre solution.
            if not event.widget.plateau.non_plein():
                event.widget.delete('pion')
                event.widget.plateau.initialiser()

        except ErreurChoixCase as e:
            messagebox.showerror ("Erreur", str(e))
	
    def desactiver_plateau(self, ligne, colonne):

        for i in range(0, 3):
            for j in range(0, 3):
                if i != ligne or j != colonne:
                    self.canvas_uplateau[i,j]['borderwidth'] = 2
                    self.canvas_uplateau[i,j]['background'] = '#e1e1e1'
                    self.canvas_uplateau[i,j].unbind('<Button-1>')

                else:

                    self.canvas_uplateau[i,j]['borderwidth'] = 2
                    self.canvas_uplateau[i,j]['background'] = 'blue'
                    self.canvas_uplateau[ligne, colonne].bind('<Button-1>', self.selectionner)

    def activer_plateau(self):
        self.canvas_uplateau[0,0].bind('<Button-1>'.self.selectionner)

    def afficher_message(self, message):
        """
            À completer !.
        """
        self.messages['foreground'] = 'black'
        self.messages['text'] = message

