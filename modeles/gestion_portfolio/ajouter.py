class Ajouter:

    def ajouter(self, portfolio, titre):
        if titre.ticker in portfolio._titres:
            raise ValueError("Ce titre est déjà dans le portfolio.")

        portfolio._titres[titre.ticker] = titre