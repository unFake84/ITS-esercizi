from abc import ABC, abstractmethod

class Ride(ABC):
    '''
Classe Ride

La classe Ride rappresenta un’attrazione generica del parco.
È una classe astratta e non può essere istanziata direttamente.
Ogni attrazione ha:

    un identificativo (id) di tipo stringa;
    un nome (name) di tipo stringa;
    un’altezza minima richiesta (min_height_cm) di tipo intero.

Metodi:

    category():
        metodo astratto.
        Deve essere implementato nelle sottoclassi per
        restituire la categoria dell’attrazione (es. "roller_coaster", "family").

    base_wait():
        metodo astratto.
        Deve essere implementato nelle sottoclassi e deve restituire l’attesa base in minuti.

    info():
        metodo concreto che restituisce un dizionario con le informazioni principali
        dell’attrazione (id, nome, altezza minima, categoria e attributi specifici).

    wait_time(crowd_factor: float = 1.0):
        metodo concreto
        che restituisce l’attesa stimata in minuti.
        L’attesa è calcolata come base_wait() * crowd_factor, arrotondata all’intero positivo.
    '''
    def __init__(self, identificativo: str, nome: str, min_height_cm: int) -> None:
        self.identificativo: str = identificativo
        self.nome: str = nome
        self.min_height: int = min_height_cm

    @abstractmethod
    def category(self) -> str:
        pass

    @abstractmethod
    def base_wait(self) -> int:
        pass

    def info(self) -> dict[str, str|int]:
        return {
            "id": self.identificativo,
            "nome": self.nome,
            "altezza_minima": self.min_height,
            "categoria": self.category()
            }

    def wait_time(self, crowd_factor: float = 1.0) -> int:
        return round(self.base_wait() * crowd_factor)

class RollerCoaster(Ride):
    '''
Classe RollerCoaster

La classe RollerCoaster rappresenta una montagna russa e eredita da Ride.

Attributi aggiuntivi:

    inversions: numero di inversioni presenti nel tracciato (ad esempio 3 o 5).

Metodi:

    category():
        restituisce la stringa "roller_coaster".

    base_wait():
        restituisce l’attesa base in minuti (ad esempio 40).

    info():
        estende il metodo della superclasse includendo anche il numero di inversioni.
    '''
    def __init__(self, identificativo: str, nome: str, min_height_cm: int, inversions: int) -> None:
        super().__init__(identificativo, nome, min_height_cm)

        self.inversions: int = inversions

    def category(self) -> str:
        return "roller_coaster"

    def base_wait(self) -> int:
        return 40

    def info(self) -> dict[str, str|int]:
        data: dict[str, str|int] = super().info()
        data["inversioni"] = self.inversions

        return data

class Carousel(Ride):
    '''
Classe Carousel

La classe Carousel rappresenta una giostra con animali e eredita da Ride.

Attributi aggiuntivi:

    animals:
        lista di animali presenti sulla giostra (ad esempio ["horse", "swan", "tiger"]).

Metodi:

    category():
        restituisce la stringa "family".

    base_wait():
        restituisce l’attesa base in minuti (ad esempio 10).

    info():
        estende il metodo della superclasse includendo la lista di animali.
    '''
    def __init__(self, identificativo: str, nome: str, min_height_cm: int, animals: list[str]) -> None:
        super().__init__(identificativo, nome, min_height_cm)

        self.animals: list[str] = animals

    def category(self) -> str:
        return "family"

    def base_wait(self) -> int:
        return 10

    def info(self) -> dict[str, str|int]:
        data: dict[str, str|int] = super().info()
        data["animali"] = self.animals
        return data

class Park:
    '''
Classe Park

La classe Park rappresenta il contenitore principale del sistema, che gestisce tutte le attrazioni presenti nel parco.

Attributi:

    rides: dizionario che associa a ogni identificativo (id) l’oggetto Ride corrispondente.

Metodi:

    add(ride):
        aggiunge un’attrazione al parco.

    get(ride_id):
        restituisce l’attrazione corrispondente all’ID specificato oppure None se non esiste.

    list_all():
        restituisce una lista di tutte le attrazioni (puoi ordinare per categoria e nome, opzionale).
    '''
    def __init__(self, rides: dict[str, Ride] = None) -> None:
        self.rides: dict[str, Ride] = rides if rides is not None else {}

    def add(self, ride: Ride) -> None:
        self.rides[ride.identificativo] = ride

    def get(self, ride_id: str) -> Ride|None:
        if ride_id not in self.rides:
            return None

        return self.rides[ride_id]

    def list_all(self) -> list[dict[str, str|int]]:

        return [ride.info() for ride in self.rides.values()]

"""
Nel codice principale dovrà essere creato un parco
e dovranno essere create almeno due attrazioni,
una di tipo RollerCoaster e una di tipo Carousel.
"""
ride1: RollerCoaster = RollerCoaster("1", "RollerBanCoaster", 140, 3)
ride2: Carousel = Carousel("2", "Carousel", 60, ["cavallo", "tigre", "elefante", "ippopotamo"])
dizioActraction: dict[str, Ride] = {
    ride1.identificativo: ride1,
    ride2.identificativo: ride2
}

parco1: Park = Park(dizioActraction)

# print(ride1.info())
# print(ride2.info())
print(parco1.list_all())