'''
### CLASSE: Film
In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio.
In tale classe, definire un codice identificativo (int) ed un titolo (string).
Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.
'''

class Film:

    __codice_identificativo: int
    __titolo: str

    def __init__(self, codice_identificativo: int, titolo: str) -> None:
        self.__codice_identificativo = codice_identificativo
        self.__titolo = titolo

    def setID(self, set_id: int) -> None:
        self.__codice_identificativo = set_id

    def setTitle(self, title: str) -> None:
        self.__titolo = title

    def getID(self) -> int:
        return self.__codice_identificativo

    def getTitle(self) -> str:
        return self.__titolo

    def isEqual(self, otherFilm: "Film") -> bool:
        if self.getID() == otherFilm.getID():
            return True

        return False
    
if __name__ == "__main__":

    f1: Film = Film(1, "Amadeus")
    f2: Film = Film(2, "I love Chopin")

    print(f1.isEqual(f2))