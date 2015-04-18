__author__ = 'IFT-1004-H2015'
__date__ = "12 mars 2015"

""" Ce fichier  permet de débuter une partie de tic-tac-toe ultime. Le début de la partie ce fait
avec la fenêtre qui permet de saisir les informations sur les joueurs. Les joueurs peuvent aussi sélectionner leur
pion et choisir le mode de jeu, seul contre l'ordinateur ou contre un autre joueur.
Si on joue contre l'ordinateur alors on peut aussi choisir la force de l'ordinateur. """

from tkinter import Tk, Canvas, Label, Entry, Radiobutton, IntVar, N, E, W, S, SE, \
    messagebox,CENTER, PhotoImage, Button
from modules.ModulesPerso import separateur, centreFen
from interface.jeu_utictactoe import Fenetre


class fen_info(Tk):
    """ Fenêtre permettant de saisir les informations sur les joueurs
    """

    def __init__(self):

        super().__init__()

        # Titre de la fenêtre
        self.title("Ultimate TIC-TAC-TOE")

        # Pour changer taille minimum de fenêtre et taille centrer,
        # changer variable self.width_fen, self.height_fen.
        self.width_fen, self.height_fen = 315, 450

        # Taille minimum de la fenêtre
        self.minsize(self.width_fen, self.height_fen)

        # Centrer la fenêtre.
        centreFen(self, self.width_fen, self.height_fen)

        # Création d'un canvas avec l'image "logo.gif"
        canvas = Canvas(self, width=280, height=100)
        self.img = PhotoImage(file="interface\logo.gif")
        canvas.create_image(280,100, anchor=SE, image=self.img)
        canvas.grid(row=0, columnspan=2, pady=10)

        # Libellé - Nouvelle Partie
        Label(self, text="Nouvelle partie", font=("Arial", 16), fg="#0080FF", justify=CENTER).grid(
            row=1, columnspan=2, padx = 20, pady = 5)
        separateur(20).grid(row=10,column=0)

        # Sélection du type de partie avec bouton radio
        self.choixJoueur = IntVar()
        r1 = Radiobutton(self, text="Jouer avec l'ordinateur",
                         variable = self.choixJoueur, value = 1, command=self.define_choix)
        r1.select()
        r1.grid(row=20, column=0)
        r2 = Radiobutton(self, text="Jouer avec un autre joueur",
                         variable = self.choixJoueur, value = 2, command=self.define_choix)
        r2.grid(row=20, column=1)

        # Champs pour saisie des noms de joueurs
        Label(self, text="Saisir le nom du joueur 1").grid(row=30, column=0, sticky=E, padx = 5, pady = 5)
        self.nom_joueur1 = Entry(self)
        self.nom_joueur1.grid(row=30, column=1)
        Label(self, text="Saisir le nom du joueur 2").grid(row=40, column=0, sticky=E, padx = 5, pady = 5)
        self.nom_joueur2 = Entry(self, state="disabled")
        self.nom_joueur2.grid(row=40, column=1)
        separateur(20).grid(row=50,column=0)

        # Sélection de la force de l'ordinateur
        self.choixForce = IntVar()
        self.f1 = Radiobutton(self, indicatoron=0, width = 20,
                         padx = 20, text="Facile", variable=self.choixForce, value=1, command=self.define_choix)
        self.f1.select()
        self.f2 = Radiobutton(self, indicatoron=0, width = 20,
                         padx = 20, text="Moyen", variable=self.choixForce, value=2, command=self.define_choix)
        self.f3 = Radiobutton(self, indicatoron=0, width = 20,
                         padx = 20, text="Difficile", variable=self.choixForce, value=3, command=self.define_choix)
        self.f1.grid(row=60, columnspan=2)
        self.f2.grid(row=61, columnspan=2)
        self.f3.grid(row=62, columnspan=2)
        separateur(20).grid(row=70, column=0)

        #Button pour démarrer la partie
        Button(text="Démarrer", command=self.demarrer_jeu).grid(row=80, columnspan=2)

    def define_choix(self):

        """
            Fonction qui active ou désactive le nom du joueur 2 selon si on joue contre l'ordinateur ou contre
            un autre joueur
        """

        if self.choixJoueur.get()==1:
            self.nom_joueur2["state"]="disabled"
            self.f1["state"]="normal"
            self.f2["state"]="normal"
            self.f3["state"]="normal"
        elif self.choixJoueur.get()==2:
            self.nom_joueur2["state"]="normal"
            self.f1["state"]="disabled"
            self.f2["state"]="disabled"
            self.f3["state"]="disabled"
        #messagebox.showinfo("Test", str(self.choixJoueur.get()))

    def demarrer_jeu(self):
        self.destroy()
        ma_fenetre = Fenetre()
        ma_fenetre.mainloop()

if __name__ == '__main__':

    fen = fen_info

    fen.mainloop()



