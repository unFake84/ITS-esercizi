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
        return self.date == other.date
    
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

    # puo prendere: una data, una lista di date oppure nessuna data 
    def __init__(self, dates = None):  # -> None: permette anche di non ricevere 'date'

        # inizializzo una lista vuota
        self.personal_db: list[Date] = []

        # <se1> l'input avviene
        if dates is not None:

            # <se2> l' input è una lista
            if isinstance(dates, list):

                # <per> ogni chiave+elemento nella lista
                for key, elem in enumerate(dates):

                    # <se3> il valore rispetta il tipo
                    if isinstance(elem, Date):

                        # aggiungo con .append l' elemento(la data) nella lista
                        self.personal_db.append(elem)
                        print(f"Added:\t\t\t-{elem}-")

                    # </se3> allora lancio un errore dicendo in quale chiave il valore non è corretto
                    else:

                        raise Exception(
                            f"The value: [ '{elem}' ] in '{key}' position is not a valid date.\n"
                            f"Expected: \"dd.mm.aaaa\"\n"
                            f"Your try: \"{elem}\"\n"
                            f"If the date is similiar to: dd.mm.aaaa,\n"
                            f"have you tried to object them? es. -> variablename: Date = Date(\"{datetime.now().strftime('%d/%m/%Y')}\")"
                            )
                # </per>

            # <se2> altrimenti l'input non è una lista, ma è cmq un dato valido(Date)
            elif isinstance(dates, Date):

                # .append per inizializzare anche una lista vuota / .extend richiede una lista non vuota <- evita errore
                # se lista esiste -> aggiunge alla lista
                self.personal_db.append(dates)

# -----> serie di controlli superflui dato che la classe Date gestisce anticipatamente questi tipi di errori.

            # </se2> non è una lista e neanche un dato valido
            else:

                # # inserire un raise per gestire l'errore
                print("Insert a valid date")

        # </se1> non inserisce nulla
        else:

            # # inserire un raise per gestire l'errore
            print("No entry")

    # metodo str per 'permettere di mostrare' i dati inseriti nella ->
    def __str__(self) -> str:

        # -> lista(listone) le date inserite
        listone: list[str] = []

        # per ogni data nella lista, ->
        for date in self.personal_db:

            # -> aggiungi le date presenti
            listone.append(str(date)) # <- casting di 'date' e <appende> la data nella "lista display" {listone}

        # ritorno la "lista di visualizzazione delle date"     -provv-
        return f"{('*************************************'*3)}\n"\
                f"List of final dates: {listone}\n"\
                    f"{('*************************************'*3)}" # <- umb is back!
        # return f"List of dates: {[str(date) for date in self.personal_db]}" <- da tenere per ordinare in futuro


