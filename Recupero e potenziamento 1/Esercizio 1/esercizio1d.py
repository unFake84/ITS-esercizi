'''
Scrivere in Python una funzione chiamata fractionCompare() che prende in input
la lista di frazioni 'l' originale e
la lista con le frazioni di 'l' semplificata.
 
Usando il metodo value(), dimostrare che il valore di ogni funzione
di entrambe le liste non cambia, stampandolo in output.

Esempio:

    Valore frazione originale: 0.538 --- Valore frazione ridotta: 0.538
'''

from esercizio1a import Frazione
from esercizio1b import mcd
from esercizio1c import semplifica

def fractionCompare(orig: list[Frazione], sempl: list[Frazione]) -> str:

    stampaConfronti: str = ""

    for i in range(len(orig)):

        risultato_normale: float = orig[i].value()
        risultato_semplificato: float = sempl[i].value()
        stampaConfronti += f"Valore frazione originale {orig[i]}: {risultato_normale} --- "\
                        f"Valore frazione ridotta {sempl[i]}: {risultato_semplificato}\n"

    return stampaConfronti

if __name__ == "__main__":

    fr_orig1: Frazione = Frazione(6, 8)
    fr_orig2: Frazione = Frazione(5, 10)
    fr_orig3: Frazione = Frazione(7, 3)
    l_originale: list[Frazione] = [fr_orig1, fr_orig2, fr_orig3]

    fr_sempl1: Frazione = Frazione(3, 4)
    fr_sempl2: Frazione = Frazione(1, 2)
    fr_sempl3: Frazione = Frazione(7, 3)
    l_semplificate: list[Frazione] = [fr_sempl1, fr_sempl2, fr_sempl3]

    print(fractionCompare(l_originale, l_semplificate))


















    # orig: list[str] = [o.value() for o in orig]
    # sempl: list[str] = [s.value() for s in sempl]
    #print(*orig, *sempl)
    #return f"Valore frazione originale: 0.538 --- Valore frazione ridotta: 0.538"
    #return f"{[str(o.value()) for o in orig]}{[str(s.value()) for s in sempl]}"



    # def fractionCompare(l: list[list[int]]) -> str:

#     f: list[int] = semplifica(l)
#     stampaConfronti: str = ""
#     stringaLunga: str = ""

#     for i in range(len(l)):

#         risultato_normale: Frazione = Frazione(l[i][0], l[i][1]).value()
#         risultato_semplificato: Frazione = Frazione(f[i][0], f[i][1]).value()

#         stringaLunga = f"Valore frazione originale {l[i][0]}/{l[i][1]}: {risultato_normale} --- "\
#                         f"Valore frazione ridotta {f[i][0]}/{f[i][1]}: {risultato_semplificato}\n"

#         stampaConfronti += stringaLunga

#     return stampaConfronti





    # stp_normale: str = ""
    # stp_semplificate: str = ""

    #     stp_normale += f"Il risultato normale di {l[i][0]} e {l[i][1]} è {risultato_normale}\n"
    #     stp_semplificate += f"Il risultato semplificato di {f[i][0]} e {f[i][1]} è {risultato_semplificato}\n"

    # return f"{stp_normale}\n{stp_semplificate}"









        #print(risultato_normale, "\n", risultato_semplificato)

        # risultato_normale: Frazione = Frazione(i[0], i[1]).value()
        # stp_normale += f"Il risultato normale di {l[0][0]} e {l[0][1]} è {risultato_normale}."

    # stp_normale = ""
    # for frazione in l:
    #     risultato_normale: Frazione = Frazione(frazione[0], frazione[1]).value()
    #     stp_normale += f"Il risultato normale di {frazione[0]} e {frazione[1]} è pari a {risultato_normale}\n"
    #     #risultato_irriducibile: Frazione = 