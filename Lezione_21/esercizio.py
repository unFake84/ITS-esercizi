'''
Testi Digitali
'''

import unittest

class Documento:
    '''
    Si definisca una classe Documento che contenga una variabile di tipo stringa chiamata testo e che
    memorizza qualsiasi contenuto testuale per il documento.
    Si crei un metodo getText() che restituisca il testo.
    Si crei un metodo setText() per impostare il testo.
    Scrivere un metodo isInText() che restituisce True se un documento contiene la parola chiave specificata.
    '''

    testo: str

    def __init__(self, ntesto: str) -> None:
        self.setText(ntesto)

    def __str__(self) -> str:
        print(f"Testo = {self.getText()}")

    def setText(self, ntesto: str) -> None:
        if not isinstance(ntesto, str):
            print("Inserire una stringa")
    
        self.testo = ntesto

    def getText(self) -> str:
        return self.testo
    
    def isInText(self, checktesto: str) -> bool:
        return True if checktesto in self.testo else False

class Email(Documento):
    '''
    Si definisca poi una classe Email che sia derivata da Documento e che includa le variabili per il mittente,
    il destinatario e il titolo del messaggio.
    Si implementino i metodi get() e set() appropriati per tali variabili.
    Il corpo del messaggio dell’e-mail dovrebbe essere memorizzato nella variabile ereditata testo.
    Si ridefinisca il metodo getText() per
    concatenare e ritornare tutti i campi di testo (mittente, destinatario, titolo del messaggio, e messaggio)
    come di seguito:
    
    Da: alice@example.com, A: bob@example.com
    Titolo: Incontro
    Messaggio: Ciao Bob, possiamo incontrarci domani?
    
    Inoltre, si implementi un metodo writeToFile() per
    scrivere il risultato del metodo getText() in un file di testo e in un percorso specificato.
    '''

    def __init__(self, ntesto, mittente: str, destinatario: str, titolo: str) -> None:
        super().__init__(ntesto)

        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitolo(titolo)

    def __str__(self):
        return super().__str__()

    def setMittente(self, setMitt: str) -> None:

        if not isinstance(setMitt, str):
            print("Non è una stringa")

        self.mittente = setMitt
    
    def setDestinatario(self, setDest: str) -> None:

        if not isinstance(setDest, str):
            print("Non è una stringa")

        self.destinatario = setDest

    def setTitolo(self, setTit: str) -> None:

        if not isinstance(setTit, str):
            print("Non è una stringa")

        self.titolo = setTit

    def getText(self) -> str:

        testo: str = f"\nDa: {self.getMittente()}, A: {self.getDestinatario()}\n"\
                    f"Titolo: {self.getTitolo()}\n"\
                    f"Messaggio: {super().getText()}\n"

        return testo

    def getMittente(self) -> str:
        return self.mittente

    def getDestinatario(self) -> str:
        return self.destinatario
    
    def getTitolo(self) -> str:
        return self.titolo
    
    def writeToFile(self):

        testo: str = self.getText()
        percorso: str = "/home/its/ITS-esercizi/Lezione_21/email1.txt"

        with open(percorso, "w") as file:
            file.write(testo)

class File(Documento):
    '''
    Analogamente, si definisca una classe File che sia derivata da Documento e includa una variabile per il nomePercorso.
    Crea un file document.txt con all'interno la stringa "Questo e' il contenuto del file." e
    salvalo in una directory a tua scelta e che sarà indicata in nomePercorso.
    I contenuti testuali del file dovrebbero essere letti da questo file di testo al percorso specificato in
    nomePercorso e memorizzati nella variabile ereditata testo tramite un metodo leggiTestoDaFile().
    Si ridefinisca il metodo getText() che concateni e ritorni il nome del percorso e il testo, come di seguito:
    
    Percorso: nomePercorso/document.txt
    Contenuto: Questo e' il contenuto del file.
    '''
    def __init__(self, nomePercorso: str  = "/home/its/ITS-esercizi/Lezione_21/document.txt") -> None:
        super().__init__(self.leggiTestoDaFile())
        self.nomePercorso = nomePercorso

    def leggiTestoDaFile(self):
        percorso: str = "/home/its/ITS-esercizi/Lezione_21/document.txt"

        with open(percorso, "r") as file:

            contenuto: str = file.read()
            return contenuto

    def getText(self):
        return f"Percorso: {self.nomePercorso}\n"\
                f"Contenuto: {super().getText()}"

