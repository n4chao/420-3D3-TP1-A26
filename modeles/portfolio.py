from modeles.sujet import Sujet
from modeles.gestion_portfolio.ajouter import Ajouter
from modeles.gestion_portfolio.retirer import Retirer
from modeles.gestion_portfolio.modifier import Modifier


class Portfolio(Sujet):

    def __init__(self, strategie):
        super().__init__()

        self._titres = {}
        self._prix = {}
        self._strategie = strategie

        self._ajout = Ajouter()
        self._retrait = Retirer()
        self._modification = Modifier()

    def ajouter(self, titre):
        self._ajout.ajouter(self, titre)
        self.notifier()

    def retirer(self, ticker):
        self._retrait.retirer(self, ticker)
        self.notifier()

    def modifier(self, ticker, quantite=None,
                 seuil_bas=None, seuil_haut=None):

        self._modification.modifier(
            self, ticker, quantite, seuil_bas, seuil_haut
        )

        self.notifier()

    def obtenir_titres(self):
        return self._titres

    def rafraichir_prix(self):
        for ticker in self._titres:
            try:
                self._prix[ticker] = self._strategie.recuperer_prix(ticker)
            except Exception:
                # Garder le dernier prix connu si le réseau échoue.
                if ticker not in self._prix:
                    self._prix[ticker] = {
                        "prix": None,
                        "ouverture": None
                    }

        self.notifier()

    def get_donnees(self):
        donnees = {}

        for ticker in self._titres:
            titre = self._titres[ticker]

            if ticker in self._prix:
                prix = self._prix[ticker]
            else:
                prix = {
                    "prix": None,
                    "ouverture": None
                }

            donnees[ticker] = {
                "quantite": titre.quantite,
                "seuil_bas": titre.seuil_bas,
                "seuil_haut": titre.seuil_haut,
                "prix": prix["prix"],
                "ouverture": prix["ouverture"]
            }

        return donnees

