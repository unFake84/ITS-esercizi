# importo i tipi di dato creati su altri files nella stessa directory
from FlightCode import FlightCode
from IATACode import IATACode
from Year import Year
from FlightTime import FlightTime

# creo una classe personalizzata di eccezioni, così da poterle "raccogliere subito"
class PersonalRaises(Exception):    
    pass

class Volo:

    # i tipo di dato devono essere: FlightCode per il codice di volo e FlightTime per la durata del volo
    # inserisco i metodi __eq__ e __hash__ per evitare di inserire piu voli con la stesso codice di volo
    # il codice di volo deve essere simile ad AA 1234 e la durata 01:12 dove [01] è l'ora e [12] sono i min
    def __init__(self, flightcode: FlightCode, flighttime: FlightTime) -> None:
        if not isinstance(flightcode, FlightCode):
            raise PersonalRaises("The type must be a FlightCode type.")

        if not isinstance(flighttime, FlightTime):
            raise ValueError("The type must be a FlightTime type")

        # se tutto ok assegno gli attributi all'init della classe Volo
        self.flightcode: FlightCode = flightcode
        self.flighttime: FlightTime = flighttime

    # metodo che mi permette di restituire una stringa descrittiva dell'oggetto
    def __str__(self) -> str:
        return f"Code: {self.flightcode}\nDuration: {self.flighttime}"

    # metodo per confrontare due istanze oggetto, se sono simili restituisce True, altrimenti False
    def __eq__(self, other: "Volo") -> bool:        
        return self.flightcode == other.flightcode

    # metodo che crea valore hash per oggetti immutabili, permette uso oggetto in set/dizionari
    def __hash__(self) -> int: # <- restituisce un intero, che ↗
        return hash(self.flightcode)

class Aeroporto:

    # per ora permette un codice di tipo IATA (es.FCO per fiumicino) e una stringa per il nome dell'aeroporto
    # il codice IATA dovrebbe essere univoco, ma ci sono circa 300 casi su 17.500 in cui il codice IATA è identico.
    def __init__(self, iata_code: IATACode, port_name: str) -> None:
        if not isinstance(port_name, str):
            raise PersonalRaises("The airport name must be of string type.")

        if not isinstance(iata_code, IATACode):
            raise PersonalRaises("The airport code must be of IATACode type.")

        self.port_name: str = port_name
        self.iata_code: IATACode = iata_code

    def __str__(self) -> str:
        return f"IATA Code: {self.iata_code}\nPort name: {self.port_name}"

    def __eq__(self, other: "Aeroporto") -> bool:        
        return self.iata_code == other.iata_code and self.port_name == other.port_name

    def __hash__(self) -> int:
        return hash((self.iata_code, self.port_name))

class Compagnia:

    # per ora permette di inserire il nome della compagnia come una stringa, es. "Dioni&Co"
    # e l'anno di fondazione della compagnia, come "1984" di tipo Year (compreso tra il 1900 ed il 2199)
    def __init__(self, company_name: str, foundation_year: Year) -> None:
        if not isinstance(company_name, str):
            raise PersonalRaises("The company name must be of string type.")

        if not isinstance(foundation_year, Year):
            raise PersonalRaises("The foundation year must be of Year type.")

        self.foundation_year: Year = foundation_year
        self.company_name: str = company_name

    def __str__(self) -> str:
        return f"Company name: {self.company_name}\nFounded in: {self.foundation_year}"

    def __eq__(self, other: "Compagnia") -> bool:        
        return self.company_name == other.company_name

    def __hash__(self) -> int:        
        return hash(self.company_name)

class Citta:

    # accetta il nome della città, la popolazione (che non deve essere minore o uguale di 0, altrimenti sollevo un'eccezione)
    # e un oggetto di tipo Nazione, che rappresenta il paese della città
    def __init__(self, city_name: str, population: int, nation_city: "Nazione") -> None:
        if isinstance(city_name, str) and isinstance(population, int) and isinstance(nation_city, Nazione):

            if population <= 0:
                raise PersonalRaises("The population cannot be less than or equal to zero.")

            self.city_name: str = city_name
            self.population: int = population
            self.nation_city: Nazione = nation_city            

        elif not isinstance(city_name, str):
            raise PersonalRaises("The city must be of string type.")

        elif not isinstance(population, int):
            raise PersonalRaises("The population must be an integer.")

        elif not isinstance(nation_city, Nazione):
            raise PersonalRaises("The country must be an instance of the Nazione class.")
        
    def __str__(self) -> str:
        return f"City: {self.city_name}\nPopulation: {self.population}\nCountry: {self.nation_city}"

    # doppio controllo perche due città possono esistere se sono situate in paesi diversi
    def __eq__(self, other: "Citta") -> bool:
        return self.nation_city == other.nation_city and self.city_name == other.city_name

    # restituisce un hash per l'oggetto per consentire l'uso in set o dizionari
    def __hash__(self) -> int:
        return hash((self.nation_city, self.city_name))

class Nazione:

    # accetta una stringa che rappresenta il nome della nazione, e viene utilizzato come parametro in Citta
    def __init__(self, nation_name: str) -> None:
        if not isinstance(nation_name, str):
            raise PersonalRaises("The country name must be a string type.")

        self.nation_name: str = nation_name

    def __str__(self) -> str:
        return f"Nazione: {self.nation_name}"

    def __eq__(self, other: "Nazione") -> bool:        
        return self.nation_name == other.nation_name

    def __hash__(self) -> int:        
        return hash(self.nation_name)