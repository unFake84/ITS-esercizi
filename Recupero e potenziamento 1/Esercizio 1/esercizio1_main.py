'''
Esercizio 1.

[A] -------------------------------------------------------------------------------------------------------------

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

[B] -------------------------------------------------------------------------------------------------------------

Il Massimo Comun Divisore di due o più numeri è il più grande divisore comune dei numeri considerati.
Ad esempio, se consideriamo i numeri 12 e 18, il loro Massimo Comun Divisore è mcd(12,18) = 6.

Infatti,

    i divisori di 12 sono:

        12 = 1, 2, 3, 4, 6, 12

    i divisori di 18 sono:

        18 = 1, 2, 3, 6, 9, 18

il divisore più grande che 12 e 18 hanno in comune è 6.

Scrivere nel file frazione.py una funzione  mcd(int x, int y) per il calcolo del Massimo Comune Divisore.

Nel caso in cui esista un Massimo Comun Divisore tra i numeri x e y,
allora la funzione deve ritornarlo come numero intero.
Altrimenti, nel caso in cui non esista un massimo Comun Divisore tra i numeri x e y,
la funzione deve ritornare 1.

Suggerimento: per semplicità, per implementare la funzione richiesta,
trovare una soluzione che generalizzi l'esempio proposto e che tenga conto dei casi x > y e x < y
per evitare di replicare righe di codice.

[C] -------------------------------------------------------------------------------------------------------------

Una frazione si dice irriducibile se il numeratore e il denominatore non hanno divisori comuni,
ovvero il più grande divisore comune tra numeratore e denominatore è 1.

Sia 'l' una lista di frazioni, ovvero una lista di oggetti della classe Frazione.

Si scriva nel file frazioni.py una funzione chiamata semplifica() che data in input una lista di frazioni
ritorni in output una lista di frazioni irriducibili.

Nello specifico:

    se una frazione f della lista data in input è già irriducibile,
    allora inserire questa frazione f nella lista da ritornare in output. 

    se una frazione f della lista data in input può essere semplificata,
    in una frazione irriducibile f1, allora si deve prima semplicare la frazione f,
    ottenendo la frazione irriducibile f1 e poi inserire f1 nella lista da ritornare in output.

Suggerimento: Leggere bene la traccia dell'intero esercizio per capire come implementare la funzione semplifica.
Inserire in modo adeguato le seguenti frazioni nella lista l.

[D] -------------------------------------------------------------------------------------------------------------

Scrivere in Python una funzione chiamata fractionCompare() che prende in input
la lista di frazioni 'l' originale e
la lista con le frazioni di 'l' semplificata.

Usando il metodo value(), dimostrare che il valore di ogni funzione
di entrambe le liste non cambia, stampandolo in output.

Esempio:

    Valore frazione originale: 0.538 --- Valore frazione ridotta: 0.538

[E] -------------------------------------------------------------------------------------------------------------

Scrivere un codice Python che inizializzi la seguente lista l di frazioni,
dove ogni frazione è un oggetto della classe Frazione:

l = 2.5/0,   1/2,   2/4,   3/5,   6/9,   4/7,   24/36,   12/36,   40/60,   5/11,   10/45,   42/78,   9/15

Sfruttando la funzione semplifica,
generare una nuova lista chiamata l_s, contente una versione semplificata delle frazioni della lista l.
Infine, richiamando la funzione fractionCompare,
dimostrare che le funzioni delle lista l e l_s sono equivalenti, ovvero hanno lo stesso valore.
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

# [B]
def mcd(x: int, y: int) -> int:

    numero_maggiore: int = max(x, y)

    while numero_maggiore >= 1:

        if x%numero_maggiore == 0 and y%numero_maggiore == 0:
            return numero_maggiore
        numero_maggiore -= 1

    else:
        return 1

# [C]
def semplifica(f: list[list[int]]) -> list[list[int]]:

    lista_irriducibili: list[list[int]] = []

    for frazione in f:

        divisore: int = mcd(frazione[0], frazione[1])

        if divisore == 1:
            lista_irriducibili.append([frazione[0], frazione[1]])

        elif divisore > 1:
            numeratore: int = frazione[0] // divisore
            denominatore: int = frazione[1] // divisore
            lista_irriducibili.append([numeratore, denominatore])

    return lista_irriducibili

# [D]
def fractionCompare(l: list[list[int]]) -> str:

    f: list[int] = semplifica(l)
    stampaConfronti: str = ""
    stringaLunga: str = ""

    for i in range(len(l)):

        risultato_normale: Frazione = Frazione(l[i][0], l[i][1]).value()
        risultato_semplificato: Frazione = Frazione(f[i][0], f[i][1]).value()

        stringaLunga = f"Valore frazione originale {l[i][0]}/{l[i][1]}: {risultato_normale} --- "\
                        f"Valore frazione ridotta {f[i][0]}/{f[i][1]}: {risultato_semplificato}\n"

        stampaConfronti += stringaLunga

    return stampaConfronti

# [E]
if __name__ == "__main__":

    frazione1: Frazione = Frazione(2.5, 0)
    frazione2: Frazione = Frazione(1, 2)
    frazione3: Frazione = Frazione(2, 4)
    frazione4: Frazione = Frazione(3, 5)
    frazione5: Frazione = Frazione(6, 9)
    frazione6: Frazione = Frazione(4, 7)
    frazione7: Frazione = Frazione(24, 36)
    frazione8: Frazione = Frazione(12, 36)
    frazione9: Frazione = Frazione(40, 60)
    frazione10: Frazione = Frazione(5, 11)
    frazione11: Frazione = Frazione(10, 45)
    frazione12: Frazione = Frazione(42, 78)
    frazione13: Frazione = Frazione(9, 15)

    l: list[Frazione] = [
        frazione1,
        frazione2,
        frazione3,
        frazione4,
        frazione5,
        frazione6,
        frazione7,
        frazione8,
        frazione9,
        frazione10,
        frazione11,
        frazione12,
        frazione13
        ]

    l_s: list[list[int]] = [[f.get_numeratore(), f.get_denominatore()] for f in l]

    print("Lista originale: \n", *[str(f)+"\n" for f in l])
    print("Lista semplificata \n", *[str(g[0])+" / "+str(g[1])+"\n" for g in semplifica(l_s)])
    print("Comparazioni: ")
    print(fractionCompare(l_s))