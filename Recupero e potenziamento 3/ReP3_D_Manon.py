'''
Mostri Contro Alieni

Definire le seguenti classi con attributi privati:


Alieno (che eredita da Creatura) con le seguenti proprietà:
- attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:

    il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola con un numero intero positivo casuale tra 10000 e 90000.

Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random e usare la funzione randint(a,b) del modulo;
 

    il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni con una lista di 15 numeri interi positivi i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ... Usare le list comprehension.

    il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.

Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli. Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto: "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".

    il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)


Mostro ( che eredita da Creatura) con le seguenti proprietà:
- attributi: urlo_vittoria (di tipo stringa), gemito_sconfitta (di tipo stringa), assalto (una lista di 15 interi positivi)
- metodi: setter, getter, __str__
In particolare:

    il metodo __init__ deve ricevere il nome del mostro, il suo urlo della vittoria ed il suo gemito sconfitta. Inoltre, deve inizializzare assalto.

    il metodo setAssalto() (privato) non riceve argomenti in input e deve inizializzare l'attributo assalto con una lista di 15 numeri interi positivi casuali tra 1 e 100, estremi inclusi, tutti diversi tra loro.

    i metodi setVittoria(vittoria: str) e setSconfitta(sconfitta: str) (privati), devono controllare se i valori di vittoria e sconfitta siano valori validi. In caso contrario, devono impostare gli attributi urlo_vittoria a "GRAAAHHH" e gemito sconfitta a "Uuurghhh".

    ad esempio, se il nome del mostro è "Godzilla", il metodo __str__ dovrà mostrare a schermo: Mostro: gOdZiLlA, ovvero il nome del mostro scritto con i caratteri alternati minuscolo-maiuscolo.



All'interno del file ReP3_inizialeNome_Cognome (fuori dalla classi) definire le seguenti funzioni:

    pariUguali(a: list[int], b: list[int]). Questo metodo riceve in input due liste a e b di interi positivi e deve restituire una lista c.

Ogni elementi della lista c deve essere uguale a:
- 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
- 0 altrimenti

    combattimento(a: Alieno, m: Mostro). Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto della classe Mostro. Il metodo deve controllare la validità di a e la validità di m. Se a non è un Alieno o se m non è un Mostro, il combattimento deve essere interrotto, mostrare un opportuno messaggio e ritornare None. Altrimenti, se a e m sono oggetti validi, il metodo deve simulare il combattimento tra Mostro e Alieno, restituendo la creatura vincitrice. Il combattimento consiste nell'applicare la funzione pariUguali() alle munizioni dell'Alieno e all'assalto del Mostro. Se la lista prodotta in output dal pariUguali() ha più di 4 elementi con valore 1, allora il vincitore è il mostro. Altrimenti, il vincitore è l'alieno. Se vince il mostro, sullo schermo viene stampato per 3 volte l'urlo della vittoria, altrimenti viene stampato il gemito della sconfitta.


    proclamaVincitore(c: Creatura). Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri ( a seconda dell'oggetto c) e , mostra il vincitore all'interno di un rettangolo con contorno di * come nell'esempio.


*****************************

*                           *

*    Alieno: Robot-25855    *

*                           *

*****************************

*************************

*                       *

*    Mostro: gOrThOr    *

*                       *

*************************

Suggerimento: stampare prima il rettangolo vuoto, le cui dimensioni sono altezza 5 e lunghezza = lunghezza di c.__str__() + 10
poi, modificare il codice in questo modo:
quando si arriva alla riga centrale del rettangolo (ovvero i=2), si deve stampare il nome del vincitore al centro del rettangolo.
per far questo si deve imporre la condizione i=2 e j =5. Se la condizione è verificata, stampare la creatura c (print(c), end=""), stampare 5 spazi vuoti e un * (print(     *), end="") e poi interrompere l'iterazione corrente.


Infine,

    Scrivere nel metodo main, un codice Python che

- Inizializza un mostro e un alieno e stampa i dati corrispondenti sullo schermo.
- Esegue un combattimento tra i due oggetti creati.
- Proclama il vincitore.


Esempio di Output:

Alieno: Robot-41119
Munizioni: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]


Mostro: gOrThOr
Assalto: [13, 23, 28, 80, 50, 56, 33, 55, 15, 20, 15, 94, 42, 16, 46]

Combattimento

GRAAAHHH
GRAAAHHH
GRAAAHHH


I Mostri hanno vinto!

*************************

*                       *

*    Mostro: gOrThOr    *

*                       *

*************************
'''

