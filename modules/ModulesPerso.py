__author__ = 'Éric Laflamme et Olivier-Thierry Cardinal'
__date__ = '15 avril 2015'

"""Fichier contenant les modules de personnalisation ou de configuration des widgets du jeu. """

from tkinter import Frame

class separateur(Frame):

    """Création d'un séparateur esthétique"""

    def __init__(self, height):

        super().__init__()
        self["height"]= height

def centreFen(fen, w=200, h=200):

    assert isinstance(fen, object),"Doit être une classe fenêtre"

    # calculer la grandeur de l'écran

    ws = fen.winfo_screenwidth()
    hs = fen.winfo_screenheight()

    # calcul des positions x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    fen.geometry('%dx%d+%d+%d' % (w, h, x, y))

