'''

3. Email semplici

Obiettivo: Definire pattern per email.

    Esercizio 3.1: Scrivi una RegEx che riconosca email del tipo nome@dominio.com.
    Esercizio 3.2: Estendi la RegEx per accettare anche domini con più estensioni, es. nome@dominio.co.uk.

Svolgimento:

Esercizio 3.1:

    ^\w+@\w+\.[a-z]{2,3}$

Esercizio 3.2:

    ^\w+@\w+(\.[a-z]{2,3})+$

'''