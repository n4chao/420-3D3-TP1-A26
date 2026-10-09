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

    def retirer(self, ticker):
        self._retrait.retirer(self, ticker)

    def modifier(self, ticker, quantite=None, seuil_bas=None, seuil_haut=None):
        self._modification.modifier(
            self, ticker, quantite, seuil_bas, seuil_haut
        )

    def obtenir_titres(self):
        return self._titres

    def rafraichir_prix(self):
        for ticker in self._titres:
            self._prix[ticker] = self._strategie.recuperer_prix(ticker)

        self.notifier()

    def get_donnees(self):
        return {
            "titres": self._titres,
            "prix": self._prix
        }