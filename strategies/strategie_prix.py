from abc import ABC, abstractmethod

class StrategiePrix(ABC):

    @abstractmethod
    def recuperer_prix(self, ticker):
        pass
