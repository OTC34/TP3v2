__author__ = 'IFT-1004-H2015'
__date__ = "05 avril 2015"

"""Ce fichier représente le point d'entrée principal du TP3.
Il ne sert qu'à exécuter votre programme du jeu Ultimate Tic-Tac-Toe"""

from interface.info_joueur import fen_info

if __name__ == '__main__':

    fen = fen_info
    fen().mainloop()