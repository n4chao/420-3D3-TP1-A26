import tkinter as tk
from observateurs.observateur import Observateur

class AffichagePortfolio(Observateur):

    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="Mon portfolio", padx=10, pady=10)
        frame.pack(fill=tk.X, padx=10, pady=5)
        self._valeur = tk.Label(frame, text="Valeur totale : calcul en cours...", font=("Segoe UI", 13, "bold"))
        self._valeur.pack()
        self._variation = tk.Label(frame, text="")
        self._variation.pack()

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()
        valeur = 0
        ouverture = 0
        for ticker in donnees:
            prix = donnees[ticker]["prix"]
            prix_ouverture = donnees[ticker]["ouverture"]
            quantite = donnees[ticker]["quantite"]
            if prix is not None and prix_ouverture is not None:
                valeur += prix * quantite
                ouverture += prix_ouverture * quantite

        variation = valeur - ouverture
        symbole = "▲" if variation >= 0 else "▼"
        couleur = "green" if variation >= 0 else "red"
        self._valeur.config(text=f"Valeur totale : {valeur:.2f} $")
        self._variation.config(text=f"{symbole} {abs(variation):.2f} $ depuis l'ouverture", fg=couleur)
