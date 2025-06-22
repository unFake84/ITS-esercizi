'''
Mostri Contro Alieni
'''

# Creatura
from string import ascii_letters
# Alieno(Creatura)
import random
# main
import os, time

class Creatura:
    '''
    Definire le seguente classe con attributi privati:

    Creatura con le seguenti proprietà:
    - attributi: nome (di tipo stringa, per indicare il nome della creatura)
    - metodi: tutti i metodi standard, ovvero __init__, setter, getter e __str__
    In particolare:

        - il metodo setNome() deve fare un controllo se il nome inserito sia una stringa valida.
          In caso contrario, impostare il nome della creatura con il valore di "Creatura Generica".

        - il metodo __str__ deve mostrare in output: "Creatura: nome creatura"
    '''
    __nome: str
    __numCreatGeneriche: int = 0    #<- Tot creature generiche (ovvero corrette)
    __numCreat: int = 0             #<- Tot creature create (di ogni tipo)
    __numIdCreat: int = 0           #<- se è la 100a creatura il suo id univoco è 100 

    def __init__(self, nome: str) -> None:
        __nomeAssegnato: bool = False

        if not isinstance(nome, str):
            Creatura.__numCreatGeneriche += 1
            self.__nome, nome = f"Creatura Generica n°{Creatura.__numCreatGeneriche}", f"Creatura Generica n°{Creatura.__numCreatGeneriche}"
            __nomeAssegnato = True

        if not __nomeAssegnato:
            for lettera in nome:

                if lettera in ascii_letters:
                    self.__nome = nome
                    __nomeAssegnato = True
                    break

            else:
                Creatura.__numCreatGeneriche += 1
                self.__nome = f"Creatura Generica n°{Creatura.__numCreatGeneriche}"

        Creatura.__numCreat += 1
        self.__numIdCreat = Creatura.__numCreat

    def __str__(self) -> str:
        return f"Creatura n°{self.__numIdCreat}: {self.getNome()}"

    def setNome(self, nuovoNome: str) -> None:
        if not isinstance(nuovoNome, str):
            Creatura.__numCreatGeneriche += 1
            self.__nome, nuovoNome = f"Creatura Generica n°{Creatura.__numCreatGeneriche}", "Creatura Generica"

        if nuovoNome != "Creatura Generica":
            for nuovaLettera in nuovoNome:

                if nuovaLettera in ascii_letters:
                    self.__nome = nuovoNome
                    break

            else:
                Creatura.__numCreatGeneriche += 1
                self.__nome = f"Creatura Generica n°{Creatura.__numCreatGeneriche}"

        else:
            Creatura.__numCreatGeneriche += 1
            self.__nome = nuovoNome + f" n°{Creatura.__numCreatGeneriche}"

    def getNome(self) -> str:
        return self.__nome

    def getTotCreat(self) -> int:
        return Creatura.__numCreat

    def getTotGeneriche(self) -> int:
        return Creatura.__numCreatGeneriche

