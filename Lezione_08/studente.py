from persona import Persona

class Studente(Persona):

    '''
    Attributi della classe Persona (in quanto studente eredita da Persona):
    self.name: str
    self.lastname: str
    self.age: int

    
    Attributi della classe Studente:
    self.matricola: str 
    '''

    def __init__(self, name: str, lastname: str, age: int, matricola: str):

        # inizializzare la classe Persona, richiamando il metodo init della superclasse.
        super().__init__(name, lastname, age)

        # istruzioni che inizializzano un oggetto della classe Studente
        self.setMatricola(matricola)

    # metodi setter 

    # metodo che imposta il valore dell'attributo self.matricola
    def setMatricola(self, matricola: str) -> None:

        if matricola:

            self.matricola = matricola

        else:

            print("Error, the serial number cannot be represented by an empty string")

    # metodi getter

    # metodo che ritorna il valore dell'attributo self.matricola
    def getMatricola(self) -> str:

        return self.matricola
    
    # ridefinire il metodo __str__
    def __str__(self) -> str:

        return f"\nName: {self.name}\nLastname: {self.getlastname()}\nMatricola: {self.getMatricola()}"

        # return super().__str__()