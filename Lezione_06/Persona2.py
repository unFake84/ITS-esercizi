class Persona:

    def __init__(self):

        self.name = ""
        self.lastname = ""
        self.age = 0

    def setname(self, name: str):
        
        self.name = name

    def getname(self):

        return self.name

    def setlastname(self, lastname: str) -> None:

        self.lastname = lastname

    def getlastname(self):

        return self.lastname

    def setage(self, age: int) -> None:

        if age < 1 or age > 130:

            self.age = 0

        else:

            self.age = age

    def getage(self):

        return self.age

    def displaydata(self) -> None:

        print(f"\nNome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}\n")

# crea un oggetto di tipo persona
d: Persona = Persona()

# impostare il nome della persona
d.setname("Dioni")

# impostare il cognome
d.setlastname("Manon")

# impostare il nome
d.setage(40)

d.displaydata()