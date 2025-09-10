'''

Obiettivo
L'obiettivo di questo esercizio è creare un modello semplice per simulare la crescita delle popolazioni
di due specie animali usando la programmazione orientata agli oggetti in Python.

Descrizione del problema
Due specie animali, i Bufali Klingon e gli Elefanti, vivono in una riserva naturale.
Ogni specie ha una popolazione iniziale e un tasso di crescita annuo. Vogliamo sapere:
- In quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon.
- In quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km².
 
Specifiche tecniche

1. Classe Specie
- Attributi:

    nome (str): Nome della specie.
    popolazione (int): Popolazione iniziale.
    tasso_crescita (float): Tasso di crescita annuo percentuale.

- Metodi:

    - __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
      Costruttore per inizializzare gli attributi della classe.

    - cresci(self, popolazione: int):
      Metodo per aggiornare la popolazione per l'anno successivo.

    - anni_per_superare(self, altra_specie: Specie) -> int:
      Metodo per calcolare in quanti anni la popolazione di questa specie supererà quella di un'altra specie.

    - getDensita(self, area_kmq: float) -> int:
      Metodo per calcolare in quanti anni la popolazione raggiungerà una densità di 1 individuo per km². 

2. Sottoclassi BufaloKlingon e Elefante
Entrambe le sottoclassi animali BufaloKlingon ed Elefante devono ereditare dalla classe base Specie e
devono inizializzare il nome della specie rispettiva.
 
Formule Matematiche:

    Aggiornamento della popolazione per l'anno successivo:
        Formula: popolazione_nuova = popolazione_attuale x (1 + tasso_crescita/100)

    Calcolo della densità di popolazione:
        Formula: popolazione / area_kmq
        Hint: Loop incrementale che continua ad aggiornare la popolazione finché la densità non raggiunge 1 individuo per km²

    Calcolo degli anni necessari per superare la popolazione di un'altra specie:
        Hint: Loop incrementale che continua ad aggiornare la popolazione di entrambe le specie finché la popolazione di una specie
        non supera quella dell'altra. Per evitare che le popolazioni crescano all'infinito, limitare il numero di anni a 1000. 

'''

class Specie:

    _nome: str
    _popolazione: int
    _tasso_crescita: float

    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float) -> None:
        self._nome = nome
        self._popolazione = popolazione_iniziale
        self._tasso_crescita = tasso_crescita

    def cresci(self, popolazione: int) -> None:
        return popolazione * (1 + self._tasso_crescita / 100)

    def anni_per_superare(self, altra_specie: "Specie") -> int:
        anni: int = 0
        pop_self: int|float = self._popolazione
        pop_altra: int|float = altra_specie._popolazione

        while pop_self <= pop_altra:
            pop_self = self.cresci(pop_self)
            pop_altra = altra_specie.cresci(pop_altra)
            anni += 1
        
        return anni

    def getDensita(self, area_kmq: float) -> float:
        densita: float = self._popolazione / area_kmq

        if densita >= 1:
            return 0

        anni: int = 0
        pop_locale: int|float = self._popolazione

        while pop_locale / area_kmq < 1:
            pop_locale = self.cresci(pop_locale)
            anni += 1

        return anni

class BufaloKlingon(Specie):

    def __init__(self, popolazione_iniziale: int, tasso_crescita: float) -> None:
        super().__init__("BufaloKlingon", popolazione_iniziale, tasso_crescita)

class Elefante(Specie):

    def __init__(self, popolazione_iniziale: int, tasso_crescita: float):
        super().__init__("Elefante", popolazione_iniziale, tasso_crescita)