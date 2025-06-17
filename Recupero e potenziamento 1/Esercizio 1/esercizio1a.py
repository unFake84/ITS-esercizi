'''
Si Scriva in Python in un file frazioni.py una classe Frazione,
i cui attributi privati siano rispettivamente numeratore e denominatore.

Si definiscano i metodi __init__, setter, getter, __str__, value.

In particolare:

    il metodo value(), deve restituire il valore della frazione,
    ovvero numeratore / denominatore arrotondato a 3 cifre decimali;

    il metodo __str__ deve mostare in output la frazione
    nel seguente modo: "numeratore / denominatore ";
    i metodi setter devono controllare che il valore inserito sia un intero,
    in caso contrario il numeratore ed il denominatore devono essere impostati
    per default rispettivamente a 13 e 5.
    Inoltre, il metodo setter relativo al denominatore deve assicurarsi che
    questo non sia mai uguale a 0.
    Nel caso in cui il denominatore passato sia 0, impostarlo per default a 5.

Suggerimento: per verificare che il numeratore ed il denominatore siano numeri interi, usare la funzione is_integer().
'''

# [A]
class Frazione:

    _numeratore: int
    _denominatore: int

    def __init__(self, numeratore: int, denominatore: int) -> None:
        if not isinstance(numeratore, int):
            numeratore = 13

        if not isinstance(denominatore, int) or denominatore == 0:
            denominatore = 5

        self._numeratore = numeratore
        self._denominatore = denominatore            

    def __str__(self):
        return f"{self._numeratore} / {self._denominatore}"
    
    def __repr__(self):
        return self.__str__()

    def set_numeratore(self, new_num: int = 13) -> None:
        if not isinstance(new_num, int):
            self._numeratore = 13

        else:
            self._numeratore = new_num

    def get_numeratore(self) -> int:
        return self._numeratore

    def set_denominatore(self, new_den: int = 5) -> None:
        if not isinstance(new_den, int) or new_den == 0:
            self._denominatore = 5

        else:
            self._denominatore = new_den

    def get_denominatore(self) -> int:
        return self._denominatore
    
    def value(self) -> float:
        return round(self.get_numeratore() / self.get_denominatore(), 3)

if __name__ == "__main__":

    i_frazione: Frazione = Frazione(1, 1)
    i_frazione.set_numeratore(20)
    i_frazione.set_denominatore(90)
    print(i_frazione.value())