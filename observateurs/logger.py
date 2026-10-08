from datetime import datetime
from observateurs.observateur import Observateur


class Logger(Observateur):

    def __init__(self, fichier="portfolio.csv"):
        self._fichier = fichier

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()
        horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self._fichier, "a") as fichier:
            for ticker in donnees:
                prix = donnees[ticker]["prix"]
                ouverture = donnees[ticker]["ouverture"]

                if prix is not None and ouverture is not None:
                    ligne = f"{horodatage},{ticker},{prix:.2f},{ouverture:.2f}\n"
                    fichier.write(ligne)