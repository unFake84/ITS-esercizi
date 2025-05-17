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

class Fraction:

    def __eq__(self, other: "Fraction"):

        return self.numeratore/self.denominatore == other.numeratore/other.denominatore
    
    def __hash__(self):

        return hash((self.numeratore, self.denominatore))

    collezione: dict[int, int] = {}

    def __init__(self, numeratore: int, denominatore: int):

        if isinstance(numeratore, int) and isinstance(denominatore, int) and denominatore != 0:

            self.numeratore = numeratore
            self.denominatore = denominatore

        else:

            if denominatore == 0:

                raise ValueError("Denominator cannot be zero.")

            raise ValueError("Numerator and Denominator must be of type int.")
        
    def simplify(self) -> float:

        #if self.numeratore%1 == 0 and self.denominatore%1 == 0:
        pass