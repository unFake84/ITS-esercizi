'''

Esercizi - Comprensione di RegEx

    Esercizio 7.1: Cosa fa questa RegEx? ^[A-Z][a-z]{2,}$
    Esercizio 7.2: Quali stringhe sono accettate da \d{3}-\d{2}-\d{4}?
    Esercizio 7.3: Qual è l’effetto del simbolo ? in questa RegEx: colou?r

Bonus - Errori comuni

Obiettivo: Trovare errori in RegEx sbagliate.

    Esercizio 8.1: Qual è l’errore nella RegEx ^\d{2,5}?$ se voglio matchare da 2 a 5 cifre?
    Esercizio 8.2: La RegEx [A-z] funziona per lettere? Perché può essere rischiosa?

Esercizio	       RegEx	                         Descrizione	                                          Esempi

7.1	         ^[A-Z][a-z]{2,}$	   Lettera maiuscola seguita da 2 o più lettere minuscole	               Apple, Banana

7.2	         \d{3}-\d{2}-\d{4}	     3 numeri, trattino, 2 numeri, trattino, 4 numeri              	123-45-6789, 001-22-3344

7.3	              colou?r	                 La lettera "u" è opzionale	                                   color, colour

8.1	            ^\d{2,5}?$	        ? rende opzionale l'elemento precedente, quindi errore              	^\d{2,5}$

8.2	              [A-z]         	Includendo caratteri speciali tra Z e a, non solo lettere              	[A-Za-z]

'''