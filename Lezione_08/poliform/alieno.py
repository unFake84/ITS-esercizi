class Alien:

    '''
    
    Di un alieno ci interessa sapere la galassia di provenienza
    self.galaxy: str
    
    '''

    # inizializzare un oggetto della classse Alieno
    def __init__(self, galaxy: str):

        self.setGalaxy(galaxy)

    # definire un metodo per impostare il valore dell'attributo self.galaxy
    def setGalaxy(self, galaxy: str) -> None:

        if galaxy:

            self.galaxy = galaxy

        else:

            print("Error! Galaxy cannot be an empty string")

    # definire un metodo per restituire il valore dell'attributo self.galaxy

    def getGalaxy(self) -> str:

        return self.galaxy
    
    # definire un metodo speak()     <- da notare che speak esiste già sulla classe Persona
    def speak(self) -> None:

        print("Alien say: ajpisdjpasodjjjjjjapsd")

    def __str__(self) -> str:

        return f"Alien from the galaxy {self.getGalaxy()}!"