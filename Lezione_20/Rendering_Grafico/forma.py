'''
Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e
le funzionalità base di ogni forma, come i metodi astratti
getArea() per calcolare l'area e
render() per disegnare su schermo la forma.
'''

from abc import ABC, abstractmethod

class Forma(ABC):

    _nome_forma: str

    def __init__(self, nome_forma: str = "Non ancora definita") -> None:
        self._nome_forma = nome_forma

    @abstractmethod
    def getArea(self) -> float:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

    @property
    def nome_forma(self) -> str:
        return self._nome_forma

    @nome_forma.setter
    def nome_forma(self, nome_forma: str) -> None:
        self._nome_forma = nome_forma