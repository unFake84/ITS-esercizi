'''
Personalized math library:
Create a Python library that provides functions for handling fractions, with built-in error handling.
The library must include functions for the following operations:

    Create a fraction from the numerator and denominator.
    Collect the numerator and denominator of a fraction.
    Simplify a fraction.
    Add, subtract, multiply and divide fractions.
    Check whether one fraction is equivalent to another. 

    All library functions must use the try-except block to handle potential errors,
    such as null denominators, unsupported operations, or division by zero.
    The library must raise custom exceptions to indicate specific errors to the user.
'''

class FractionErrors(Exception):

    pass

class Fraction:

    def __eq__(self, other: "Fraction"):

        return self.numeratore/self.denominatore == other.numeratore/other.denominatore
    
    def __hash__(self):

        return hash((self.numeratore, self.denominatore))

    def __str__(self):

        display: list[str] = []

        if self.frazioni:

            for i, (key, value) in enumerate(self.frazioni.items()):

                numeratore: str = str(key[0])
                denominatore: str = str(key[1])
                content: str = f"Frazione {i + 1}: {numeratore}/{denominatore} - {value}"
                display.append(content)
        
        if self.semplificate:

            for i, (key, value) in enumerate(self.semplificate.items()):

                numeratore: str = str(key[0])
                denominatore: str = str(key[1])
                content: str = f"Frazione semplificata {i + 1}: {numeratore}/{denominatore} - {value}"
                display.append(content)
        
        else:

            display.append("No fractions in database")
        
        return "\n".join(display)

        # numero: int = 1
        # display: dict[str, str] = {}

        # for key,value in self.frazioni.items():

        #     display[f"{key[0]}/{key[1]}"] = value

        # return f"{display}"

    frazioni: dict[tuple[int, int], str] = {}
    semplificate: dict[tuple[int, int], str] = {}

    def __init__(self, numeratore: int, denominatore: int):

        if isinstance(numeratore, int) and isinstance(denominatore, int) and denominatore != 0:

            self.numeratore = numeratore
            self.denominatore = denominatore            
            frazione: tuple[int, int] = (self.numeratore, self.denominatore)

            if frazione not in self.frazioni.keys() and frazione not in self.semplificate.keys():

                self.frazioni[frazione] = "Fraction to be simplified"
                self.simplify()

            else:

                raise FractionErrors("Same fraction allready exist")

        else:

            if denominatore == 0:

                raise FractionErrors("Denominator cannot be zero.")

            raise FractionErrors("Numerator and Denominator must be of type int.")
        
    def simplify(self) -> float:

        # prendo il numero più piccolo tra numeratore e denominatore,
        # che mi servirà per trovare il Massimo Comune Divisore (MCD)
        numero_minore: int = min(self.numeratore, self.denominatore)

        # cerco il MCD partendo dal numero più piccolo e scendendo fino a 1
        # - mentre il numero_minore è maggiore di 1: -
        while numero_minore >= 1:

            # - se il numero+piccolo("numero_minore") divide sia il numeratore che il denominatore: -
            if self.numeratore%numero_minore == 0 and self.denominatore%numero_minore == 0:

                # allora "numero_minore" è il MDC.
                # divido entrambi per il MCD per ottenere la frazione semplificata.
                # l'operatore // mi assicura che restituisce un intero
                numeratore_semplificato: int = self.numeratore // numero_minore
                denominatore_semplificato: int = self.denominatore // numero_minore
                break

            # se "numero_minore" non è un divisore comune, lo decremento
            else:

                numero_minore -= 1

        semplificata: tuple[int, int] = numeratore_semplificato, denominatore_semplificato

        if semplificata not in self.semplificate:

            if semplificata in self.frazioni:

                return f"{self.numeratore}/{self.denominatore} it's allready a simply fraction"

            else:

                # # da modificare stringa se modifico il codice "in-place" (salvare anticipatamente le variabili)
                self.semplificate[semplificata] = f"fraction simplied from: {self.numeratore}/{self.denominatore}"

        else:

            return "The fraction allready exist."

        return semplificata

if __name__ == "__main__":

    prova: Fraction = Fraction(6, 8)
    prova2: Fraction = Fraction(5, 10)
    prova3: Fraction = Fraction(7, 3)
    prova4: Fraction = Fraction(100, 10)
    #prova3.simplify()# <----gestire 7/3 se rimanere su frazioni o passare in semplificate
    print(prova3)