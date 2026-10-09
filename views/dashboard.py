import tkinter as tk
from datetime import datetime

from observateurs.affichage_prix import AffichagePrix
from observateurs.affichage_portfolio import AffichagePortfolio
from observateurs.alerte_prix import AlertePrix
from observateurs.logger import Logger
from views.gestion_titres import GestionTitres


class Dashboard:

    def __init__(self, portfolio):
        self._portfolio = portfolio

        self._fenetre = tk.Tk()
        self._fenetre.title("Portfolio Tracker")
        self._fenetre.resizable(False, False)
        self._fenetre.option_add("*Font", ("Segoe UI", 10))

        tk.Label(
            self._fenetre,
            text="Portfolio Tracker",
            font=("Segoe UI", 16, "bold")
        ).pack(pady=10)

        self._affichage_prix = AffichagePrix(self._fenetre)

        # Créer une ligne de prix pour chaque titre initial.
        for ticker in portfolio.obtenir_titres():
            self._affichage_prix.ajouter_ligne(ticker)

        GestionTitres(
            self._fenetre,
            portfolio,
            self._affichage_prix
        )

        self._affichage_portfolio = AffichagePortfolio(self._fenetre)
        self._alerte = AlertePrix(self._fenetre)

        self._label_maj = tk.Label(
            self._fenetre,
            text="En attente des prix...",
            font=("Segoe UI", 9),
            fg="gray"
        )
        self._label_maj.pack(pady=5)

        # Enregistrer les observateurs.
        self._portfolio.abonner(self._affichage_prix)
        self._portfolio.abonner(self._affichage_portfolio)
        self._portfolio.abonner(self._alerte)
        self._portfolio.abonner(Logger())

        # Lancer la première actualisation après la création de l'interface.
        self._fenetre.after(100, self.actualiser)

    def actualiser(self):
        try:
            self._portfolio.rafraichir_prix()

            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self._label_maj.config(
                text=f"Dernière mise à jour : {date}",
                fg="gray"
            )

        except Exception as erreur:
            self._label_maj.config(
                text=f"Erreur : {erreur}",
                fg="red"
            )

        # Réessayer après 30 secondes.
        self._fenetre.after(30000, self.actualiser)

    def mainloop(self):
        self._fenetre.mainloop()

