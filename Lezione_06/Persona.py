class Persona:

    '''
    Di una persona dobbiamo sapere delle informazioni.
    Queste informazioni vengono chiamate attributi (della classe 'Persona')
    Le informazioni saranno:

    - nome
    - cognome
    - età

    Come li rappresento in Python?

    self.name: str          (attributo di tipo stringa)
    self.lastname: str      (attributo di tipo stringa)
    self.age: int           (attributo di tipo int)
    '''

    def __init__(self, name: str, lastname: str, age: int):

        # il 'self' indica che la var 'name' appartiene alla classe 'Persona' ed etc.
        self.name = name
        self.lastname = lastname
        self.age = age

    def displaydata(self) -> None:

        print(f"\nNome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}\n")

if __name__ == "__main__":

    d: Persona = Persona("Dioni", "Manon", 40)

    # mostra i dati di una persona
    d.displaydata()

    # # Errore, fa vedere solo l'indirizzo di memoria
    # print(d)