if __name__ == "__main__":
    '''
    ### Test tramite codice driver:
    Creazione degli oggetti:

        Email: Viene creato un oggetto Email con mittente, destinatario, oggetto e corpo del messaggio.
        File: Viene creato un oggetto File specificando il percorso di un file esistente.

    Prova dei metodi:

        Stampa del testo dell'email: Viene stampato il testo del messaggio dell'email utilizzando il metodo getText().
        Stampa del testo del file: Viene stampato il contenuto del file utilizzando il metodo getText().

    Scrittura del contenuto dell'email su un file:

        Scrittura su file: Il contenuto dell'email viene scritto su un nuovo file chiamato email1.txt
        utilizzando il metodo writeToFile().

    Verifica della presenza di parole chiave:

        Email: Utilizzo del metodo isInText() per verificare se la parola 'incontrarci' è presente nel testo dell'email.
        Il risultato atteso è True.
        File: Utilizzo del metodo isInText() per verificare se la parola 'percorso' è presente nel testo del file.
        Il risultato atteso è False.
    '''
    email: Email = Email("Ciao come va?", "uccio@uccia.it", "uccia@uccio.it", "Ucciamo?")
    file: File =File()

    print(f"E\'stato creato l'oggetto email -> {email.getText()}")
    print(file.getText())
    print("\nCreato(o sovrascritto) file emai1.txt\n")

    email.writeToFile()

    print(email.isInText("come"))
    print(email.isInText("incontrarci"))

    '''
    ### Test con UnitTest

    Utilizzando il modulo unittest, definire i seguenti test per le classi Documento, Email e File.
    
    I test devono includere:

        Verifica dei metodi getText() e setText() nella classe Documento.
        Verifica del metodo isInText() nella classe Documento.
        Verifica del metodo getText() nella classe Email.
        Verifica del metodo writeToFile() nella classe Email.
        Verifica del metodo isInText() nella classe Email.
        Verifica del metodo getText() nella classe File.
        Verifica del metodo isInText() nella classe File.
    '''

    class TestDocumento(unittest.TestCase):

        def test_getText(self):
            test = Email("Ciao come va?", "uccio@uccia.it", "uccia@uccio.it", "Ucciamo?")
            self.assertEqual(test.getText(), "\nDa: uccio@uccia.it, A: uccia@uccio.it\nTitolo: Ucciamo?\nMessaggio: Ciao come va?\n")

        # def test_setText(self):
        #     settest = Email("bellaa")
        #     self.assertEqual(settest.setText(), "\nDa: uccio@uccia.it, A: uccia@uccio.it\nTitolo: Ucciamo?\nMessaggio: bellaa\n")
    
    unittest.main()


    # TEST GENERALI
    # print("\nDOCUMENTO\n")
    # i_testo: Documento = Documento("CiaoCiao")          # creo un oggetto Documenti
    # print(i_testo.getText())                           # "CiaoCiao"
    # print(i_testo.isInText("CiaoCiao"))                 # True

    # print("\nEMAIL\n")
    # primaMail: Email = Email("prova", "primo@uno.it", "secondo@due.it", "titolone")
    # print(primaMail.getText())
    # print("Provo a creare il file \"ProvaEsercizio.txt\"")
    # primaMail.writeToFile()
    # print("file creato correttamente!,\nda ora in poi\nogni volta che eseguo il programma\ncreo o sovrascrico il suddetto file")
    # print("\nTEST FILE\n")
    # secondaMail: File = File()
    # print(secondaMail.getText())