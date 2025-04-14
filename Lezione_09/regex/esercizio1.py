'''

1. Riconoscere numeri

Obiettivo: Definire una RegEx che riconosca solo stringhe composte da cifre.

    Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
    Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).

Svolgimento:

    Esercizio 1.1:

        ^\d+$

    Esercizio 1.2:

        ^-\d+$|^\d+$     ---> soluzione + pratica ^-?\d+$

'''