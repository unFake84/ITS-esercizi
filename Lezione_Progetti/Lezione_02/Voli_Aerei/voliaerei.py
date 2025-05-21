import FlightCode, IATACode, Age, FlightTime

class PersonalRaises(Exception):    
    pass

class Volo:
    def __eq__(self, other: "Volo"):        
        return self.flightcode == other.flightcode    
    def __hash__(self):        
        return hash(self.flightcode)

    def __init__(self, flightcode: FlightCode, flighttime: FlightTime) -> None:
        if not isinstance(flightcode, FlightCode):
            raise PersonalRaises("The type must be a FlightCode type.")
        if not isinstance(flighttime, FlightTime):
            raise ValueError("The type must be a FlightTime type")
        
        self.flightcode: FlightCode = flightcode
        self.flighttime: FlightTime = flighttime
            
class Aeroporto:
    def __eq__(self, other: "Aeroporto") -> bool:        
        return self.iata_code == other.iata_code and self.port_name == other.port_name

    def __hash__(self):
        return hash((self.iata_code, self.port_name))

    def __init__(self, iata_code: IATACode, port_name: str):  
        if not isinstance(port_name, str):
            raise PersonalRaises("The airport name must be of string type.")
        
        try:
            if not isinstance(iata_code, IATACode):
                raise PersonalRaises("The airport code must be of type IATACode.")

            self.port_name: str = port_name

        except ValueError as unknow:
            raise PersonalRaises(f"Error in airport type: {unknow}.")

        self.iata_code = iata_code
            
class Compagnia:
    def __eq__(self, other: "Compagnia"):        
        return self.compagnia_nome == other.compagnia_nome

    def __hash__(self):        
        return hash(self.compagnia_nome)

    def __init__(self, compagnia_nome: str, anno_fondazione: Age):
        if not isinstance(compagnia_nome, str):
            raise PersonalRaises("The company name must be of string type.")

        try:
            if not isinstance(anno_fondazione, Age):
                raise ValueError("Not an Age type")

            self.anno_fondazione: Age = anno_fondazione

        except ValueError as unknow:
            raise PersonalRaises(f"Error in Age type: {str(unknow)}.")

        self.compagnia_nome: str = compagnia_nome

class Citta:

    def __eq__(self, other: "Citta"):
        return self.nazione_citta == other.nazione_citta and self.nome_citta == other.nome_citta

    def __init__(self, nome_citta: str, abitanti: int = 0, nazione_citta: "Nazione" = None):
        if isinstance(nome_citta, str) and isinstance(abitanti, int) and nazione_citta is not None:

            if abitanti < 0:
                raise PersonalRaises("The value per inhabitant cannot be less than 0.")
            
            self.nome_citta = nome_citta
            self.abitanti = abitanti
            self.nazione_citta = nazione_citta
            

        elif not isinstance(nome_citta, str):
            raise PersonalRaises("The city must be of type string.")

        elif not isinstance(abitanti, int):
            raise PersonalRaises("The number of inhabitants must be of integer type.")
        
        elif nazione_citta is None:
            raise PersonalRaises("The country must be entered.")
        
class Nazione:
    def __eq__(self, other: "Nazione"):        
        return self.nome_nazione == other.nome_nazione
    
    def __hash__(self):        
        return hash(self.nome_nazione)

    def __init__(self, nome_nazione: str):
        if isinstance(nome_nazione, str):
            self.nome_nazione = nome_nazione

        else:
            raise PersonalRaises("The country must be of type string.")
        
if __name__ == "__main__":

    # Due istanze di Volo con stesso codice_volo → == True, un solo elemento in un set

    # Due istanze di Città con stesso nome e nazione → == True

    # Istanza di Aeroporto con tipo errato → solleva PersonalRaises
    pass