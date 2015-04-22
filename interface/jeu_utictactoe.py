__authors__ = 'Olivier Cardinal et Éric Laflamme'
__date__ = "Ajoutez la date de remise"

"""Ce fichier permet de...(complétez la description de ce que
ce fichier est supposé faire ! """

from tkinter import Tk, Canvas, Label, Entry, Checkbutton, IntVar, Frame, GROOVE, RAISED, messagebox, Button, E, W
from tictactoe.partie import Partie
from tictactoe.joueur import Joueur
from modules.ModulesPerso import centreFen
from modules.gestionErr import ErreurChoixCase, EstGagnant


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
                         height=self.plateau.n_colonnes * self.taille_case, borderwidth=2, bg="grey")

        # Dessiner le plateau du jeu ultimate Tic-Tac-Toe.
        self.dessiner_plateau()


    def dessiner_plateau(self):
        """
            Fonction qui créer les 9 carrés de jeu compris à l'intérieur des 9 plateaux de jeu.
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
    def __init__(self, joueur1, joueur2, type2, pion1, pion2, force):
        """
            À completer !.
        :param joueur1, joueur2, type2, pion1, pion2, force
        """
        self.type2 = type2
        self.force_ordi = force

        super().__init__()

        # Nom de la fenêtre.
        self.title("Ultimate Tic-Tac-Toe")

        # La partie de ultimate Tic-Tac-Toe
        self.partie = Partie()

        # Initialiser les joueurs en créant des classes Joueur avec nom, type et pion.
        p1 = Joueur(joueur1, "Personne", pion1)
        p2 = Joueur(joueur2, type2, pion2)
        #self.force = force
        self.partie.joueurs = [p1,p2]
        self.partie.joueur_courant = p1

        # Un dictionnaire contenant les 9 canvas des 9 plateaux du jeu
        self.canvas_uplateau = {}

        # Bouton pour quitter le match
        Button(self.canvas_uplateau, text = 'Quitter', command = self.destroy).grid(row = 20, column = 0, sticky = E)

        # Étiquette d'information sur les joueurs, les pions et le joueur courant.
        self.label_joueur_courant = Label(text="À votre tour {}".format(p1.nom), font=("Arial", 14), fg="#0080FF")
        self.label_joueur_courant.grid(row=1, columnspan=3, padx=5, pady=5)
		
        # Étiquette des statistiques des parties gagnées par chaque joueur initialisées à zéro
        self.label_stat = Label(text="Plateaux gagnées: \n\n{} : {}\n{} : {}"\
                                .format(joueur1, 0, joueur2, 0))
        self.label_stat.grid(row = 10, column =1)

        # Appel de la méthode qui dessine le plateau de Tic-Tac-Toe Ultime
        self.dessiner_canvas(self)

        # Ajout d'une étiquette d'information.
        self.messages = Label(self)
        self.messages.grid(columnspan=3)

        # Centrer la fenêtre. Détermine la taille de la fenêtre.
        self.width_fen, self.height_fen = 740, 750
        centreFen(self, self.width_fen, self.height_fen)

    def selectionner(self, event):
        """
            Permet de dessiner le pion dans la case sélectionnée.
        """

        self.reinitialise = False

        # Faire joueur l'ordinateur si le joueur courant est l'ordinateur. Définir ligne et colonne
        # selon le choix de l'ordinateur. Si joueur est une personne, la ligne et la colonne vient
        # des coordonnées de l'événement créé par le clic de la souris.
        if self.partie.joueur_courant.type == "Ordinateur":
            pion = self.partie.joueur_courant.pion
            ligne, colonne = event.widget.plateau.choisir_prochaine_case(pion, self.force_ordi)
        else:
            # On trouve le numéro de ligne/colonne en divisant par le nombre de pixels par case.
            # event.widget représente ici un des 9 canvas !
            ligne = event.y // event.widget.taille_case
            colonne = event.x // event.widget.taille_case

        try:

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
                    self.partie.joueur_courant.nb_parties_gagnees +=1
                    raise EstGagnant (" Bravo {}, Vous avez gagné un plateau !!!".format (self.partie.joueur_courant.nom))
            except EstGagnant as e:
                messagebox.showinfo("Partie terminée", str(e))

                # affichage des statistiques
                self.label_stat = Label(text="Plateaux gagnées:\n\n{} :{}\n{} :{}"\
                        .format(self.partie.joueurs[0].nom, self.partie.joueurs[0].nb_parties_gagnees,
                                self.partie.joueurs[1].nom, self.partie.joueurs[1].nb_parties_gagnees))
                self.label_stat.grid(row = 10, column =1)

                # Partie terminée, redémarrer ou quitter.
                if messagebox.askyesno("Continuer", "Voulez-vous continuer?",):
                    self.vider_plateau(event)
                    self.reinitialise = True
                else:
                    self.destroy()

            # Changer le joueur courant.
            # Vous pouvez modifier ou déplacer ce code dans une autre méthode selon votre propre solution.
            if self.partie.joueur_courant == self.partie.joueurs[0]:
                self.partie.joueur_courant = self.partie.joueurs[1]
            else:
                self.partie.joueur_courant = self.partie.joueurs[0]

            # Modification au libellé pour afficher joueur courant
            self.label_joueur_courant["text"]="À votre tour {}".format(self.partie.joueur_courant.nom)

            # Effacer le contenu du widget (canvas) et du plateau (dictionnaire) quand ce dernier devient plein.
            # Vous pouvez modifier ou déplacer ce code dans une autre méthode selon votre propre solution.
            if not event.widget.plateau.non_plein():
                event.widget.delete('pion')
                event.widget.plateau.initialiser()

            # Appel de la procédure qui désactive les 8 autres plateaux
            if not self.reinitialise:
                self.desactiver_plateau(ligne, colonne)

        except ErreurChoixCase as e:
            messagebox.showerror ("Erreur", str(e))

    def desactiver_plateau(self, ligne, colonne):
        """
            Procédure qui active le plateau où le jeu doit se jouer et désactive les 8 autres plateaux.

        :param ligne: No. de la ligne du plateau à ne pas désactiver
        :param colonne: No. de la colonne du plateau à ne pas désactiver
        :return: None
        """

        for i in range(0, 3):
            for j in range(0, 3):
                if i != ligne or j != colonne:
                    self.canvas_uplateau[i,j]['background'] = 'white'
                    self.canvas_uplateau[i,j].unbind('<Button-1>')

                else:
                    self.canvas_uplateau[i,j]['background'] = '#0080FF'
                    self.canvas_uplateau[ligne, colonne].bind('<Button-1>', self.selectionner)

    def afficher_message(self, message):
        """
            À completer !.
        """
        self.messages['foreground'] = 'black'
        self.messages['text'] = message

    def afficher_joueur_courant(self, joueur_courant):
        """
            Définition du texte à afficher pour le libellé label_joueur_courant
        :param joueur_courant:
        :return: Text à afficher pour le libellé label_joueur_courant
        """
        if self.partie=="Ordinateur":
            text = "Au tour de Colosse"
        else:
            text = "À votre tour {}".format(self.partie.joueur_courant.nom)

    def vider_plateau(self,event):

        self.partie.initialiser()
        self.frame_plateau.destroy()
        self.dessiner_canvas(self)
        for i in range(0, 3):
            for j in range(0, 3):
                self.canvas_uplateau[i,j]['bg']="grey"
                self.canvas_uplateau[i,j].bind('<Button-1>')


    def dessiner_canvas(self, parent):

        # Création d'un frame qui contient le plateau de jeu
        self.frame_plateau = Frame(parent)
        self.frame_plateau.grid(row = 10, column=0, padx=5, pady=5)

        # Création des frames et des canvas du jeu
        for i in range(0, 3):
            for j in range(0, 3):
                cadre = Frame(self.frame_plateau, borderwidth=5, relief=GROOVE)
                cadre.grid(row=i, column=j, padx=5, pady=5)
                self.canvas_uplateau[i,j] = CanvasPlateau(cadre, self.partie.uplateau[i,j])
                self.canvas_uplateau[i,j].grid()
                # On lie un clic sur le Canvas à une méthode.
                self.canvas_uplateau[i,j].bind('<Button-1>', self.selectionner)
