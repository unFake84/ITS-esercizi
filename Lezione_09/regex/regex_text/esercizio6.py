'''

6. Codici personalizzati

Obiettivo: Unire lettere, numeri e caratteri speciali.

    Esercizio 6.1: Scrivi una RegEx per identificare un codice prodotto nel formato PROD-1234-XY.
    Esercizio 6.2: Crea una RegEx per un ID alfanumerico di esattamente 8 caratteri, che può contenere lettere maiuscole e numeri (es. AB12CD34).

Svolgimento:

    Esercizio 6.1:

        ^[A-Z]{4}-\d{4}-[A-Z]{2}$

    Esercizio 6.2:

        ^[A-Z0-9]{8}$

'''