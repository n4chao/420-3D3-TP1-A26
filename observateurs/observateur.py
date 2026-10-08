from abc import ABC, abstractmethod

class Observateur(ABC):

    @abstractmethod
    def rafraichir(self, sujet) -> None:
        pass