import tkinter as tk
from observateurs.observateur import Observateur


class AffichagePortfolio(Observateur):

    def __init__(self, parent):
        frame = tk.LabelFrame(
            parent,
            text="Mon portfolio",
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.X, padx=10, pady=5)

        self._valeur = tk.Label(
            frame,
            text="Valeur totale : calcul en cours...",
            font=("Segoe UI", 13, "bold")
        )
        self._valeur.pack()

        self._variation = tk.Label(frame, text="")
        self._variation.pack()

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()

        valeur = 0
        ouverture = 0
        nombre_prix_disponibles = 0

        for ticker in donnees:
            titre = donnees[ticker]

            prix = titre["prix"]
            prix_ouverture = titre["ouverture"]
            quantite = titre["quantite"]

            if prix is not None and prix_ouverture is not None:
                valeur += prix * quantite
                ouverture += prix_ouverture * quantite
                nombre_prix_disponibles += 1

        if nombre_prix_disponibles == 0:
            self._valeur.config(
                text="Valeur totale : prix indisponibles"
            )
            self._variation.config(text="")
            return

        variation = valeur - ouverture

        if variation >= 0:
            symbole = "▲"
            couleur = "green"
        else:
            symbole = "▼"
            couleur = "red"

        self._valeur.config(
            text=f"Valeur totale : {valeur:.2f} $"
        )

        self._variation.config(
            text=f"{symbole} {abs(variation):.2f} $ depuis l'ouverture",
            fg=couleur
        )

