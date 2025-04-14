'''

5. Riconoscere date

Obiettivo: Lavorare con formati numerici separati da caratteri speciali.

    Esercizio 5.1: Scrivi una RegEx che riconosca una data nel formato gg/mm/aaaa (es. 09/04/2025).
    Esercizio 5.2: Adatta la RegEx per accettare anche il formato gg-mm-aaaa.

Svolgimento:

    Esercizio 5.1:

        ^(?:0[1-9]|[12][0-9]|3[0-1])\/(?:0[1-9]|1[0-2])\/\d{4}$

    Esercizio 5.2:

        ^(?:0[1-9]|[12][0-9]|3[0-1])-(?:0[1-9]|1[0-2])-\d{4}$

'''