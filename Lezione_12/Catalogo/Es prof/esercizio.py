class MovieCatalog:

    '''
    Attributi della classe Movie Catalog:
    self.catalog: dict[str, list[str]]
    '''

    # inizializzare un oggetto della classe MovieCatalog
    def __init__(self) -> None:
        
        self.setCatalog()

    # metodi setter:

    # metodo che imposta il valore dell'attributo self.catalog
    def setCatalog(self) -> None:

        self.catalog: dict[str, list[str]] = {}

    # metodo getter

    # metodo che ritorna un valore dell'attributo self.catalog
    def getCatalog(self) -> dict[str, list[str]]:

        return self.catalog

    # metodo str

    def __str__(self) -> str: # DA SISTEMARE

        string: str = ""
        
        for key, value in self.catalog.items():

            string = "\n" + key + ": " + str(value) + "\n"

        return string

    # metodi della classe MovieCatalog:

    # metodo che aggiunge una lista di film al catalogo
    def add_movie(self, director_name: str, movies: list[str]) -> None:

        if not director_name:

            print("Fornire un nome valido per il regista")

        # check valore valido di movies
        elif not movies:

            print("Fornire una lista di film che non sia vuota")

        # se i dati inseriti sono validi
        else:

            # se il regista è presente nel catalogo
            if director_name in self.catalog:

                # aggiungere film al catalogo
                for movie in movies:

                    # controlliamo se i film della lista movies siano già stati inseriti dentro il catalogo
                    # dizionario[key] -> ritorna il valore corrispondente alla chiave key
                    # self.catalog[director_name] è la lista dei film prodotti dal regista director_name
                    # dove self.catalog è un dizionario
                    # director_name è la chiave
                    # self.catalog[director_name] è il valore corrispondente alla chiave directory_name
                    if movie in self.catalog[director_name]:

                        print(f"Il film {movie} è gia presente nel catalogo")

                    # un film della lista movies non è già presente nel catalogo
                    else:

                        # aggiungere il film al catalogo
                        self.catalog[director_name].append(movie)

            # se il regista non è presente nel catalogo, creare un nuovo record che ha come chiave il nome del regista
            # e come valore la lista di film movies
            else:

                self.catalog[director_name] = movies

    # metodo che rimuove un film dal catalogo
    def remove_movie(self, director_name: str, movie: str) -> None:

        if not director_name:

            print("Fornire un nome valido per il regista")

        # check valore valido di movies
        elif not movie:

            print("Fornire una lista di film che non sia vuota")

        # se i dati inseriti sono validi
        else:

            # se il regista è presente nel catalogo e check se il film da rimuovere è presente nella lista dei film prodotti dal regista director_name
            if director_name in self.catalog and movie in self.catalog[director_name]:

                #rimuovere il film dalla lista
                self.catalog[director_name].remove(movie)

            # se la lista dei film è vuota, rimuovi il regista dal catalogo
            if not self.catalog[director_name]:

                # rimuovere il regista dal catalogo
                del self.catalog[director_name]

    def list_directors(self) -> list[str]:

        return list(self.catalog.keys())