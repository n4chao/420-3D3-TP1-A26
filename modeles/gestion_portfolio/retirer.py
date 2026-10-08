from modeles.portfolio import Portfolio

class Retirer:

    def retirer(self, portfolio, ticker):
        if ticker in portfolio._titres:
            del portfolio._titres[ticker]

        if ticker in portfolio._prix:
            del portfolio._prix[ticker]