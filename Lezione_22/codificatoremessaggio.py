'''
# Codificatori Messaggio

Si crei una classe astratta chiamata CodificatoreMessaggio che ha
un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare.
Il metodo restituirà il messaggio codificato.

Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo astratto decodifica(testoCodificato),
dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio.
Il costruttore dovrebbe ricevere un numero intero chiamato chiave.
Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.

Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e',
la lettera 'c' sarà sostituita da 'f' e così via.

    Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c
    da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio.
Il costruttore dovrebbe ricevere un numero intero chiamato n.
Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte.
Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato.

Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi'
(nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà).

Il messaggio combinato è 'afbgchdie'.

    Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e
    ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).


Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

    Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che
    compie un'azione inversa al metodo sposta_carattere().

    Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che
    compie un'azione inversa al metodo combinazione().


Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file
per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

### Test tramite codice driver:
Test del Cifratore a Scorrimento:
- Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

Test del Cifratore a Combinazione:
- Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
- Lettura del testo: Il testo in chiaro viene letto da un file.
- Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
- Scrittura del testo codificato: Il testo codificato viene scritto su un file.
- Stampa del testo codificato: Il testo codificato viene stampato.
- Decodifica: Il testo codificato viene decodificato.
- Stampa del testo decodificato: Il testo decodificato viene stampato.

'''

import os

from abc import ABC, abstractmethod
from string import ascii_lowercase, ascii_uppercase

class CodificatoreMessaggio(ABC):
    '''
    Si crei una classe astratta chiamata CodificatoreMessaggio che ha
    un solo metodo astratto codifica(testoInChiaro), dove testoInChiaro sarà il messaggio da codificare.
    Il metodo restituirà il messaggio codificato.
    '''

    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass

class DecodificatoreMessaggio(ABC):
    '''
    Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo astratto decodifica(testoCodificato),
    dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.
    '''

    @abstractmethod
    def decodifica(self, testoCodificato) -> str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    '''
    Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio.
    Il costruttore dovrebbe ricevere un numero intero chiamato chiave.
    Si definisca il metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.

    Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e',
    la lettera 'c' sarà sostituita da 'f' e così via.

        Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di un singolo carattere c
        da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).
    '''

    _chiave: int

    def __init__(self, chiave: int) -> None:
        self._chiave = chiave

    def codifica(self, testoInChiaro: str) -> str:
        testoCodificato: str = ""
        for caratt in testoInChiaro:

            testoCodificato += self._sposta_carattere(caratt)

        return testoCodificato

    def _sposta_carattere(self, caratt: str) -> str:
        for lower_c, upper_c in zip(ascii_lowercase, ascii_uppercase):

            if caratt == lower_c:
                ind_low_codificato: int = (ascii_lowercase.index(lower_c) + self._chiave) % 26
                car_low_codificato: str = ascii_lowercase[ind_low_codificato]

                return car_low_codificato

            elif caratt == upper_c:
                ind_upp_codificato: int = (ascii_uppercase.index(upper_c) + self._chiave) % 26
                car_upp_codificato: str = ascii_uppercase[ind_upp_codificato]

                return car_upp_codificato   

        return caratt

    def decodifica(self, testoCodificato: str) -> str:
        '''
        Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

            Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che
            compie un'azione inversa al metodo sposta_carattere().

        '''

        testo_decodificato: str = ""
        for caratt in testoCodificato:

            testo_decodificato += self._decodifica_carattere(caratt)

        return testo_decodificato

    def _decodifica_carattere(self, caratt: str) -> str:
        for lower_c, upper_c in zip(ascii_lowercase, ascii_uppercase):

            if caratt == lower_c:
                ind_low_codificato: int = (ascii_lowercase.index(lower_c) - self._chiave) % 26
                car_low_codificato: str = ascii_lowercase[ind_low_codificato]

                return car_low_codificato

            elif caratt == upper_c:
                ind_upp_codificato: int = (ascii_uppercase.index(upper_c) - self._chiave) % 26
                car_upp_codificato: str = ascii_uppercase[ind_upp_codificato]

                return car_upp_codificato   

        return caratt

    def leggereFile(self, file_name: str, mode: str = "r", encoding: str = "utf-8") -> None:
        '''
        Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file
        per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

        TESTO NORMALE -> TESTO CIFRATO
        '''

        with open(file_name, mode=mode, encoding=encoding) as f:

            return f.read()

    def scrivereFile(self, testo: str, file_name: str, mode: str = "w", encoding: str = "utf-8") -> None:
        '''Percorso di default /Lezione_22'''

        path_file: str = "/home/its/ITS-esercizi/Lezione_22/"
        full_path: str = os.path.join(path_file, file_name)

        testo_codificato: str = self.codifica(testo)
        with open(full_path, mode=mode, encoding=encoding) as f:

            f.write(testo_codificato)

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    '''
    Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio.
    Il costruttore dovrebbe ricevere un numero intero chiamato n.

    Si definisca il metodo codifica(testoInChiaro) così che il messaggio sia combinato n volte.
    Per eseguire una singola combinazione, si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato.

    Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi'
    (nel caso in cui la lunghezza del testo da decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà).

    Il messaggio combinato è 'afbgchdie'.

        Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e
        ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).
    '''

    _n: int

    def __init__(self, n: int) -> None:
        self._n = n

    def codifica(self, testoInChiaro: str) -> str:
        testo: str = testoInChiaro
        for _ in range(self._n):

            testo = self._combinazione(testo)

        return testo

    def _combinazione(self, testo: str) -> str:
        meta_stringa: int = (len(testo) + 1) // 2
        prima_meta: str = testo[:meta_stringa]
        seconda_meta: str = testo[meta_stringa:]
        frase_combinata: str = ""

        while prima_meta != "" or seconda_meta != "":

            if seconda_meta != "":
                frase_combinata += prima_meta[0] + seconda_meta[0]

            else:
                frase_combinata += prima_meta[0]

            prima_meta = prima_meta[1:]
            seconda_meta = seconda_meta[1:]

        return frase_combinata

    def decodifica(self, testoCodificato):
        '''
        Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

            Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che
            compie un'azione inversa al metodo combinazione().
        '''

        testo: str = testoCodificato
        for _ in range(self._n):

            testo = self._decodifica_combinazione(testo)

        return testo

    def _decodifica_combinazione(self, testo: str) -> str:
        prima_meta_orig: str = ""
        seconda_meta_orig: str = ""

        for i, l in enumerate(testo):

            if i % 2 == 0:
                prima_meta_orig += l

            else:
                seconda_meta_orig += l

        return prima_meta_orig + seconda_meta_orig

    def leggereFile(self, file_name: str, mode: str = "r", encoding: str = "utf-8") -> None:
        '''
        Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo cifrato su un file
        per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

        TESTO CIFRATO -> TESTO NORMALE
        '''

        with open(file_name, mode=mode, encoding=encoding) as f:

            return f.read()

    def scrivereFile(self, testo: str, file_name: str, mode: str = "w", encoding: str = "utf-8") -> None:
        '''Percorso di default /Lezione_22'''

        path_file: str = "/home/its/ITS-esercizi/Lezione_22/"
        full_path: str = os.path.join(path_file, file_name)

        testo_codificato: str = self.codifica(testo)        
        with open(full_path, mode=mode, encoding=encoding) as f:

            f.write(testo_codificato)

