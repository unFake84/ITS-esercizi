'''
Scrivere un codice Python che inizializzi la seguente lista l di frazioni,
dove ogni frazione è un oggetto della classe Frazione:
 
l = 2.5/0,   1/2,   2/4,   3/5,   6/9,   4/7,   24/36,   12/36,   40/60,   5/11,   10/45,   42/78,   9/15
       
Sfruttando la funzione semplifica,
generare una nuova lista chiamata l_s, contente una versione semplificata delle frazioni della lista l.
Infine, richiamando la funzione fractionCompare,
dimostrare che le funzioni delle lista l e l_s sono equivalenti, ovvero hanno lo stesso valore.
'''

from esercizio1a import Frazione
from esercizio1b import mcd
from esercizio1c import semplifica
from esercizio1d import fractionCompare

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

# l_s: list[list[int]] = [[f.get_numeratore(), f.get_denominatore()] for f in l]

# print("Lista originale: \n", *[str(f)+"\n" for f in l])
# print("Lista semplificata \n", *[str(g[0])+" / "+str(g[1])+"\n" for g in semplifica(l_s)])
# print("Comparazioni: ")
# print(fractionCompare(l_s))