'''
Database of dates:

1.
    Write a class that manages a database of dateswith the format gg.mm.aaaa
2.
    implementing methods to add a new date,
    delete a given date,
    modify a date,
    and perform a query on a given date is required.
3.
    A query on a given date allows for retrieving a given new date.
    Note that a date is an object for your database;
    it must be instantiated from a string.

'''

from datetime import datetime

class Date:

    def __init__(self, date: str):

        # proviamo se l'input è un tipo 'corretto' = data corretta
        try:

            # # STRING 'PARSE' TIME
            # self.date acquisisce la stringa in input e la converte in un oggetto datetime.date nel formato "gg.mm.aaaa"
            # strptime converte la stringa in formato gg.mm.aaaa in un oggetto datetime
            self.date = datetime.strptime(date, "%d.%m.%Y").date()

        # se è una data non valida lancio un eccezione, e per il 'momento' blocco il programma
        except ValueError:

            # motivando che la data non è valida
            raise ValueError("Date not valid")
        
    # per comparare due oggetti che hanno posizioni diverse in memoria
    # altrimenti qualsiasi comparazione restituirà sempre False
    def __eq__(self, other: "Date"):

        # se la data è uguale ad un altra data
        # ritorno True
        return self.date == other.date                   # -> da verificare se non è + necessario: -> if self.date is True else None
    
    # necessario per mostrare le date e non le locazioni in memoria
    def __str__(self):

        # # STRING 'FORMAT' TIME
        # Converte l'oggetto datetime.date in una stringa nel formato "gg.mm.aaaa"
        # strftime formatta l'oggetto datetime in una stringa nel formato gg.mm.aaaa
        convert_to_str: str = self.date.strftime("%d.%m.%Y")
        
        # ritorno la stringa formattata
        return convert_to_str

# 1.
class Database:

    # prende una data
    def __init__(self, dates = None):

        # inizializzo una lista vuota
        self.personal_db: list[Date] = []

        # <se1> l'input avviene
        if dates is not None:

            # <se2> è una lista
            if isinstance(dates, list):

                # <per> ogni chiave+elemento nella lista
                for key, elem in enumerate(dates):

                    # <se3> il valore rispetta il tipo
                    if isinstance(elem, Date):

                        # aggiungo con .append l' elemento(la data) nella lista
                        self.personal_db.append(elem)

                    # </se3> allora lancio un errore dicendo in quale chiave il valore non è corretto
                    else:

                        raise Exception(f"The value: {elem}: in '{key}' position is not a valid date")
                # </per>

            # <se2> altrimenti non è una lista, ma è un dato valido
            elif isinstance(dates, Date):

                # .append per inizializzare una lista vuota / .extend richiede una lista non vuota / evita errore
                self.personal_db.append(dates)

            # </se2> non è una lista ma non è neanche un dato valido
            else:

                print("Insert a valid date")

        # </se1> non inserisce nulla
        else:

            print("Nothing inserted")

    def __str__(self):

        # lista per vedere le date inserite
        listone = []

        # per ogni data nella lista
        for date in self.personal_db:

            # aggiungi le date presenti
            listone.append(str(date))

        # ritorno la "lista di visualizzazione delle date"
        return f" List of dates: {str(listone)}"
        # return f"List of dates: {[str(date) for date in self.personal_db]}"

#_______________________________________________________________^^CORRETTO.


    def newdate(self, new: Date) -> str:

        # se inserita data
        if new:

            # aggiunge data
            #print(self.personal_db)
            return self.personal_db.append(new)

        else:

            # altrimenti messaggio di errore
            print("Cannot be empty")

    def deldate(self, delete: Date) -> None:

        if delete:

            # var boolena per avvisarmi se è stato trovata una data esistente
            found: bool = False

            # per ogni data da cancellare nella lista personal_db
            for date_to_del in self.personal_db:

                # se la data è uguala alla data da cancellare
                if date_to_del == delete:

                    # attivo la var bool per avvisare che è stata trovata la data da cancellare
                    # elimino la data da eliminare
                    # interrompo il ciclo una volta trovato, non ce bisono di proseguire, se trovato
                    found = True
                    self.personal_db.remove(delete)
                    print(f"Removed: --")
                    #print(f"{self.personal_db}")
                    break

            # se non è stata trovata la data, messaggio di avviso
            if not found:

                print("Not found")

        # se lasciato vuoto
        else:

            print("Cannot be empty")

if __name__ == "__main__":

    # prova: Database = Database("312.22.11")
    # prova1: Database = Database("01.01.2004")
    # prova.newdate("12.03.1997")
    # prova1.newdate("12.03.1998")
    # print(prova)
    data1: Date = Date("31.10.1984")
    data2: Date = Date("30.10.1984")
    data3: Date = Date("29.10.1984")
    prova: Database = Database(data1)
    prova.newdate(data2)
    prova.newdate(data3)
    #prova.newdate(data1)
    #prova.deldate(data2)
    #prova.newdate(data1)

    print(prova)