if __name__ == "__main__":
    '''
    ### Test tramite codice driver:
    Test del Cifratore a Scorrimento:
    1 - Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
    2 - Lettura del testo: Il testo in chiaro viene letto da un file.
    3 - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
    4 - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
    5 - Stampa del testo codificato: Il testo codificato viene stampato.
    6 - Decodifica: Il testo codificato viene decodificato.
    7 - Stampa del testo decodificato: Il testo decodificato viene stampato.
    '''

    print('=' * 80)
    print("TEST DEL CIFRATORE A SCORRIMENTO")

    # 1
    oggetto1: CifratoreAScorrimento = CifratoreAScorrimento(3)

    # 2
    testo1: str = """
    Taci. 
    Su le soglie del bosco non odo parole che dici umane; 
    ma odo parole più nuoveche parlano gocciole e foglie lontane. 
    Ascolta.
    Piove dalle nuvole sparse.
    """

    # 3
    print(oggetto1.codifica(testo1))

    # 4
    file_codificato: str = "/home/its/ITS-esercizi/Lezione_22/testo_codificato.txt"
    oggetto1.scrivereFile(testo1, file_codificato)

    # 5
    with open(file_codificato, "r", encoding="utf-8") as f:
        print(f.read())

    # 6
    testo_codificato: str = ""
    testo_decodificato: str = ""
    with open(file_codificato, "r", encoding="utf-8") as f:
        testo_codificato = f.read()
    
    testo_decodificato = oggetto1.decodifica(testo_codificato)

    # 7
    print(testo_decodificato)

    '''
    ### Test del Cifratore a Combinazione:
    1 - Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
    2 - Lettura del testo: Il testo in chiaro viene letto da un file.
    3 - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
    4 - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
    5 - Stampa del testo codificato: Il testo codificato viene stampato.
    6 - Decodifica: Il testo codificato viene decodificato.
    7 - Stampa del testo decodificato: Il testo decodificato viene stampato.
    '''

    print('=' * 80)
    print("TEST DEL CIFRATORE A COMBINAZIONE")

    # 1
    oggetto2: CifratoreACombinazione = CifratoreACombinazione(3)

    # 2
    testo2: str = """
    Sempre caro mi fu quest'ermo colle,
    E questa siepe, che da tanta parte
    Dell'ultimo orizzonte il guardo esclude.
    """

    # 3
    print(oggetto2.codifica(testo2))

    # 4
    file_codificato2: str = "/home/its/ITS-esercizi/Lezione_22/testo_codificato2.txt"
    oggetto2.scrivereFile(testo2, file_codificato2)

    # 5
    with open(file_codificato2, "r", encoding="utf-8") as f:
        print(f.read())

    # 6
    testo_codificato2: str = ""
    testo_decodificato2: str = ""
    with open(file_codificato2, "r", encoding="utf-8") as f:
        testo_codificato2 = f.read()
    
    testo_decodificato2 = oggetto2.decodifica(testo_codificato2)

    # 7
    print(testo_decodificato2)
    print('=' * 80)