class Alieno(Creatura):
    '''
    Definire le seguente classe con attributi privati:

    Alieno (che eredita da Creatura) con le seguenti proprietà:
    - attributi: matricola (di tipo intero positivo), munizioni (una lista di 15 interi positivi)
    - metodi: setter, getter, __str__
    In particolare:

        - il metodo setMatricola() (privato), non riceve argomenti in input e deve inizializzare l'attributo matricola
          con un numero intero positivo casuale tra 10000 e 90000.

    Per generare un numero intero casuale nell'intervallo [a, b] (ovvero estremi inclusi), importare il modulo random
    e usare la funzione randint(a,b) del modulo; 

        - il metodo setMunizioni() (privato) non riceve argomenti in input e deve inizializzare l'attributo munizioni
          con una lista di 15 numeri interi positivi i cui elementi sono numeri della sequenza 0, 1, 4, 9, 16, 25, 36, 49, ...
          Usare le list comprehension.

          il metodo __init__ deve inizializzare la superclasse, inizializzare la matricola e le munizioni.

    Inoltre, i nomi di tutti gli alieni devono essere "Robot-" + matricola (ad esempio, "Robot-16326", scritto con la R maiuscola).
    Pertanto, nel metodo __init__ impostare il nome dell'Alieno come richiesto, effettuando opportuni controlli.
    Nel caso in cui il nome dell'alieno non sia conforme, mostrare il seguente messaggio e re-impostare il nome in modo corretto:
    "Attenzione! Tutti gli Alieni devono avere il nome "Robot" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!".

        - il metodo __str__ deve mostrare in output: "Alieno: nome alieno" (ad esempio: Alieno: Robot-16326)
    '''
    __numIdAlien: int = 0   #<- se è il 100° alieno il suo id univoco è 100 tra gli Alieni
    __contAlieni: int = 0   #<- quanti alieni ci sono nel sistema

    def __init__(self, nome: str = "Robot") -> None:
        super().__init__(nome)

        self.__setMatricola()
        self.__setMunizioni()

        if nome == "Robot":
            nomeCorretto: str = nome + "-" + str(self.__matricola)
            self.setNome(nomeCorretto)

        else:
            print(
                "Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola!\n"
                    "Reimpostazione nome Alieno in Corso!"
            )

            nomeReimpostato: str = "Robot-" + str(self.__matricola)
            self.setNome(nomeReimpostato)

        Alieno.__contAlieni += 1
        self.__numIdAlien = Alieno.__contAlieni

    def __str__(self) -> str:
        #return f"{super().__str__()} - Alieno n°{self.__numIdAlien}: {self.getNome()} con {max(self.getMunizioni())} munizioni"
        return f"Alieno: {self.getNome()}"

    def __setMatricola(self) -> None:
        self.__matricola = random.randint(10000, 90000)

    def __setMunizioni(self) -> None:
        self.__munizioni = [n**2 for n in range(15)]

    def getMatricola(self) -> int:
        return self.__matricola

    def getMunizioni(self) -> list[int]:
        return self.__munizioni

    def getTotAlieni(self) -> int:
        return Alieno.__contAlieni

class Mostro(Creatura):
    '''
    Definire le seguente classe con attributi privati:

    Mostro (che eredita da Creatura) con le seguenti proprietà:
        - attributi: urlo_vittoria (di tipo stringa), gemito_sconfitta (di tipo stringa), assalto (una lista di 15 interi positivi)
        - metodi: setter, getter, __str__

    In particolare:

    - il metodo __init__ deve ricevere il nome del mostro, il suo urlo della vittoria ed il suo gemito sconfitta.
      Inoltre, deve inizializzare assalto.

    - il metodo setAssalto() (privato) non riceve argomenti in input e deve inizializzare l'attributo assalto 
      una lista di 15 numeri interi positivi casuali tra 1 e 100, estremi inclusi, tutti diversi tra loro.

    - i metodi setVittoria(vittoria: str) e setSconfitta(sconfitta: str) (privati), devono controllare
      se i valori di vittoria e sconfitta siano valori validi.
      In caso contrario, devono impostare gli attributi urlo_vittoria a "GRAAAHHH" e gemito sconfitta a "Uuurghhh".

    - ad esempio, se il nome del mostro è "Godzilla", il metodo __str__ dovrà mostrare a schermo: Mostro: gOdZiLlA,
      ovvero il nome del mostro scritto con i caratteri alternati minuscolo-maiuscolo.
    '''
    __assalto: list[int]
    __vittoria: str
    __sconfitta: str
    __numIdMostro: int = 0    #<- ved.Creatura/Alieno
    __contMostro: int = 0     #<- ved.Creatura/Alieno

    def __init__(self, nome: str, urloVittoria: str, gemitoSconfitta: str) -> None:
        super().__init__(nome)

        self.__setAssalto()
        self.__setVittoria(urloVittoria)
        self.__setSconfitta(gemitoSconfitta)
        Mostro.__contMostro += 1
        self.__numIdMostro = Mostro.__contMostro

    def __str__(self) -> str:
        nome: str = Mostro.getNome(self)
        # [<<espressione_if_true>> if condizione else <<espressione_if_false>> for elemento in iterabile]
        nOmE: str = ''.join([nome[n].lower() if n%2 == 0 else nome[n].upper() for n in range(len(nome))])
        return f"Mostro: {nOmE}"

        # USATO PER TEST
        # return f"{super().__str__()} - {nOmE} - Mostro n°{self.__numIdMostro} vitt = {self.__vittoria} sconf = {self.__sconfitta}"

    def __setAssalto(self) -> None:
        self.__assalto = random.sample(range(1, 101), 15)

    def __setVittoria(self, checkUrlo: str) -> None:
        if not isinstance(checkUrlo, str):
            checkUrlo = "GRAAAHHH"

        checkUrloCaratt: bool = False

        for caratt in checkUrlo:

            if caratt in ascii_letters:
                checkUrloCaratt = True

        if not checkUrloCaratt:
            self.__vittoria = "GRAAAHHH"

        else:
            self.__vittoria = checkUrlo

    def __setSconfitta(self, checkGemito: str) -> None:
        if not isinstance(checkGemito, str):
            checkGemito = "Uuurghhh"

        checkGCaratt: bool = False

        for caratt in checkGemito:

            if caratt in ascii_letters:
                checkGCaratt = True

        if not checkGCaratt:
            self.__sconfitta = "Uuurghhh"

        else:
            self.__sconfitta = checkGemito

    def getTotMostri(self) -> int:
        return Mostro.__contMostro

    def getAssalto(self) -> list[int]:
        return self.__assalto

    def getVittoria(self) -> str:
        return self.__vittoria

    def getSconfitta(self) -> str:
        return self.__sconfitta

