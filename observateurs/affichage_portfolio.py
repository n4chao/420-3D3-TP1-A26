# observateurs/affichage_portfolio.py
import tkinter as tk
from observateurs.observateur import Observateur


class AffichagePortfolio(Observateur):

    def __init__(self, parent: tk.Misc) -> None:
        self.frame_portfolio = tk.LabelFrame(parent, text="Mon portfolio", padx=10, pady=10)
        self.frame_portfolio.pack(fill=tk.X, padx=10, pady=5)
        self.label_valeur = tk.Label(
        self.frame_portfolio, text="Valeur totale : calcul en cours...",
        font=("Segoe UI", 13, "bold")
        )
        self.label_valeur.pack()
        self.label_variation = tk.Label(self.frame_portfolio, text="")
        self.label_variation.pack()

    def actualiser(self, sujet) -> None:

        donnees = sujet.get_donnees()
        valeur = donnees["valeur_totale"]
        variation = donnees["variation_valeur"]


        if valeur is None:
            self._afficher_attente()
            return

        self._afficher_valeur(valeur)
        self._afficher_variation(variation)

    def _afficher_attente(self) -> None:
        self.label_valeur.config(text="Valeur totale : calcul en cours...")
        self.label_variation.config(text="")

    def _afficher_valeur(self, valeur: float) -> None:
        self.label_valeur.config(text=f"Valeur totale : {valeur:.2f} $")

    def _afficher_variation(self, variation: float) -> None:
        if variation >= 0:
            symbole = "▲"
            couleur = "green"
        else:
            symbole = "▼"
            couleur = "red"
        self.label_variation.config(
            text=f"{symbole} {abs(variation):.2f} $ depuis l'ouverture", fg=couleur
        )