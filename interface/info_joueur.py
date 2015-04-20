__author__ = 'IFT-1004-H2015'
__date__ = "12 mars 2015"

""" Ce fichier  permet de débuter une partie de tic-tac-toe ultime. Le début de la partie ce fait
avec la fenêtre qui permet de saisir les informations sur les joueurs. Les joueurs peuvent aussi sélectionner leur
pion et choisir le mode de jeu, seul contre l'ordinateur ou contre un autre joueur.
Si on joue contre l'ordinateur alors on peut aussi choisir la force de l'ordinateur. """

from tkinter import Tk, Canvas, Label, Entry, Radiobutton, IntVar, N, E, W, S, SE, \
    messagebox,CENTER, PhotoImage, Button, END, Frame, SUNKEN
from modules.ModulesPerso import separateur, centreFen
from interface.jeu_utictactoe import Fenetre


class fen_info(Tk):
    """ Fenêtre permettant de saisir les informations sur les joueurs
    """

    def __init__(self):

        super().__init__()
        # Initialisation des pions à la valeur initiale.
        self.pion1 = "X"
        self.pion2 = "O"

        # Titre de la fenêtre
        self.title("Ultimate TIC-TAC-TOE")

        # Pour changer taille minimum de fenêtre et taille centrer,
        # changer variable self.width_fen, self.height_fen.
        self.width_fen, self.height_fen = 430, 500

        # Taille minimum de la fenêtre
        self.minsize(self.width_fen, self.height_fen)

        # Centrer la fenêtre.
        centreFen(self, self.width_fen, self.height_fen)

        # Création d'un canvas avec l'image "logo.gif"
        canvas = Canvas(self, width=280, height=100)
        self.img = PhotoImage(file="interface\logo.gif")
        canvas.create_image(280, 100, anchor=SE, image=self.img)
        canvas.grid(row=0, columnspan=5, pady=10)

        # Libellé - Nouvelle Partie
        Label(self, text="Nouvelle partie", font=("Arial", 16), fg="#0080FF", justify=CENTER).grid(
            row=1, columnspan=5, padx = 20, pady = 5)
        separateur(20).grid(row=10,columnspan=5)

        # Sélection du type de partie avec bouton radio
        self.choixJoueur = IntVar()
        r1 = Radiobutton(self, text="Jouer avec l'ordinateur",
                         variable = self.choixJoueur, value = 1, command=self.define_choix)
        r1.select()
        r1.grid(row=20, column=0)
        r2 = Radiobutton(self, text="Jouer avec un autre joueur",
                         variable = self.choixJoueur, value = 2, command=self.define_choix)
        r2.grid(row=20, column=1)

        # Saisie du nom du joueur 1.
        f_j1 = Frame(self, borderwidth=1, padx=5, pady=5, relief=SUNKEN)
        f_j1.grid(row=30, columnspan=5, padx=5, pady=5)
        Label(f_j1, text="Nom joueur 1:").grid(row=1, column=0, sticky=E, padx = 5, pady = 5)
        self.nom_joueur1 = Entry(f_j1)
        self.nom_joueur1.grid(row=1,column=1)

        # Sélection du pion joueur 1. Le pion restant est automatiquement attribué au joueur 2.

        Label(f_j1, text="Choix de pion:").grid(row=1, column=2, padx=5)
        self.sel_pion=IntVar()
        p1 = Radiobutton(f_j1, indicatoron=0, width=5, text="X",
                         variable=self.sel_pion, value=1, command=self.choix_pion)
        p1.grid(row=1, column=3, padx=2)
        p1.select()
        Radiobutton(f_j1, indicatoron=0, width=5, text="O", variable=self.sel_pion, value=2,
                    command=self.choix_pion).grid(row=1, column=4, padx=2)

        # Saisie du nom du joueur 2. Apparaît seulement si on sélection 2 joueurs. Voir define_choix
        self.f_j2 = Frame(self, width=420, borderwidth=1, padx=5, pady=5, relief=SUNKEN)
        Label(self.f_j2, text="Nom joueur 2").grid(row=1, column=0, sticky=E, padx = 5, pady = 5)
        self.nom_joueur2 = Entry(self.f_j2, state="disabled")
        self.nom_joueur2.grid(row=1, column=1)
        self.label_pion2 = Label(self.f_j2, text="Pion Joueur 2 = O")
        self.label_pion2.grid(row=1, column=2, padx=5)

        # Information sur l'ordinateur. Disparaît si on choisi 2 joueurs.
        self.f_ordi = Frame(self, width=420, borderwidth=1, padx=5, pady=5, relief=SUNKEN)
        self.f_ordi.grid(row=40, columnspan=5, padx=5, pady=5)
        Label(self.f_ordi, text="Ordinateur = Colosse", font=("Arial", 12), fg="#0080FF")\
            .grid(row=1, column=0, sticky=E, padx = 5, pady = 5)
        self.pion_ordi = Label(self.f_ordi, text="| Pion de l'ordinateur = O",
                               font=("Arial", 12), fg="#0080FF")
        self.pion_ordi.grid(row=1, column=2)
        separateur(20).grid(row=50,columnspan=5)

        # Sélection de la force de l'ordinateur
        self.choixForce = IntVar()
        self.f1 = Radiobutton(self, indicatoron=0, width = 20,
                         padx = 20, text="Facile", variable=self.choixForce, value=1, command=self.define_choix)
        self.f1.select()
        self.f1.grid(row=60, columnspan=5)
        self.f2 = Radiobutton(self, indicatoron=0, width = 20,
                         padx = 20, text="Moyen", variable=self.choixForce, value=2, command=self.define_choix)
        self.f2.grid(row=61, columnspan=5)
        self.f3 = Radiobutton(self, indicatoron=0, width = 20,
                         padx = 20, text="Difficile", variable=self.choixForce, value=3, command=self.define_choix)
        self.f3.grid(row=62, columnspan=5)
        separateur(40).grid(row=70, column=0)

        #Button pour démarrer la partie
        self.bt_start = Button(text="Démarrer", font=("Arial", 12), fg="green", command=self.demarrer_jeu)
        self.bt_start.grid(row=80, columnspan=5)

    def define_choix(self):

        """
            Fonction qui active ou désactive le nom du joueur 2 selon si on joue contre l'ordinateur ou contre
            un autre joueur
        """

        if self.choixJoueur.get()==1:
            self.nom_joueur2.delete(0, END)
            self.nom_joueur2["state"]="disabled"
            self.f1["state"]="normal"
            self.f2["state"]="normal"
            self.f3["state"]="normal"
            self.f_j2.grid_remove()
            self.f_ordi.grid(row=40, columnspan=5, padx=5, pady=5)

        elif self.choixJoueur.get()==2:
            self.nom_joueur2["state"]="normal"
            self.f1["state"]="disabled"
            self.f2["state"]="disabled"
            self.f3["state"]="disabled"
            self.f_j2.grid(row=40, columnspan=5, padx=5, pady=5)
            self.f_ordi.grid_remove()

    def choix_pion(self):
        # Définition des pions

        if self.sel_pion.get()==1:
            self.pion1="X"
            self.pion2="O"
            self.label_pion2["text"]="Pion Joueur 2 = {}".format(self.pion2)
            self.pion_ordi["text"]="| Pion de l'ordinateur = {}".format(self.pion2)
        else:
            self.pion1="O"
            self.pion2="X"
            self.label_pion2["text"]="Pion Joueur 2 = {}".format(self.pion2)
            self.pion_ordi["text"]="| Pion de l'ordinateur = {}".format(self.pion2)

    def demarrer_jeu(self):
        """
        Démarrer la partie avec les informations saisie. Afficher le plateau
        """
        if self.choixJoueur.get()==1:
            type2 = "Ordinateur"
            if self.nom_joueur1.get()!='':
                j1 = self.nom_joueur1.get()
                j2 = "Colosse"
            else:
                j1 = "Joueur 1"
                j2 = "Colosse"
        elif self.choixJoueur.get()==2:
            type2 = "Personne"
            if self.nom_joueur1.get()!='' and self.nom_joueur2.get()!='':
                j1 = self.nom_joueur1.get()
                j2 = self.nom_joueur2.get()
            elif self.nom_joueur1.get()=='':
                j1 = "Joueur 1"
                if self.nom_joueur2.get()=='':
                    j2 = "Joueur 2"
                else:
                    j2 = self.nom_joueur2.get()
            else:
                j1 = self.nom_joueur1.get()
                if self.nom_joueur2.get()=='':
                    j2 = "Joueur 2"
                else:
                    j2 = self.nom_joueur2.get()

        p1 = self.pion1
        p2 = self.pion2
        force = self.choixForce.get()
        self.destroy()
        ma_fenetre = Fenetre(j1, j2, type2, p1, p2, force)
        ma_fenetre.mainloop()



if __name__ == '__main__':

    fen = fen_info
    fen.mainloop()