def pariUguali(a: list[int], b: list[int]) -> list[int]:
    '''
    Definire la seguente funzione:

        pariUguali(a: list[int], b: list[int]).
        Questo metodo riceve in input due liste a e b di interi positivi e deve restituire una lista c.

    Ogni elemento della lista c deve essere uguale a:
    - 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
    - 0 altrimenti
    '''
    if not isinstance(a, list)\
    or not isinstance(b, list)\
    or len(a) != len(b):
        raise ValueError("Devono essere liste e di uguali lunghezze")

    for j, k in zip(a, b):
        if not isinstance(j, int) or not isinstance(k, int):
            raise ValueError("I valori all'interno delle liste devono essere interi")

    return [1 if j%2 == 0 and k%2 == 0 else 0 for j, k in zip(a, b)]

def combattimento(a: Alieno, m: Mostro) -> str|None:
    '''
    Definire la seguente funzione:

        combattimento(a: Alieno, m: Mostro).
        Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto della classe Mostro.
        Il metodo deve controllare la validità di a e la validità di m.
        Se a non è un Alieno o se m non è un Mostro, il combattimento deve essere interrotto,
        mostrare un opportuno messaggio e ritornare None.
        Altrimenti, se a e m sono oggetti validi, il metodo deve simulare il combattimento tra Mostro e Alieno,
        restituendo la creatura vincitrice.
        Il combattimento consiste nell'applicare la funzione pariUguali() alle munizioni dell'Alieno e all'assalto del Mostro.
        Se la lista prodotta in output dal pariUguali() ha più di 4 elementi con valore 1, allora il vincitore è il mostro.
        Altrimenti, il vincitore è l'alieno.
        Se vince il mostro, sullo schermo viene stampato per 3 volte l'urlo della vittoria,
        altrimenti viene stampato il gemito della sconfitta.
    '''
    if not isinstance(a, Alieno)\
        or not isinstance(m, Mostro):
        print(
            "Devono essere inseriti un Alieno e un Mostro,\n"
            "in questo ordine:\n"
            "combattimento(Alieno, Mostro)\n"
            )
        return None

    munizioniAlieno: list[int] = Alieno.getMunizioni(a)
    assaltoMostro: list[int] = Mostro.getAssalto(m)
    risultato: list[int] = pariUguali(munizioniAlieno, assaltoMostro)
    checkMostro: int = 0

    for uno in risultato:
        if uno == 1:
            checkMostro += 1

    if checkMostro > 4:
        return '\n'.join([Mostro.getVittoria(m)]*3)

        # return f"IL MOSTRO {Mostro.getNome(m)} WIN!! e dice:\n" + '\n'.join([Mostro.getVittoria(m)]*3)

    else:
        return Mostro.getSconfitta(m)

        # return f"L'ALIENO {Alieno.getNome(a)} WIN!!\n"\
        #     f"Il mostro {Mostro.getNome(m)} grugnisce '{Mostro.getSconfitta(m)}'"

