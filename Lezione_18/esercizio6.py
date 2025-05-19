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

# creo classe da far convogliare le eccezioni personalizzate
class FractionErrors(Exception):

    pass

class Fraction:

    # dato che ho scelto dei dizionari ho bisogno dell eq per poter confrontrare le chiavi
    # tra oggetti in memorie diverse
    def __eq__(self, other: "Fraction"):

        return self.numeratore/self.denominatore == other.numeratore/other.denominatore
    
    # restituisce un intero che poi servirà per identificare i valori dentro i dizionari, tuple
    # dato che sono immutabili una volta create
    def __hash__(self):

        return hash((self.numeratore, self.denominatore))

    # comodo per poter stampare informazioni sulle frazioni per ora -| Originali | Semplificati |-
    def __str__(self):

        # inizializzo lista vuota
        display: list[str] = []

        # se esiste un dizionario con frazioni "originali" all'interno
        if self.frazioni:

            # per ogni indice[1>], creami una tupla contente il numeratore(key)
            # e il denominatore (value) e aggiungila alla lista (display)
            for i, (key, value) in enumerate(self.frazioni.items()):

                numeratore: str = str(key[0])
                denominatore: str = str(key[1])
                content: str = f"Original fraction {i + 1}: {numeratore}/{denominatore} - {value}"
                display.append(content)
        
        # se esiste anche un dizionario con frazioni "semplificate"
        if self.semplificate:

            # stesso ragionamento con le frazioni semplificate
            for i, (key, value) in enumerate(self.semplificate.items()):

                numeratore: str = str(key[0])
                denominatore: str = str(key[1])
                content: str = f"Simplified fraction {i + 1}: {numeratore}/{denominatore} - {value}"
                display.append(content)
        
        # se non esiste nessun dato
        else:

            display.append("No simplified fractions found.")
        
        # uso .join per poter aggiungere alla stringa "\n"
        return "\n".join(display)

        # numero: int = 1
        # display: dict[str, str] = {}

        # for key,value in self.frazioni.items():

        #     display[f"{key[0]}/{key[1]}"] = value

        # return f"{display}"

    # inizializzo due dizionari per immagazzinare le frazioni
    # le ho rese condivisibili con tutte le funzioni della classe
    frazioni: dict[tuple[int, int], str] = {}
    semplificate: dict[tuple[int, int], str] = {}

    # cominciamo ad inizializzare l'init
    # per ora si aspetta due numeri interi <- modificare con None per rispettare
    # il Null della traccia
    def __init__(self, numeratore: int, denominatore: int):

        # se il numeratore ed il denominatore sono interi e quest'ultimo è diverso da 0
        if isinstance(numeratore, int) and isinstance(denominatore, int) and denominatore != 0:

            # aggiungo dentro una tupla la frazione inserita
            self.numeratore = numeratore
            self.denominatore = denominatore            
            frazione: tuple[int, int] = (self.numeratore, self.denominatore)

            # se la frazione non è presente in nessuno dei due dizionari
            # utilizzo .keys nei dizionari per controllare direttamente le loro chiavi
            if frazione not in self.frazioni.keys() and frazione not in self.semplificate.keys():

                #| per ora la semplificazione viene chiamata ogni volta che si prova ad aggiungere 
                #| una frazione nella collezione "Original"
                self.frazioni[frazione] = "not yet simplified -> try @simplify()"
                self.simplify()

            # altrimenti già esiste e lancia un raise (da gestire)
            else:

                raise FractionErrors(f"Fraction {frazione[0]}/{frazione[1]} already exists.")

        # altrimenti:
        else:

            # se il denominatore è 0
            if denominatore == 0:

                raise FractionErrors("Denominator cannot be zero.")

            # se il tipo passato non è di tipo int
            raise FractionErrors("Numerator and Denominator must be of type int.")
        
    #| per ora la semplificazione viene chiamata ogni volta che si prova ad aggiungere 
    #| una frazione nella collezione "Original"
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

        # creo una variabile che mi cattura dentro un'altra tupla
        # i valori semplificati dopo la scomposizione (se fatta)
        semplificata: tuple[int, int] = numeratore_semplificato, denominatore_semplificato

        # se la frazione,ridotta ai minimi termini,
        # non è già presente nella collezione semplificate
        if semplificata not in self.semplificate:

            # se il numeratore ed il denominatore risulta già dentro la collezione semplificate
            if self.numeratore == numeratore_semplificato and self.denominatore == denominatore_semplificato: #-> fa la stessa cosa ma meno robusto come controllo-> #if semplificata in self.frazioni:

                # avviso che la frazione esiste già semplificata nella collezione
                self.semplificate[semplificata] = f"{self.numeratore}/{self.denominatore} fraction is already simplified."
                return semplificata
                                                            #return "This simplified fraction has already been inserted.", None # <- potrei sostituire con -semplificata- se mi serve da tenere traccia

            # altrimenti, se non presente, aggiungo la frazione nelle semplificate
            else:

                # # da modificare stringa se modifico il codice "in-place" (salvare anticipatamente le variabili)
                self.semplificate[semplificata] = f"Fraction simplified from: {self.numeratore}/{self.denominatore}"

        # altrimenti ritorno una stringa di avviso
        else:

            return "The fraction allready exist."

        # comunque vada ritorno la tupla con le frazioni
        return semplificata

# TEST senza unittest
if __name__ == "__main__":

    prova: Fraction = Fraction(6, 8)
    prova2: Fraction = Fraction(5, 10)
    prova3: Fraction = Fraction(7, 3)
    prova4: Fraction = Fraction(100, 10)
    prova3.simplify()# <----gestire 7/3 se rimanere su frazioni o passare in semplificate
    print(prova3)