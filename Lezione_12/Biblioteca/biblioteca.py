'''
Sistema di Gestione Biblioteca

Si desidera sviluppare un sistema per la gestione di una biblioteca in Python.
Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e
restituzione degli stessi.
Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e
visualizzare quali libri sono disponibili in un dato momento.

Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito.
         Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi della classe:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca.
      Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato,
      lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile.
      Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili.
      Se non ci sono libri disponibili, restituisce un messaggio di errore.

Codice Driver

    Aggiungi libri alla biblioteca.
    Presta e restituisci libri, gestendo anche casi limite (già prestato, doppia restituzione, libro inesistente).
    Mostra i libri disponibili in ogni fase.
    Visualizza lo stato finale di ogni libro.

'''

class Libro:
    '''- Rappresenta un libro con titolo, autore, stato del prestito.'''

    _titolo: str
    _autore: str
    _prestato: bool

    def __init__(self, t: str, a: str, s: bool = False) -> None:
        self._titolo = t
        self._autore = a
        self._prestato = s

    @property
    def titolo(self) -> str:
        return self._titolo

    @titolo.setter
    def titolo(self, t: str) -> None:
        self._titolo = t

    @property
    def autore(self) -> str:
        return self._autore

    @autore.setter
    def autore(self, a: str) -> None:
        self._autore = a

    @property
    def stato(self) -> bool:
        return self._prestato

    @stato.setter
    def stato(self, p: bool) -> None:
        self._prestato = p

    def __str__(self) -> str:
        libro_str: str = f"{'Titolo:':<10}{self.titolo}\n"\
                         f"{'Autore:':<10}{self.autore}\n"\
                         f"{'Stato:':<10}{'Disponibile' if not self.stato else 'Prestato'}"

        return libro_str

class Biblioteca:
    '''
    - Gestice tutte le operazioni legate alla gestione di una biblioteca.

        Metodi della classe:

        - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca.
          Restituisce un messaggio di conferma.

        - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato,
          lo segna come disponibile. Restituisce un messaggio di stato.

        - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile.
          Restituisce un messaggio di stato.

        - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili.
          Se non ci sono libri disponibili, restituisce un messaggio di errore.
    '''

    _nome: str
    _catalogo: dict[bool, dict[str, Libro]]

    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._catalogo = {
            False: {},
            True: {}
        }

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, n: str) -> None:
        self._nome = n

    def aggiungi_libro(self, libro: Libro) -> str:
        '''
        - Aggiunge un nuovo libro al catalogo della biblioteca.
          Restituisce un messaggio di conferma.
        '''
        if libro.titolo not in self._catalogo[False] and libro.titolo not in self._catalogo[True]:
            self._catalogo[False][libro.titolo] = libro

            return f"Il libro '{libro.titolo}' è stato aggiunto al catalogo."

        else:
            raise ValueError("Libro già presente nel catalogo.")

    def presta_libro(self, titolo: str) -> str:
        '''
        - Cerca un libro per titolo e, se disponibile e non già prestato,
          lo segna come (in)disponibile. Restituisce un messaggio di stato.
        '''

        nome_libro: str = None
        stato_libro: bool = None

        for stato, libri in self._catalogo.items():

            for libro in libri.values():

                if libro.titolo == titolo:
                    nome_libro = libro.titolo
                    stato_libro = stato
                    oggetto: Libro = libro
                    break

            if stato_libro is not None:
                break

        if stato_libro is not None:
            if stato_libro == False:
                self._catalogo[False].pop(nome_libro)
                self._catalogo[True][nome_libro] = oggetto
                oggetto.stato = True

                return f"Il libro {titolo} è stato prestato con successo."

            else:
                return f"Non è stato possibile, {titolo} non disponibile."

        else:
            return f"{titolo} non è ancora presente nel catalogo."

    def restituisci_libro(self, titolo: str) -> str:
        '''
        - Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile.
          Restituisce un messaggio di stato.
        '''

        nome_libro: bool = None
        stato_libro: bool = None

        for stato, libri in self._catalogo.items():

            for libro in libri.values():

                if libro.titolo == titolo:
                    nome_libro = libro.titolo
                    stato_libro = libro.stato
                    oggetto: Libro = libro
                    break

            if stato_libro is not None:
                break

        if stato_libro is not None:
            if stato_libro:
                self._catalogo[True].pop(nome_libro)
                self._catalogo[False][nome_libro] = oggetto
                oggetto.stato = False

                return f"Il libro {titolo} è stato restituito con successo."

            else:
                return f"Il libro {titolo} risulta già in giacenza, impossibile consegnare."

        else:
            return f"Il libro {titolo} non è della libreria {self.nome}."

    def mostra_libri_disponibili(self) -> str:
        '''
        - Restituisce una lista dei titoli dei libri attualmente disponibili.
          Se non ci sono libri disponibili, restituisce un messaggio di errore.
        '''

        if not self._catalogo[False]:
            return f"Non ci sono libri disponibili al momento."
        
        stringa_finale: str = f"\nDISPONIBILI AL MOMENTO\n{'-' * 50}\n"

        for libro in self._catalogo[False].values():

            stringa_finale += str(libro) + f"\n" + '-' * 50 + '\n'

        return stringa_finale

    def __str__(self) -> str:
        disponibili_str: str = f"DISPONIBILI:\n{'-' * 50}\n" if self._catalogo[False] else "NESSUN LIBRO DISPONIBILE\n"
        prestati_str: str = f"PRESTATI:\n{'-' * 50}\n" if self._catalogo[True] else "NESSUN LIBRO PRESTATO\n"

        for stato, libri in self._catalogo.items():

            if stato == False:
                for l in libri.values():

                    disponibili_str += str(l) + f"\n" + '-' * 50 + "\n"

            if stato == True:
                for l in libri.values():

                    prestati_str += str(l) + f"\n" + '-' * 50 + "\n"

        return f"\nBiblioteca: {self.nome}\n\n{disponibili_str}\n{prestati_str}"