def proclamaVincitore(c: Creatura) -> None:
    '''
    proclamaVincitore(c: Creatura).
    Questo metodo stampa a schermo se hanno vinto gli alieni o i mostri ( a seconda dell'oggetto c) e ,
    mostra il vincitore all'interno di un rettangolo con contorno di * come nell'esempio.


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

    Suggerimento:
        stampare prima il rettangolo vuoto, le cui dimensioni sono altezza 5 e lunghezza = lunghezza di c.__str__() + 10
        poi, modificare il codice in questo modo:
        quando si arriva alla riga centrale del rettangolo (ovvero i=2),
        si deve stampare il nome del vincitore al centro del rettangolo.

    per far questo si deve imporre la condizione i=2 e j=5. Se la condizione è verificata, stampare la creatura c (print(c), end=""),
    stampare 5 spazi vuoti e un * (print(     *), end="") e poi interrompere l'iterazione corrente.
    '''
    c: str = str(c)
    altezza: int = 5
    lunghezza: int = len(c) + 10        #<<- 27 - 2 = 25

    for i in range(altezza):

        if i == 0:
            print('*'*lunghezza)

        elif i == 2:
            print('*', c.center(lunghezza - 4),'*')

        elif i == 4:
            print('*'*lunghezza)

        else:
            i1ei3: int = lunghezza - 2
            print('*' + ' ' * i1ei3 + '*')

    '''
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

if __name__ == "__main__":

    alieno: Alieno = Alieno("Robot")
    mostro: Mostro = Mostro("Kaiju", "ROoaAAaRRR!!!", "BOOOOOOM!!!eD!!")
    esito: str|None = combattimento(alieno, mostro)

    alien_lista: list[int] = alieno.getMunizioni()
    mOnSt3r_lista: list[int] = mostro.getAssalto()
    alienAscii: str = """
       .--------.
     .'  _     _  `.       
    /     \   /     \     
   |   .,.     .,.  |     
    \        .     /      
     `.     @    .'
       `-.____.-'
        /\\\   \     
       /_/\\\ \ \\                                  /
   |||||||| ALIEN GUN ON >>>=======:::::::::::🔥   = BANG!BANG!BANG!
        \_____/                                   \\
"""
    alienAsciiWIN: str = """
       .--------.
     .'  _     _  `.       
    /     \   /     \     
   |   .,.     .,.  |     
    \        . _    /                               ~
     `.     \/    .'                              ~ ~
       `-.____.-'                                ~ 
        /\\\   \                                ~ ~
       /_/\\\ \ \\                               ~ ~    
   |||||||| ALIEN GUN OFF >>>=======::::::::::: ~ ~
        \_____/  
"""
    mosterAscii: str = """
 <>=======() 
(/\___   /|\\\          ()==========<>_
      \_/ | \\\        //|\   ______/ \)
        \_|  \\\      // | \_/
          \|\/|\_   //  /\/
           (oo)\ \_//  /
          //_/\_\/ /  |
         @@/  |=\  \  |
              \_=\_ \ |
      🔥        \==\ \|\_ 
    🔥 🔥    __(\===\(  )\\
   🔥 🔥    (((~) __(_/   |
 🔥 🔥 🔥        (((~) \  /
                 ______/ /
                 '------'
"""
    mosterAsciiWIN: str = """
 <>=======() 
(/\___   /|\\\ 
      \_/ | \\\ 
        \_|  \\\ 
          \|\/|\_ 
           (^^)\ \ ___
          //_/\_\/ --\\
         @@/  |=\  \  \\
              \_=\_ \  \\
                \==\ \|\\\ 
             __(\===\(  )\\
            (((~) __(_/  \/|
                 (((~) \  /
                 ______/ /
                 '------'
"""
    pre_incontro: list[int] = [1 if j%2 == 0 and k%2 == 0 else 0 for j, k in zip(alien_lista, mOnSt3r_lista)]
    scontro: list[int] = []
    totAlien: int = 0
    totMonster: int = 0

    os.system('clear')
    print(
        f"\n{alieno}\n"\
        f"Munizioni: {alieno.getMunizioni()}\n\n\n"
        f"{mostro}\n"\
        f"Assalto: {mostro.getAssalto()}\n\n"\
        f" Combattimento in inizializzazione ...\n"
        )
    time.sleep(1)

    if esito:

        while True:
            time.sleep(1)
            os.system('clear')

            scontro.append(pre_incontro[0]) if pre_incontro != [] else scontro.append("FINE")
            pre_incontro.pop(0) if pre_incontro != [] else pre_incontro.append("FINE")

            print(
                f"\n{alieno}\n"\
                f"Munizioni: {alien_lista}\n\n\n"\
                f"{mostro}\n"\
                f"Assalto: {mOnSt3r_lista}\n\n",\
                f"Combattimento ingaggiato\n" if scontro[-1] != 'FINE' else f"Combattimento terminato\n"
                )
            print(
                f"Esito combattimento ...\n\n" if scontro[-1] != "FINE" else f"Esito combattimento ...TERMINATO\n\n",\
                f"\nPunteggio Alieno: {totAlien/10:.2f} - {f'Colpi effettuati: {totAlien}' if scontro[-1] != 'FINE' else f'Tot colpi sferrati: {totAlien}'}"\
                f"\nPunteggio Mostro: {totMonster/5:.2f} - {f'Colpi effettuati: {totMonster}' if scontro[-1] != 'FINE' else f'Tot colpi sferrati: {totMonster}'}\n"
                )

            if scontro[-1] == "FINE":
                break

            if scontro[-1] == 1:
                totMonster += 1
                print(f"Round: {totAlien+totMonster}/15\t\tMossa attuale = [{scontro[-1] if scontro != [] else 'GO'}]\n\n",\
                         "⚔️ Il Mostro colpisce! ⚔️\n", mosterAscii, "\n")

            elif scontro[-1] == 0:
                totAlien += 1
                print(f"Round: {totAlien+totMonster}/15\t\tMossa attuale = [{scontro[-1] if scontro != [] else 'GO'}]\n\n",\
                     "🔫 L'Alieno colpisce! 🔫\n", alienAscii, "\n")

            print("\n")

        print(esito+"\n" if '\n' in esito else mostro.getSconfitta()+"\n")
        print('I mostri hanno vinto!\n' if '\n' in esito else 'Gli alieni hanno vinto!\n')

        if totMonster == 0 or totAlien == 0:
            print("\n!!SUPREME VICTORY!!\n")

        verA: float = totMonster/5
        verM: float = totAlien/10

        if round(verA, 3) == round(verM, 3):
            print("Stesso punteggio ma la spunta comunque il Mostro!")

        proclamaVincitore(mostro if '\n' in esito else alieno)
        print(mosterAsciiWIN if '\n' in esito else alienAsciiWIN)

    else:
        print("Combattimento annullato")





















    # # [TEST CREATURA]------------------------------
    # print("CREATURE:")
    # creatura1: Creatura = Creatura("Creatura 99#")
    # creatura2: Creatura = Creatura(125)
    # creatura3: Creatura = Creatura("Creatura-98#")
    # creatura4: Creatura = Creatura(521)
    # creatura5: Creatura = Creatura("Creatura!")
    # print(creatura1)
    # print(creatura2)
    # print(creatura3)
    # print(creatura4)
    # print(creatura5)
    # # [/TEST CREATURA]-----------------------------
    # print("")
    # # [TEST ALIENO]------------------------------
    # print("ALIENI:")
    # alieno1: Alieno = Alieno("Roboto")
    # alieno2: Alieno = Alieno("Robot")
    # print(alieno1)
    # print(alieno2)
    # # [/TEST ALIENO]------------------------------
    # print("")
    # # [TEST MOSTRO]
    # print("MOSTRI:")
    # mostro1: Mostro = Mostro("Godzillah", "Ohyeah", "nuuuuoooooooo")
    # mostro2: Mostro = Mostro("Kaiju", "ROoaAAaRRR!!!", "BOOOOOOM!!!eD!!")
    # mostro3: Mostro = Mostro("1234", "0342352", 1456)
    # print(mostro1)
    # print(mostro2)
    # print(mostro3)
    # # [/TEST MOSTRO]
    # print("")
    # # [LISTE]
    # print(pariUguali([12, 43, 44, 26], [74, 95, 101, 88]))
    # # [/LISTE]
    # print("")
    # # [TEST COMBATTIMENTO]
    # print(combattimento(alieno1, mostro1))
    # # [/TEST COMBATTIMENTO]
    # print("")
    # # [TEST VINCITORE]
    # proclamaVincitore(mostro1)
    # # [/TEST VINCITORE]
    # print("")
    # # [SOMMARIO CREATURE]
    # print(
    #     "CREATURE:\n"
    #     f"Creature con nome valido: {creatura5.getTotCreat() - creatura5.getTotGeneriche()}\n"
    #     f"Creature generiche: {creatura4.getTotGeneriche()}\n"
    #     f"Alieni: {alieno2.getTotAlieni()}\n"
    #     f"MOstRi: {mostro3.getTotMostri()}\n"
    #     f"Creature totali {creatura5.getTotCreat()}"
    # )
    # # [/SOMMARIO CREATURE]