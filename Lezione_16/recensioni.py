'''
SISTEMA DI RECENSIONI

Obiettivo:
Implementare una classe Media che rappresenti un media generico
(ad esempio, un film o un libro) e una classe derivata Film che
rappresenti specificamente un film e ne specifichi il titolo.
Gli studenti dovranno anche creare oggetti di queste classi, ag
giungere valutazioni e visualizzare le recensioni.

Specifiche della Classe Media:

Attributi:
- title (stringa): Il titolo del media.
- reviews (lista di interi): Una lista di valutazioni del media,
  con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto,
  3=Normale, 4=Bello, 5=Grandioso.

Metodi:
- set_title(self, title): Imposta il titolo del media.
- get_title(self): Restituisce il titolo del media.
- aggiungiValutazione(self, voto): Aggiunge una valutazione alla
  lista delle recensioni se è valida (tra 1 e 5).
- getMedia(self): Calcola e restituisce la media delle valutazioni.
- getRate(self): Restituisce una stringa che descrive il giudizio
  medio basato sulla media delle valutazioni, ovvero mostra 
  "Terribile" se il voto medio si avvicina a 1,
  "Brutto" se il voto medio si avvicina a 2,
  "Normale" se il voto medio si avvicina a 3,
  "Bello" se il voto medio si avvicina a 4,
  "Grandioso" se il voto medio si avvicina a 5.
- ratePercentage(self, voto): Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
- recensione(self): Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo,
  il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:

    Titolo del Film: The Shawshank Redemption
    Voto Medio: 3.80
    Giudizio: Bello
    Terribile: 10.00%
    Brutto: 10.00%
    Normale: 10.00%
    Bello: 30.00%
    Grandioso: 40.00%

Si verifichi il funzionamento scrivendo un codice che crei almeno due oggetti di tipo Film,
aggiunga a ognuno dei due almeno dieci valutazioni e richiami il metodo recensione().

'''

class Media:
    '''
    Specifiche della Classe Media:

    Attributi:
    - title (stringa): Il titolo del media.
    - reviews (lista di interi): Una lista di valutazioni del media,
      con voti compresi tra 1 e 5, dove 1=Terribile, 2=Brutto,
      3=Normale, 4=Bello, 5=Grandioso.
    '''

    _title: str
    _reviews: list[int]

    def __init__(self, title: str) -> None:
        self._title = title
        self._reviews = []

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, t: str) -> None:
        self._title = t

    @property
    def reviews(self) -> list[int]:
        return self._reviews

    def aggiungiValutazione(self, voto: int) -> None:
        '''- Aggiunge una valutazione alla lista delle recensioni se è valida (tra 1 e 5).'''

        if voto < 1 or voto > 5:
            raise ValueError(f"{voto} non è valido come votazione")

        self.reviews.append(voto)

    def getMedia(self) -> float:
        '''- Calcola e restituisce la media delle valutazioni.'''
        totale_voti: int = 0
        for voto in self.reviews:

            totale_voti += voto

        return totale_voti / len(self.reviews) if self.reviews else 0

    def getRate(self) -> str:
        '''
        - Restituisce una stringa che descrive il giudizio medio <br>
          basato sulla media delle valutazioni, ovvero mostra: <br>
            - "Terribile" se il voto medio si avvicina a 1, <br>
            - "Brutto" se il voto medio si avvicina a 2, <br>
            - "Normale" se il voto medio si avvicina a 3,<br>
            - "Bello" se il voto medio si avvicina a 4, <br>
            - "Grandioso" se il voto medio si avvicina a 5.
        '''

        voto_medio: float = round(self.getMedia())
        valutazione: dict[int, str] = {
            1: "Terribile",
            2: "Brutto",
            3: "Normale",
            4: "Bello",
            5: "Grandioso"
        }

        return valutazione[voto_medio] if voto_medio > 0 else "Non ancora valutato"

    def ratePercentage(self, voto: int) -> int:
        '''
        - Calcola e restituisce la percentuale di un voto specifico nelle recensioni.
        '''

        tot_voto: int = 0
        tot_totale: int = 0

        for v in self.reviews:

            if v == voto:
                tot_voto += 1

            tot_totale += 1

        if tot_totale > 0:
            return round((tot_voto / tot_totale) * 100)

        return 0

    def recensione(self, header: str = "Titolo:") -> str:
        '''
        - Mostra un riassunto delle recensioni e delle valutazioni del media, stampando il titolo,
          il voto medio, il giudizio e le percentuali di ciascun voto. Esempio di riassunto:

            Titolo del Film: The Shawshank Redemption
            Voto Medio: 3.80
            Giudizio: Bello
            Terribile: 10.00%
            Brutto: 10.00%
            Normale: 10.00%
            Bello: 30.00%
            Grandioso: 40.00%
        '''

        stringone: str = f"{header:<20}{self.title}\n"\
                        f"{'Voto Medio:':<20}{self.getMedia():.2f}\n"\
                        f"{'Giudizio:':<20}{self.getRate()}\n"\
                        f"{'Terribile:':<20}{self.ratePercentage(1):.2f}%\n"\
                        f"{'Brutto:':<20}{self.ratePercentage(2):.2f}%\n"\
                        f"{'Normale:':<20}{self.ratePercentage(3):.2f}%\n"\
                        f"{'Bello:':<20}{self.ratePercentage(4):.2f}%\n"\
                        f"{'Grandioso:':<20}{self.ratePercentage(5):.2f}%\n"\

        return stringone

class Film(Media):

    def __init__(self, title):
        super().__init__(title)

    def recensione(self, header = "Titolo del film:"):
        return super().recensione(header)

if __name__ == "__main__":

    media1: Media = Media("True Lies")

    media1.aggiungiValutazione(5)
    media1.aggiungiValutazione(5)
    media1.aggiungiValutazione(4)
    media1.aggiungiValutazione(4)
    media1.aggiungiValutazione(5)
    media1.aggiungiValutazione(4)
    media1.aggiungiValutazione(5)

    print(media1.getMedia())
    print(media1.getRate())
    print(media1.ratePercentage(5))

    media2: Media = Media("Forrest Gump")

    print(media2.ratePercentage(4))
    print("="*150)
    print(media1.recensione())
    print("="*150)

    film1: Film = Film("Navigator")

    film1.aggiungiValutazione(5)
    film1.aggiungiValutazione(4)
    film1.aggiungiValutazione(3)
    film1.aggiungiValutazione(4)
    film1.aggiungiValutazione(3)
    film1.aggiungiValutazione(5)
    film1.aggiungiValutazione(4)

    print("="*150)
    print(film1.recensione())
    print("="*150)