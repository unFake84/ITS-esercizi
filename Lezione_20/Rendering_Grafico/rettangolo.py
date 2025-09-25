'''
Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo,
ed impostare il nome della forma su "Rettangolo".
Il metodo getArea() deve calcolare l'area del rettangolo.
Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore.
Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro.
(Vedi Esempio di output)

Ecco un Rettangolo avente base 8 ed altezza 4!
* * * * * * * *
*             *
*             *
* * * * * * * *
L'area di questo rettangolo vale: 32

'''

from forma import Forma

class Rettangolo(Forma):

    _lunghezza: int|float
    _altezza: int|float

    def __init__(self, lunghezza: int|float, altezza: int|float, nome_forma: str = "Rettangolo") -> None:
        super().__init__(nome_forma)

        self._lunghezza = None
        self._altezza = None
        self.lunghezza = lunghezza
        self.altezza = altezza

    def getArea(self) -> float:
        return self.lunghezza * self.altezza

    def render(self) -> None:
        if self.lunghezza is not None and self.altezza is not None:
            spazi_bianchi: int = int(round(self.lunghezza - 2))

            print(f"Ecco un Rettangolo avente base {self.lunghezza} ed altezza {self.altezza}!")
            print('* ' * round(self.lunghezza))
            for riga_colonna in range(round(self.altezza) - 2):

                print('* ' + '  '*spazi_bianchi + '*')

            print('* ' * round(self.lunghezza))
            area: int|float = round(self.getArea()) if self.getArea()%1 == 0 else self.getArea()
            print(f"L'area di questo rettangolo vale: {area}")

    @property
    def lunghezza(self) -> int|float:
        return self._lunghezza

    @lunghezza.setter
    def lunghezza(self, lunghezza: int|float) -> None:
        if isinstance(lunghezza, int|float) and lunghezza >= 1.5 and (self.altezza is None or abs(lunghezza - self.altezza) >= 0.5):

            self._lunghezza = lunghezza

        elif lunghezza < 1.5:
            raise ValueError("Per un Rettangolo la lunghezza minima è 1.5!")

        elif abs(lunghezza - self.altezza) < 0.5:
            raise ValueError("Deve essere un rettangolo!Aumenta o diminuisci di almeno 0.5!")

        else:
            raise ValueError(f"Non è un numero: >>{lunghezza}<<")

    @property
    def altezza(self) -> int|float:
        return self._altezza

    @altezza.setter
    def altezza(self, altezza: int|float) -> None:
        if isinstance(altezza, int|float) and altezza > 1.5 and (self.lunghezza is None or abs(altezza - self.lunghezza) >= 0.5):

            self._altezza = altezza

        elif altezza < 1.5:
            raise ValueError("Per un Rettangolo l'altezza minima è 1.5!")

        elif abs(altezza - self.lunghezza) < 0.5:
            raise ValueError("Deve essere un rettangolo! aumenta o diminuisci di almeno 0.5!")

        else:
            raise ValueError(f"Non è un numero: >>{altezza}<<")

if __name__ == "__main__":

    try:
        r1: Rettangolo = Rettangolo(8, 4)
        r1.render()

    except ValueError as err:
        print("EXCEPTIONS:")
        print(f">>{err}")