#_______________________________________________________________^^ CORRETTO. (spero!)
# Potrei rendere newdate, deldate etc piu flessibile sul input (simile all' init->None->List etc),
# Ma per ora mi aspetto che una volta inserita una base di partenza, l'utente possa gestire
# una data alla volta, è deve essere di tipo Date
#_______________________________________________________________vv Gestione singola + soloNone vv


    def newdate(self, new = None) -> None:

        # se inserita data di tipo Date
        if new and isinstance(new, Date):

            # e se non è già presente nella lista
            if new not in self.personal_db:

                # aggiunge data
                self.personal_db.append(new)
                print(f"Added:\t\t\t-{new}-")

            # per ora stampo che è impossibile aggiungere visto che già esiste tale data
            else:

                print(f"Impossible to insert '{new}', allready exists")

        # altrimenti:
        # se non inserito.. <- la classe Date dovrebbe già effettuare questo controllo,
        # se utente non inserisce tipo Date, questo controllo è essenziale per evitare
        # di inserire dati errati
        else:

            # non si possono inserire date vuote
            if new is None:

                # messaggio di errore da far diventare un raise
                print("Cannot be empty:\t-not added-")

            # il tipo di dato inserito non è Date
            else:

                print(f"Failed:\t\t\t-{new}-\tdate not valid")

    def deldate(self, delete = None) -> None:

        # <se1> inserita una data da cancellare valida(Date)
        if delete and isinstance(delete, Date):

            # <var> boolena per avvisarmi se è stato trovata una data esistente
            found: bool = False

            # <per> ogni data da cancellare nella lista personal_db
            for date_to_del in self.personal_db:

                # <se2> la data è uguala alla data da cancellare
                if date_to_del == delete:

                    # attivo la </var> bool per avvisare che è stata trovata la data da cancellare
                    # elimino la data da eliminare
                    # interrompo il ciclo una volta trovato, non ce bisono di proseguire, se trovato
                    found = True
                    self.personal_db.remove(delete)
                    print(f"Removed:\t\t-{delete}-")
                    break # <- per ora; appena trova, interrompe il ciclo ( != quando potrà cancellare + di una data)
                # </se2> 
            # </per>

            # <se!> non è stata trovata la data, messaggio di avviso
            if not found:

                print(f"Not found:\t\t-{delete}-\tcan not delete")

        # </se1> se non è stata inserita nessuna data da cancellare
        # oppure se il tipo di date non è Date(essenziale)
        else:

            # se lasciato vuoto
            if delete is None:

                print("Cannot be empty:\t-not deleted-")

            # altrimenti mostro cosa è andato storto
            else:

                vuota: str = ""

                if delete == vuota :

                    print(f"Failed:\t\t\t-empty-\t\tdate not valid")

                else:

                    print(f"Failed:\t\t\t-{delete}-\tdate not valid")

    def modifydate(self, old = None, new = None) -> None:

        # <se1> la vecchia data e la nuova data da inserire sono di tipo Date,
        if isinstance(old, Date) and isinstance(new, Date):
        
            # <se2> la data da modificare è presente nel database(personal_db)
            if old in self.personal_db:

                # utilizziamo un ciclo per trovare l'indice da poter poi usare,
                # <per> ogni chiave e valore presente nel database(personal_db)
                for key, value in enumerate(self.personal_db):

                    # se la data(valore) nella lista è uguale alla data da modificare
                    if value == old:

                        # controlla che la nuova data non sia già presente nel database (così si evitano duplicati)
                        if new not in self.personal_db:

                            self.personal_db[key] = new
                            print(f"Modified:\t\t-{old}-\tto\t\t\t-{new}-")
                            break

                        # altrimenti se la data già esiste
                        else:

                            print(f"Can not modified:\t-{new}-\texisting date\t\t-{value}-")
                            break

            # </se2> se la data da modificare non è presente nel database
            else:

                print(f"Not found:\t\t-{old}-\tcan not insert:\t\t-{new}-")
        
        # </se1:> non sono di tipo Date:
        else:

            # </se1a> è solo la data nuova ad essere tipo Date
            if isinstance(new, Date):

                print("Invalid date:\t\t-can not find-\tinvalid date type\t-not modified-")

            # </se1b> invece è la data vecchia ad essere tipo Date
            elif isinstance(old, Date):

                print(f"Invalid date:\t\t-{old}-\tinvalid date type\t-not modified-")

            # </se1c> entrambi non sono di tipo Date 
            else:

                print("Invalid date:\t\t-not modified-\tinvalid's date type\t-not modified-")

    def query(self, show = None) -> None:

        # <se1> la data da controllare è una data di tipo Date,
        if show and isinstance(show, Date):

            # <se2> la data è all'interno del database
            if show in self.personal_db:

                # <per> ogni chiave e valore nel database
                for key, value in enumerate(self.personal_db):

                    # <se3> troviamo il valore,
                    if value == show:

                        print(f"Query:\t\t\t-{value}-\tindex found:\t\t-{key}-")
                    # </se3>
                # </per>

            # </se2> precedentemente la data non è stata trovata nel database
            else:

                print(f"Query:\t\t\t-{show}-\tdata not found:\t\t-Na-")

        # </se1> la data non è un tipo Date
        else:

            print(f"Query:\t\t\t-invalid type-\tno index:\t\t-Na-")

#----------------- in futuro modificare per mostrare l'ora di inserimento -----------------
        #     self.show = datetime.now()

        # print(self.show.strftime("%H:%M:%Y"))

if __name__ == "__main__":

    #-------------------------------------------------
    # prova: Database = Database("312.22.11") <- errato, si passa una stringa
    # prova1: Database = Database("01.01.2004") <- uguale
    # prova.newdate("12.03.1997") <- non è 'ancora' un tipo Date|
    # prova1.newdate("12.03.1998") <- - - - - - - - - - - - - - |
    #-------------------------------------------------

    data1: Date = Date("31.10.1984")
    data2: Date = Date("30.10.1984")
    data3: Date = Date("29.10.1984")
    data4: Date = Date("01.10.1980")
    data5: Date = Date("09.03.1987")
    data6: Date = Date("10.06.2020")
    data7: Date = Date("11.06.2020")
    data8: Date = Date("20.01.2008")
    data9: Date = Date("17.01.2008")
    data10 = ("24.56.2032")




    prova: Database = Database([data1, data2, data3])
    print(prova)
    prova.newdate(" ciao ")
    prova.newdate(data4)
    prova.newdate(data10)
    prova.deldate(data2)
    prova.deldate(data2)
    prova.deldate("")
    prova.deldate(data10)
    prova.newdate(data2)

    print(prova)
    prova.modifydate(data1, "ciao")
    prova.modifydate(data3, data2)
    prova.modifydate("01.11.1984", data3)
    prova.modifydate("banana", "fragola")
    prova.modifydate(data3, data5)
    prova.modifydate(data2, data6)
    prova.modifydate(data2, data7)
    prova.modifydate(data4, data9)
    prova.modifydate(data6, data8)

    print(prova)
    prova.query(data9)
    prova.query(12)
    prova.query(data4)
    print(prova)