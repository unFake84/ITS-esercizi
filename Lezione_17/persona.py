'''
### CLASSE: Persona
Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona.
Tale classe deve avere due attributi privati di tipo String, uno per il nome ed uno per il cognome,
ed un attributo privato di tipo int per l'età.

- La classe Persona deve avere i seguenti metodi:

    init(first_name, last_name):
    Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo,
    impostare a None l'attributo che non risulta essere una stringa, stampando un messaggio di errore,
    ad esempio, "Il nome inserito non è una stringa!".
    Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona;
    se first_name e last_name non sono due stringhe, allora assegnare None all'età.

    setName(first_name):
    Consente di impostare il nome di una persona, modificando il valore del relativo attributo.
    Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario,
    stampare un messaggio di errore, ad esempio "Il nome inserito non è una stringa!".

    setLastName(last_name):
    Consente di impostare il cognome di una persona, modificando il valore del relativo attributo.
    Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario,
    stampare un messaggio di errore, ad esempio "Il cognome inserito non è una stringa!".

    setAge(age):
    Consente di impostare l'età di una persona, modificando il valore del relativo attributo.
    Il valore viene modificato se e solo se viene passato al metodo un numero intero.
    In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere un numero intero!".

    getName(): consente di ritornare il nome di una persona.

    getLastname(): consente di ritornare il cognome di una persona.

    getAge(): consente di ritornare l'età di una persona.

    greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"
'''

class Person:

    __first_name: str
    __last_name: str
    __age: int

    def __init__(self, first_name: str, last_name: str) -> None:
        self.__first_name = first_name if isinstance(first_name, str) else None
        self.__last_name = last_name if isinstance(last_name, str) else None
        self.__age = 0 if self.__first_name and self.__last_name else None

        if self.__first_name is None:
            print("Il nome inserito non è una stringa!")
        
        if self.__last_name is None:
            print("Il cognome inserito non è una stringa!")

    def __str__(self) -> str:
        return f"Nome: {self.__first_name}\nCognome: {self.__last_name}\nEtà: {self.__age}"

    def setName(self, first_name: str) -> None:
        if isinstance(first_name, str):
            self.__first_name = first_name

            if self.__last_name:
                self.__age = 0

        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self, last_name: str) -> None:
        if isinstance(last_name, str):
            self.__last_name = last_name

            if self.__first_name:
                self.__age = 0

        else:
            print("Il cognome inserito non è una stringa!")

    def setAge(self, age: int) -> None:
        if isinstance(age, int) and age >= 0:
            self.__age = age

        else:
            print("L'età deve essere un numero intero!")

    def getName(self) -> str|None:
        return self.__first_name

    def getLastName(self) -> str|None:
        return self.__last_name

    def getAge(self) -> int|None:
        return self.__age

    def greet(self) -> None:
        if isinstance(self.__age, int):

            print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")

if __name__ == "__main__":

    p1: Person = Person(4, 2)
    p1.setName("Agamennone")
    p1.setLastName("Sbadalacci")
    p1.setAge(57)
    # print(p1)
    # # print(p1.getName())
    p1.greet()