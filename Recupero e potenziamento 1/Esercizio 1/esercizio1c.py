'''
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
'''

from esercizio1a import Frazione
from esercizio1b import mcd

def semplifica(f: list[Frazione]) -> list[Frazione]:

    lista_irriducibili: list[Frazione] = []

    for frazione in f:

        num: int = int(frazione.get_numeratore())
        den: int = int(frazione.get_denominatore())

        divisore: int = mcd(num, den)

        if divisore == 1:
            lista_irriducibili.append(frazione)

        elif divisore > 1:
            numeratore: int = num // divisore
            denominatore: int = den // divisore
            lista_irriducibili.append(Frazione(numeratore, denominatore))

    return lista_irriducibili

if __name__ == "__main__":

    f1: Frazione = Frazione(6, 8)
    f2: Frazione = Frazione(5, 10)
    f3: Frazione = Frazione(7, 3)
    l: list[Frazione] = [f1, f2, f3]

    print(semplifica(l))


















            # lista_irriducibili.append(mcd(numeratore, denominatore))
            # frazione: list[int] = []
            # numero_minore: int = min(numeratore, denominatore)
            # while numero_minore >= 1:
            #     if numeratore%numero_minore == 0 and denominatore%numero_minore == 0:
            #         numeratore_semplif: int = numeratore // numero_minore
            #         denominatore_semplif: int = denominatore // numero_minore
            #         frazione.append(numeratore_semplif)
            #         frazione.append(denominatore_semplif)
            #         break
            #     else:
            #         numero_minore -= 1