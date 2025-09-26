'''
Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del triangolo
(per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
Il metodo getArea() deve calcolare l'area del triangolo.
Il metodo render() deve stampare su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai
valori passati nel costruttore.
Il triangolo da stampare deve essere un triangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro.
(Vedi Esempio di output)

Esempio di output:

Ecco un Triangolo avente base 4 ed altezza 4!
*      
**    
* *  
****
L'area di questo triangolo vale: 8.0

'''

from forma import Forma

class Triangolo(Forma):

    _lato: int|float

    def __init__(self, lato: int|float, nome_forma: str = "Triangolo") -> None:
        super().__init__(nome_forma)

        self.lato = lato

    def getArea(self) -> int|float:
        return (self.lato * self.lato) / 2

    def render(self) -> None:
        spazi_bianchi: int = 0
        lato_int: int = int(round(self.lato))

        print(f"Ecco un Triangolo avente base {self.lato:g} ed altezza {self.lato:g}")
        print("*")
        for riga in range(lato_int - 2):

            print('*' + ' ' * (spazi_bianchi) + '*')
            spazi_bianchi += 1

        print('*' * lato_int)
        print(f"L'area di questo triangolo vale: {self.getArea():g}")

    @property
    def lato(self) -> int|float:
        return self._lato

    @lato.setter
    def lato(self, lato: int|float) -> None:
        if isinstance(lato, int|float) and lato >= 1.5:

            self._lato = lato

        elif not isinstance(lato, int|float):
            raise ValueError(f"Non è un numero: >>{lato}<<")

        elif lato < 1.5:
            raise ValueError("Il lato deve essere maggiore o uguale di 1.5")

if __name__ == "__main__":

    try:
        t1: Triangolo = Triangolo(4)
        t1.render()

    except ValueError as err:
        print("EXCEPTIONS:")
        print(f">>{err}")