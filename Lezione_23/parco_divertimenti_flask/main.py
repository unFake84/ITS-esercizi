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
            "altezza minima": self.min_height,
            "categoria": self.category()
            }

    def wait_time(self, crowd_factor: float = 1.0) -> float:
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

    def info(self):
        return {
            "id": self.identificativo,
            "nome": self.nome,
            "altezza minima": self.min_height,
            "categoria": self.category(),
            "inversioni": self.inversions
            }

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

    def category(self):
        return "family"

    def base_wait(self):
        return 10

    def info(self):
        return {
            "id": self.identificativo,
            "nome": self.nome,
            "altezza minima": self.min_height,
            "categoria": self.category(),
            "animali": self.animals
            }

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
    def __init__(self, rides: dict[str, Ride] = {}) -> None:
        self.rides: dict[str, Ride] = rides
    
    def add(self, ride: Ride) -> None:
        self.rides[ride.identificativo] = ride
    
    def get(self, ride_id: str) -> Ride|None:
        if ride_id not in self.rides:
            return None

        return self.rides[ride_id]
    
    def list_all(self) -> list[Ride]:
        lista_roller: list[Ride] = [a1 for a1 in self.rides.values() if a1.category() == "roller_coaster"]
        lista_carosuel: list[Ride] = [a2 for a2 in self.rides.values() if a2.category() == "family"]

        return lista_roller + lista_carosuel