if __name__ == "__main__":

    try:
        # TEST LIBRO
        libro1: Libro = Libro("Harry Potter e la pietra filosofale", "J. K. Rowling")

        # libro1.stato = True                                       OK
        # libro1.titolo = "Harry Potter e il calice di fuoco"       OK

        print("Libro creato:")
        print(libro1)

        # TEST BIBLIOTECA
        libro2: Libro = Libro("Notte sull'acqua", "Ken Follet")

        biblio1: Biblioteca = Biblioteca("Biblio")

        print(biblio1.aggiungi_libro(libro1))
        print(biblio1.aggiungi_libro(libro2))

        print(biblio1.aggiungi_libro(libro2))


    except ValueError as err:
        print(f"\nEXCEPTION\nImpossibile aggiungere '{libro2.titolo}'.")
        print(err, "\n")

    print("="*120)
    print(biblio1)
    print("="*120)

    print(biblio1.presta_libro("Notte sull'acqua"))
    print(biblio1.presta_libro("Notte sull'acqua"))
    print(biblio1.presta_libro("Il ritratto di Dorian Gray"))

    print("="*120)
    print(biblio1)
    print("="*120)

    print(biblio1.restituisci_libro("Notte sull'acqua"))
    print(biblio1.restituisci_libro("Notte sull'acqua"))
    print(biblio1.restituisci_libro("Il ritratto di Dorian Gray"))

    print("="*120)
    print(biblio1)
    print("="*120)

    print(biblio1.presta_libro("Harry Potter e la pietra filosofale"))

    print(biblio1.presta_libro("Notte sull'acqua"))
    print("="*120)
    print(biblio1.mostra_libri_disponibili())
    print("="*120)

    print(biblio1.presta_libro("Notte sull'acqua"))

    print("="*120)
    print(biblio1)
    print("="*120)