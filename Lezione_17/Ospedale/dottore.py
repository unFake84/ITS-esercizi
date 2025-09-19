'''
### CLASSE: Dottore
Creare un file chiamato "dottore.py".
In tale file, definire una classe chiamata Dottore. Si derivi Dottore dalla classe Persona.

Un dottore ha un nome, un cognome, un età, definiti dalla classe Persona,
una specializzazione descritta tramite una stringa (ad esempio, Pediatra, Ostetrico, Medico Generale),
ed una parcella per le visite in studio (si usi il tipo float).
Gli attributi della classe dottore devono essere anch'essi privati.

- Definire i seguenti metodi:

    costruttore della classe Dottore,
    il quale richiede in input la specializzazione (specialization) di un dottore e la sua parcella (parcel).
    Tale metodo deve controllare che specialization sia una stringa e che parcel sia un float,
    altrimenti assegna None all'attributo che non verifica la condizione richiesta,
    mostrando un messaggio di errore, ad esempio, "La parcella inserita non è un float!".

    setSpecialization(specialization):
    Consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo.
    Il valore viene modificato se e solo se viene passata al metodo una stringa.
    In caso contrario, stamapre un messaggio di errore, ad esempio "La specializzazione inserita non è una stringa!".

    setParcel(parcel):
    Consente di impostare la parcella di un dottore, modificando il valore del relativo attributo.
    Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario,
    stamapre un messaggio di errore, ad esempio "La parcella inserita non è un float!".

    getSpecialization():
    Consente di ritornare la specializzazione del dottore.

    getParcel():
    Consente di ritornare la parcella del dottore.

    isAValidDoctor():
    Stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni,
    in quanto ha avuto il tempo necessario di compiere i suoi studi in medicina.
    Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido.
    In caso contrario, stampare "Doctor nome e cognome is not valid!".

    doctorGreet():
    Tale metodo richiama la funzione greet() della classe Persona.
    Poi, stampa il seguente saluto "Sono un medico {specializzazione}"
'''

from persona import Person

class Doctor(Person):

    __specialization: str
    __parcel: float

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)

        self.__specialization = specialization if isinstance(specialization, str) else None
        self.__parcel = parcel if isinstance(parcel, float) else None

        if self.__specialization is None:
            print("La specializzazione inserita non è una stringa!")

        if self.__parcel is None:
            print("La parcella inserita non è un float!")

    def __str__(self):
        parcel_filter: str = f"{self.__parcel:.2f}" if self.__parcel is not None else "Non definita"
        return super().__str__() + f"\nSpecializzazione: {self.__specialization}\nParcella: {parcel_filter}"

    def setSpecialization(self, specialization: str) -> None:
        if isinstance(specialization, str):

            self.__specialization = specialization

        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel: float) -> None:
        if isinstance(parcel, float) and parcel >= 0:

            self.__parcel = parcel

        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self) -> str:
        return self.__specialization

    def getParcel(self) -> float:
        return self.__parcel

    def isAValidDoctor(self) -> None:
        if self.getAge() > 30:

            print(f"Il dottore {self.getName()} {self.getLastName()} è un dottore valido!")
            return True

        else:
            print(f"Il dottore {self.getName()} {self.getLastName()} non è un dottore valido!")
            return False

    def doctorGreet(self) -> None:
        self.greet()
        print(f"Sono un medico {self.getSpecialization()}")

if __name__ == "__main__":

    d1: Doctor = Doctor("Pino", "Micio", "Piediatra", 97.5)
    d1.setAge(30)

    d1.setSpecialization("Medico base")
    d1.setParcel(99.5)

    #print(d1)
    #d1.isAValidDoctor()
    d1.doctorGreet()