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

# 1.
class Database:

    # prende una lista di stringhe
    def __init__(self, dates: list[str]):

        # inizializzo una lista vuota
        # successivamente "estendo" la lista, .append avrebbe creato liste annidate
        self.personal_db: list[str] = []
        self.personal_db.extend(dates)

    def newdate(self, new: str) -> str:

        # se inserita data
        if new:

            # aggiunge data
            self.personal_db.append(new)

        else:

            # altrimenti messaggio di errore
            print("Cannot be empty")

    def deldate(self, delete: str) -> None:

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
                    break

            # se non è stata trovata la data, messaggio di avviso
            if not found:

                print("Not found")

        # se lasciato vuoto
        else:

            print("Cannot be empty")