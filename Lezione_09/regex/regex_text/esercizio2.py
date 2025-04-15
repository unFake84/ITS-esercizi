'''

2. Riconoscere parole

Obiettivo: Lavorare con lettere e lunghezze di stringhe.

    Esercizio 2.1: Scrivi una RegEx che riconosca una parola composta solo da lettere minuscole.
    Esercizio 2.2: Adatta la RegEx per accettare parole con lettere maiuscole e minuscole.
    Esercizio 2.3: Modifica la RegEx per accettare parole lunghe da 5 a 10 caratteri.

Svolgimento:

    Esercizio 2.1:
    
        ^[a-z]+$

    Esercizio 2.2:

        ^[a-zA-Z]+$

    Esercizio 2.3:

        ^[a-zA-Z]{5,10}$

'''