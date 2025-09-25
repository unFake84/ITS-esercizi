'''
Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore.
Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro.
(Vedi Esempio di output)
'''

from forma import Forma

class Quadrato(Forma):

    _lato: int|float

    def __init__(self, lato: int|float, nome_forma: str = "Quadrato") -> None:
        super().__init__(nome_forma)

        self.lato = lato
    
    def getArea(self) -> float:
        pass

    def render(self) -> None:
        pass

    @property
    def lato(self) -> int|float:
        return self._lato

    @lato.setter
    def lato(self, lato: int|float) -> None:
        if isinstance(lato, int|float) and lato >= 0:

            self._lato = lato

        else:
            raise ValueError("Il lato del quadrato deve essere maggiore di 0")