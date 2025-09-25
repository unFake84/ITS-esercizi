'''
Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
Il metodo getArea() deve calcolare l'area del quadrato.
Il metodo render() deve stampare su schermo un quadrato avente lato pari al valore passato nel costruttore.
Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro.
(Vedi Esempio di output)
Esempi di output:

Ecco un Quadrato di lato 4!
* * * *
*     *
*     *
* * * *
L'area di questo quadrato vale: 16

'''

from forma import Forma

class Quadrato(Forma):

    _lato: int|float

    def __init__(self, lato: int|float, nome_forma: str = "Quadrato") -> None:
        super().__init__(nome_forma)

        self.lato = lato

    def getArea(self) -> float:
        return self.lato ** 2

    def render(self) -> None:
        spazi_bianchi: int = int(round(self.lato - 2))
        lato_int: int = int(round(self.lato))

        print(f"Ecco un Quadrato di lato {self.lato}!")
        print('* ' * lato_int)
        for riga in range(lato_int - 2):

            print('* ' + '  ' * spazi_bianchi + '*')

        print('* ' * lato_int)
        print(f"L'area di questo quadrato vale: {self.getArea():.2f}")

    @property
    def lato(self) -> int|float:
        return self._lato

    @lato.setter
    def lato(self, lato: int|float) -> None:
        if isinstance(lato, int|float) and lato >= 1.5:

            self._lato = lato

        else:
            raise ValueError("Il lato del quadrato deve essere un numero maggiore di 1.5")

if __name__ == "__main__":

    try:
        q1: Quadrato = Quadrato(4.9)
        q1.render()

    except ValueError as err:
        print("EXCEPTIONS:")
        print(f">>{err}")