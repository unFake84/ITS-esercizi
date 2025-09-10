'''
Vogliamo gestire un contatore che può essere incrementato, decrementato, resettato e visualizzato.
La classe offre un modo semplice per tenere traccia di un conteggio che non può diventare negativo.

Classe Contatore
Attributi:
- conteggio: un intero che conserva il valore del conteggio, inizializzato a 0.

Metodi:
- __init__(): Inizializza l'attributo conteggio a 0.
- setZero(): Imposta il conteggio a 0.
- add1(): Incrementa il conteggio di 1.
- sub1(): Decrementa il conteggio di 1, ma non permette che il conteggio diventi negativo.
  Se il conteggio è già 0, stampa un messaggio di errore.
- get(): Restituisce il valore corrente del conteggio.
- mostra(): Stampa a schermo il valore corrente del conteggio.

'''

class Contatore:

    _conteggio: int

    def __init__(self, conteggio: int = 0) -> None:
        self._conteggio = conteggio

    def setZero(self) -> None:
        self._conteggio = 0

    def add1(self) -> None:
        self._conteggio += 1

    def sub1(self) -> None:
        if self._conteggio == 0:
            print("Non è possibile eseguire la sottrazione")
            return

        self._conteggio -= 1
        if self._conteggio < 0:
            self._conteggio = 0
    
    def get(self) -> int:
        return self._conteggio
    
    def mostra(self) -> None:
        print(f"Conteggio attuale: {self._conteggio}")