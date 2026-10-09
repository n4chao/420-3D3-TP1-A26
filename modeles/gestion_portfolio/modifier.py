class Modifier:

    def modifier(self, portfolio, ticker, quantite=None,
                 seuil_bas=None, seuil_haut=None):

        if ticker not in portfolio._titres:
            raise ValueError("Ce titre n'existe pas dans le portfolio.")

        titre = portfolio._titres[ticker]

        if quantite is not None:
            titre.quantite = quantite

        if seuil_bas is not None:
            titre.seuil_bas = seuil_bas

        if seuil_haut is not None:
            titre.seuil_haut = seuil_haut
