import yfinance as yf
from strategies.strategie_prix import StrategiePrix

class PrixTitre(StrategiePrix):

    def recuperer_prix(self, ticker):
        info = yf.Ticker(ticker).fast_info
        prix = info["last_price"]
        if prix is None:
            raise ValueError("Le titre n'existe pas.")
        return {"prix": prix, "ouverture": info["open"]}
