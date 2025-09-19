'''
### CLASSE: Paziente
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed
un codice identificativo(si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente:
    Il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.

    setIdCode(idCode):
    Consente di impostare il codice identificativo del paziente.

    getidCode(): consente di ritornare il codice identificativo del paziente.

    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
'''

from persona import Person

class Patient(Person):

    __id: str

    def __init__(self, first_name: str, last_name: str, id_code: str) -> None:
        super().__init__(first_name, last_name)

        self.__id = id_code if isinstance(id_code, str) else None

        if self.__id is None:
            print("L'id code non è di tipo stringa!")

    def setIdCode(self, idCode: str) -> None:
        if isinstance(idCode, str):

            self.__id = idCode

        else:
            print("L'id code non è di tipo stringa!")

    def getIdCode(self) -> str|None:
        return self.__id

    def patientInfo(self) -> None:
        if self.__id is not None:

            print(f"Paziente: {self.getName()} {self.getLastName()}\nID: {self.getIdCode()}")

    def __str__(self):
        return super().__str__() + f"\nPatient id: {self.__id}"

if __name__ == "__main__":

    p1: Patient = Patient("Galbanino", "Spezzati", 12)
    p1.setAge(27)

    p1.setIdCode("001")

    #print(p1)

    p1.patientInfo()