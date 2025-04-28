from abc import ABC, abstractmethod

class FormaGenerica(ABC):

    @abstractmethod # decorator(un), indica che è un metodo astratto
    def draw(self) -> None:

        pass

    def setShape(self, shape: str) -> None:

        if shape:

            self.shape = shape

        else:

            print("Shape cannot be an empty string")

    def getShape(self) -> str:

        return self.shape