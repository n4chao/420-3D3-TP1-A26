import tkinter as tk
from observateurs.observateur import Observateur


class AffichagePrix(Observateur):

    def __init__(self, parent):
        self._labels = {}
        self._frames = {}

        self._frame = tk.LabelFrame(
            parent,
            text="Prix en temps réel",
            padx=10,
            pady=10
        )
        self._frame.pack(fill=tk.X, padx=10, pady=5)

    def ajouter_ligne(self, ticker, prix=None, ouverture=None):
        if ticker not in self._labels:
            frame = tk.Frame(self._frame)
            frame.pack(fill=tk.X, pady=2)

            tk.Label(
                frame,
                text=ticker + ":",
                width=8,
                anchor="w"
            ).pack(side=tk.LEFT)

            label = tk.Label(frame, text="Chargement...")
            label.pack(side=tk.LEFT)

            self._labels[ticker] = label
            self._frames[ticker] = frame

        self._afficher_prix(ticker, prix, ouverture)

    def retirer_ligne(self, ticker):
        if ticker in self._frames:
            self._frames[ticker].destroy()
            del self._frames[ticker]
            del self._labels[ticker]

    def _afficher_prix(self, ticker, prix, ouverture):
        if ticker not in self._labels:
            self.ajouter_ligne(ticker, prix, ouverture)
            return

        if prix is None or ouverture is None:
            self._labels[ticker].config(
                text="Prix indisponible",
                fg="gray"
            )
            return

        if ouverture == 0:
            self._labels[ticker].config(
                text=f"{prix:.2f} $",
                fg="gray"
            )
            return

        variation = (prix - ouverture) / ouverture * 100

        if variation >= 0:
            symbole = "▲"
            couleur = "green"
        else:
            symbole = "▼"
            couleur = "red"

        texte = f"{prix:.2f} $  {symbole} {abs(variation):.2f}%"

        self._labels[ticker].config(
            text=texte,
            fg=couleur
        )

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()

        for ticker in donnees:
            self._afficher_prix(
                ticker,
                donnees[ticker]["prix"],
                donnees[ticker]["ouverture"]
            )
