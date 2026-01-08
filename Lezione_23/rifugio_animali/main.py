from abc import ABC, abstractmethod

class Animal(ABC):
    '''
    La classe Animal rappresenta un animale generico del rifugio.
    È una classe astratta e non può essere istanziata direttamente.

    Ogni animale ha:

        un identificativo id di tipo stringa (es. "d1", "c3"),

        un nome name di tipo stringa,

        un’età age_years di tipo intero (anni),

        un peso weight_kg di tipo float (chilogrammi).

    Metodi

        species(): metodo astratto.
        Deve essere implementato nelle sottoclassi per restituire la specie dell’animale, ad esempio "dog" o "cat".

        daily_food_grams(): metodo astratto.
        Deve essere implementato nelle sottoclassi e deve restituire la quantità di cibo giornaliera raccomandata in grammi.

        info(): metodo concreto.
        Restituisce un dizionario con le informazioni principali dell’animale, ad esempio:
        { "id": ..., "name": ..., "species": ..., "age_years": ..., "weight_kg": ..., # più eventuali campi specifici delle sottoclassi }

        bmi_like(): metodo concreto che restituisce un valore derivato (simile a un indice di “forma fisica”), ad esempio calcolato come:
        weight_kg / (age_years + 1)
        Il dettaglio della formula è lasciato libero, l’importante è che sia coerente e restituisca un numero (float).
    '''
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float) -> None:
        self.id = id
        self.name = name
        self.age_years = age_years
        self.weight_kg = weight_kg
    
    @abstractmethod
    def species(self) -> str:
        pass

    @abstractmethod
    def daily_food_grams(self) -> int:
        pass

    def info(self) -> dict[str, str|int|float]:
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species(),
            "age_years": self.age_years,
            "weight_kg": self.weight_kg
        }
    
    def bmi_like(self) -> float:
        return self.weight_kg / (self.age_years + 1)
    
class Dog(Animal):
    '''
    La classe Dog rappresenta un cane e eredita da Animal.
    Attributi aggiuntivi

        breed: razza del cane, stringa (es. "labrador"),

        is_trained: booleano che indica se il cane è addestrato (True/False).

    Metodi

        species(): restituisce la stringa "dog".

        daily_food_grams(): restituisce la quantità di cibo giornaliero in grammi.
        Puoi usare una formula plausibile, ad esempio:
        return 200 + age_years * 50

        oppure un’altra a tua scelta, purché sia chiaro che il risultato rappresenta grammi di cibo al giorno.

        info(): estende il metodo della superclasse includendo anche breed e is_trained.
    '''
    def __init__(self, id: str, name: str, age_years: int, weight_kg: float, breed: str, is_trained: bool):
        super().__init__(id, name, age_years, weight_kg)

        self.breed = breed
        self.is_trained = is_trained
    
    def species(self) -> str:
        return "dog"
    
    def daily_food_grams(self) -> int:
        return 200 + self.age_years * 50
    
    def info(self) -> dict[str, str|int|float|bool]:
        data: dict[str, str|int|float] = super().info()
        data["breed"] = self.breed
        data["is_trained"] = self.is_trained

        return data

class Cat(Animal):
    '''
    Classe Cat

    La classe Cat rappresenta un gatto e eredita da Animal.
    Attributi aggiuntivi

        indoor_only: booleano che indica se il gatto vive solo in casa (True/False),

        favorite_toy: stringa che rappresenta il gioco preferito (es. "ball", "mouse").

    Metodi

        species(): restituisce la stringa "cat".

        daily_food_grams(): restituisce la quantità di cibo giornaliero in grammi.
        Anche qui puoi usare una formula plausibile, ad esempio:
        return 100 + age_years * 30

        info(): estende il metodo della superclasse includendo anche indoor_only e favorite_toy.
    '''
    def __init__(
            self, id: str,
            name: str,
            age_years: int,
            weight_kg: float,
            indoor_only: bool,
            favorite_toy: str
        ):
        super().__init__(id, name, age_years, weight_kg)

        self.indoor_only = indoor_only
        self.favorite_toy = favorite_toy
    
    def species(self) -> str:
        return "cat"
    
    def daily_food_grams(self) -> int:
        return 100 + self.age_years * 30
    
    def info(self) -> dict[str, str|int|float|bool]:
        data: dict[str, str|int|float] = super().info()
        data["indoor_only"] = self.indoor_only
        data["favorite_toy"] = self.favorite_toy

        return data