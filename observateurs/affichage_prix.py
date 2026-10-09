import tkinter as tk
from observateurs.observateur import Observateur

class AffichagePrix(Observateur):

    def __init__(self, parent):
        self._labels = {}
        self._frames = {}
        self._frame = tk.LabelFrame(parent, text="Prix en temps réel", padx=10, pady=10)
        self._frame.pack(fill=tk.X, padx=10, pady=5)

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()
        for ticker in donnees:
            self._afficher_prix(
                ticker,
                donnees[ticker]["prix"],
                donnees[ticker]["ouverture"]
            )
