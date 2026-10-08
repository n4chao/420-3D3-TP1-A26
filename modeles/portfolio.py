from modeles.sujet import Sujet

class Portfolio(Sujet):

    def __init__(self, strategie):
        super().__init__()
        self._titres = {}
        self._prix = {}
        self._strategie = strategie

    def actualiser_prix(self):
        for ticker in self._titres:
            self._prix[ticker] = self._strategie.recuperer_prix(ticker)

        self.notifier()

    def get_donnees(self):
        return {
            "titres": self._titres,
            "prix": self._prix
        }