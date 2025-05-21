from FlightCode import FlightCode
from IATACode import IATACode
from Age import Age
from FlightTime import FlightTime

class PersonalRaises(Exception):    
    pass

class Volo:
    def __init__(self, flightcode: FlightCode, flighttime: FlightTime) -> None:
        if not isinstance(flightcode, FlightCode):
            raise PersonalRaises("The type must be a FlightCode type.")
        if not isinstance(flighttime, FlightTime):
            raise ValueError("The type must be a FlightTime type")
        
        self.flightcode: FlightCode = flightcode
        self.flighttime: FlightTime = flighttime

    def __str__(self) -> str:
        return f"Code: {self.flightcode}, Duration: {self.flighttime}"

    def __eq__(self, other: "Volo") -> bool:        
        return self.flightcode == other.flightcode    
    def __hash__(self) -> int:        
        return hash(self.flightcode)
            
class Aeroporto:

    def __init__(self, iata_code: IATACode, port_name: str) -> None:  
        if not isinstance(port_name, str):
            raise PersonalRaises("The airport name must be of string type.")
        
        try:
            if not isinstance(iata_code, IATACode):
                raise PersonalRaises("The airport code must be of type IATACode.")

            self.port_name: str = port_name

        except ValueError as unknow:
            raise PersonalRaises(f"Error in airport type: {unknow}.")

        self.iata_code = iata_code

    def __eq__(self, other: "Aeroporto") -> bool:        
        return self.iata_code == other.iata_code and self.port_name == other.port_name

    def __hash__(self) -> int:
        return hash((self.iata_code, self.port_name))
            
class Compagnia:

    def __init__(self, company_name: str, foundation_age: Age) -> None:
        if not isinstance(company_name, str):
            raise PersonalRaises("The company name must be of string type.")

        try:
            if not isinstance(foundation_age, Age):
                raise ValueError("Not an Age type")

            self.foundation_age: Age = foundation_age

        except ValueError as unknow:
            raise PersonalRaises(f"Error in Age type: {str(unknow)}.")

        self.company_name = company_name

    def __eq__(self, other: "Compagnia") -> bool:        
        return self.company_name == other.company_name

    def __hash__(self) -> int:        
        return hash(self.company_name)
    
class Citta:

    def __init__(self, city_name: str, populaion: int = 0, nation_city: "Nazione" = None):
        if isinstance(city_name, str) and isinstance(populaion, int) and nation_city is not None:

            if populaion < 0:
                raise PersonalRaises("The value per inhabitant cannot be less than 0.")
            
            self.city_name = city_name
            self.populaion = populaion
            self.nation_city = nation_city            

        elif not isinstance(city_name, str):
            raise PersonalRaises("The city must be of type string.")

        elif not isinstance(populaion, int):
            raise PersonalRaises("The number of inhabitants must be of integer type.")
        
        elif nation_city is None:
            raise PersonalRaises("The country must be entered.")
        
    def __eq__(self, other: "Citta") -> bool:
        return self.nation_city == other.nation_city and self.city_name == other.city_name
    
    def __hash__(self) -> int:
        return hash((self.nation_city, self.city_name))
        
class Nazione:
    def __init__(self, nation_name: str) -> None:
        if isinstance(nation_name, str):
            self.nation_name = nation_name

        else:
            raise PersonalRaises("The country must be of type string.")
        
    def __eq__(self, other: "Nazione") -> bool:        
        return self.nation_name == other.nation_name
    
    def __hash__(self) -> int:        
        return hash(self.nation_name)
        
if __name__ == "__main__":
    volocod: FlightCode = FlightCode("AA 1234")
    volotime: FlightTime = FlightTime("01:24")
    a1: Volo = Volo(volocod, volotime)
    a2: Volo = Volo(volocod, volotime)
    print(a1, "\n", a2)
    print("a1 and a2 have same flightcode?", a1 == a2)

    diziodivoli: dict = {
        a1: "First flight",
        a2: "Second flight"
    }

    print(f"Flight collections without duplicates: {len(diziodivoli)}")
    print("a1 is same istance of a2?:", a1 is a2)
    print("a2 was discarded because a1 has the same flight code?", a1 == a2)

    # OK Due istanze di Volo con stesso codice_volo → == True, un solo elemento in un set

    # Due istanze di Città con stesso nome e nazione → == True

    # Istanza di Aeroporto con tipo errato → solleva PersonalRaises