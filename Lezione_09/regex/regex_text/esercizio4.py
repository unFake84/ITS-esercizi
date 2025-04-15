'''
4. CAP e codici

Obiettivo: Lavorare con lunghezze fisse e caratteri misti.

    Esercizio 4.1: Definisci una RegEx per un CAP italiano (esattamente 5 cifre).
    Esercizio 4.2: Scrivi una RegEx che riconosca un codice fiscale italiano semplificato: 6 lettere, 2 numeri, 1 lettera, 2 numeri.

Svolgimento:

    Esercizio 4.1:

        ^(\d{5})$

    Esercizio 4.2:

        ^[A-Z]{6}\d{2}A-Z\d{2}$

    
        
    Codice fiscale normale: ^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$


'''