# Creatura
from string import ascii_letters
# Alieno(Creatura)
import random

class Creatura:
    '''
    Definire le seguenti classi con attributi privati:
    Creatura con le seguenti proprietà:
    - attributi: nome (di tipo stringa, per indicare il nome della creatura)
    - metodi: tutti i metodi standard, ovvero __init__, setter, getter e __str__
    In particolare:

    il metodo setNome() deve fare un controllo se il nome inserito sia una stringa valida.
    In caso contrario, impostare il nome della creatura con il valore di "Creatura Generica".

    il metodo __str__ deve mostrare in output: "Creatura: nome creatura"
    '''
    __nome: str
    __totCreatGen: int = 0
    __totCreat: int = 0
    __contStr: int = 0

    def __init__(self, nome: str) -> None:
        __nomeAssegnato: bool = False

        if not isinstance(nome, str):
            Creatura.__totCreatGen += 1
            self.__nome, nome = f"Creatura Generica n°{Creatura.__totCreatGen}", f"Creatura Generica n°{Creatura.__totCreatGen}"
            __nomeAssegnato = True

        if not __nomeAssegnato:
            for lettera in nome:

                if lettera in ascii_letters:
                    Creatura.__totCreat += 1
                    self.__nome = nome
                    __nomeAssegnato = True
                    break

            else:
                Creatura.__totCreatGen += 1
                self.__nome = f"Creatura Generica n°{Creatura.__totCreatGen}"

    def __str__(self) -> str:
        Creatura.__contStr += 1
        return f"Creatura n°{Creatura.__contStr}: {self.__nome}"
    
    def setNome(self, nuovoNome: str) -> None:
        if not isinstance(nuovoNome, str):
            self.__nome, nuovoNome = "Creatura Generica", "Creatura Generica"
        
        if nuovoNome != "Creatura Generica":
            for nuovaLettera in nuovoNome:

                if nuovaLettera in ascii_letters:
                    self.__nome = nuovoNome
                    break

            else:
                self.__nome = "Creatura Generica"

    def getNome(self) -> str:
        return self.__nome
    
class Alieno(Creatura):
    '''
    Definire le seguenti classi con attributi privati:
    Alieno (che eredita da Creatura) con le seguenti proprietà:
    - attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
    - metodi: setter, getter, __str__
    In particolare:

    il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola
    con un numero intero positivo casuale tra 10000 e 90000.

    Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random
    e usare la funzione randint(a,b) del modulo; 

    il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni
    con una lista di 15 numeri interi positivi i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ...
    Usare le list comprehension.

    il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.

    Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
    Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli.
    Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto:
    "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".

    il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)
    '''
    __contAlienStp: int = 0
    __contAlien: int = 0
    __matricola: int = 0
    __munizioni: list[int] = []

    def __init__(self, nome: str = "Robot-"):
        super().__init__(nome)
        self.__setMatricola()
        self.__setMunizioni()

        if nome == "Robot-":
            #self._Creatura__nome = nome + str(self.__matricola)
            nomeCorretto: str = nome + str(self.__matricola)
            self.setNome(nomeCorretto)
            Alieno.__contAlien += 1

        else:
            print(
                "Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola!\n"
                    "Reimpostazione nome Alieno in Corso!"
            )

            nomeReimpostato: str = "Robot-" + str(self.__matricola)
            self.setNome(nomeReimpostato)
            Alieno.__contAlien += 1
    
    def __setMatricola(self) -> None:
        self.__matricola = random.randint(10000, 90000)

    def __setMunizioni(self) -> None:
        self.__munizioni = [n**2 for n in range(15)]

    def __str__(self):
        # return str([str(m) for m in self.__munizioni])
        Alieno.__contAlienStp += 1
        return f"Alieno n°{self.__contAlienStp}: {self.getNome()}"

if __name__ == "__main__":

    # [TEST CREATURA]------------------------------
    provaNome: Creatura = Creatura("Creatura 99#")
    provaNome2: Creatura = Creatura(125)
    provaNome3: Creatura = Creatura("Creatura-98#")
    provaNome4: Creatura = Creatura(521)
    provaNome5: Creatura = Creatura("Creatura!")
    print(provaNome)
    print(provaNome2)
    print(provaNome3)
    print(provaNome4)
    print(provaNome5)
    # [/TEST CREATURA]-----------------------------

    # [TEST ALIENO]------------------------------
    alieno1: Alieno = Alieno("Roboto-")
    alieno2: Alieno = Alieno("Robot-")
    print(alieno1)
    print(alieno2)
    # [/TEST ALIENO]------------------------------