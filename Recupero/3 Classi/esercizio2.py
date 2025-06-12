class Movie:
    '''
    Classe Movie:
        Attributi:
    ● movie_id: str - Identificatore di un film.
    ● title: str - Titolo del film.
    ● director: str - Regista del film.
    ● is_rented: boolean - Booleano che indica se il film è noleggiato o meno.
    Metodi:
    '''

    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented

    def __str__(self) -> str:
        return (
            f"ID: {self.movie_id}\n"
            f"Titolo: {self.title}\n"
            f"Regista: {self.director}\n"
            f"Affittato: {'Si' if self.is_rented else 'No'}"
            )

    def __repr__(self):
        return f"||FilmID = {self.movie_id} |Titolo = {self.title} |Direttore = {self.director} |Affittato: '{'Si' if self.is_rented else 'No'}'||\n"

    def rent(self) -> None:
        '''
        ● rent(): Contrassegna il film come noleggiato se non è già noleggiato. Se il film
        non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
        film '{self.title}' è già noleggiato."
        '''

        if self.is_rented:
            print(f"Il film '{self.title}' è già noleggiato.")

        else:
            self.is_rented = True

    def return_movie(self) -> None:
        '''
        ● return_movie(): Contrassegna il film come restituito. Se il film è già noleggiato
        imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
        stato noleggiato da questo cliente."
        '''

        if not self.is_rented:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")

        else:
            self.is_rented = False

class Customer:
    '''
    2. Classe Customer:
    Attributi:
    ● customer_id: str - Identificativo del cliente.
    ● name: str - Nome del cliente.
    ● rented_movies: list[Movie] - Lista dei film noleggiati.
    '''

    def __init__(self, customer_id: str, name: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []

    def __str__(self) -> str:
        lista_di_film: list[str] = []
        contatore_films: int = 0

        for i, film in enumerate(self.rented_movies, 1):
            lista_di_film.append(f"\nFilm n° {i}:\n{str(film)}")
            contatore_films += 1

        if lista_di_film:
            lista_di_film.append("-"*30)

        mostra_film: str = '\n'.join(lista_di_film) if lista_di_film else 'Nessun film attualmente in affitto'

        return (
            f"ID: {self.customer_id}\n"
            f"Nome: {self.name}\n"
            f"Film attualmente in affitto: {contatore_films}\n"
            f"{mostra_film}"
        )

    def __repr__(self):
        return f"ClienteID = {self.customer_id} Nome = {self.name}\n"

    def rent_movie(self, movie: Movie) -> None:

        '''
        ● rent_movie(movie: Movie): Aggiunge il film nella lista rented_movies se non è già
        stato noleggiato, altrimenti stampa il messaggio "Il film '{movie.title}' è già
        noleggiato."
        '''

        if movie.is_rented:
            print(f"Il film '{movie.title}' è già noleggiato.")

        else:
            movie.rent()
            self.rented_movies.append(movie)

    def return_movie(self, movie: Movie) -> None:
        '''
        ● return_movie(movie: Movie): Rimuove il film dalla lista rented_movies se già
        presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
        noleggiato da questo cliente."
        '''

        if movie in self.rented_movies:
            movie.return_movie()
            self.rented_movies.remove(movie)

        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    '''
    3. Classe VideoRentalStore:
    Attributi:
    ● movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore
    l'oggetto Movie.
    ● customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per
    valore l'oggetto Customer.
    '''

    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}) -> None:
        self.movies = movies
        self.customers = customers

    def __str__(self) -> str:
        movies: list[str] = []
        customer: list[str] = []
        contatore_film: int = 0
        contatore_clienti: int = 0

        if self.movies:
            for value in self.movies.values():
                stringa_movies: str = f"\n{str(value)}\n"
                movies.append(stringa_movies)
                contatore_film += 1

        else:
            movies.append("Nessun film attualmente in affitto")

        if self.customers:
            for value in self.customers.values():
                string_customers: str = f"\n{str(value)}\n"
                customer.append(string_customers)
                contatore_clienti += 1
        
        else:
            customer.append("Nessun cliente registrato ancora")

        mostra_movies: str = '\n'.join(movies)
        mostra_clienti: str = '\n'.join(customer) if customer else 'Nessun film attualmente in affitto'

        return (
            f"\nFilm:\n"
            f"\nFilm totali: {contatore_film}\n"
            f"\n{mostra_movies}\n{'-'*30}\n"
            f"\nCliente:\n"
            f"\nClienti totali: {contatore_clienti}\n"
            f"{mostra_clienti}"
            )

    def __repr__(self):
        return f"Customers: {self.customers} Movies: {self.movies}\n"

    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        '''
        ● add_movie(movie_id: str, title: str, director: str): Aggiunge un nuovo film nel
        videonoleggio se non è già presente, altrimenti stampa il messaggio "Il film con
        ID '{movie_id}' esiste già."
        '''

        if movie_id not in self.movies:
            movie: Movie = Movie(movie_id, title, director)
            #self.movies[movie_id] = movie
            tupla: tuple = (movie_id, movie)
            self.movies.update(tupla)

        else:
            print(f"Il film con ID '{movie_id}' esiste già.")

    def register_customer(self, customer_id: str, name: str) -> None:
        '''
        ● register_customer(customer_id: str, name: str): Iscrive un nuovo cliente nel
        videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
        con ID '{customer_id}' è già registrato."
        '''

        if customer_id in self.customers:
            print(f"Il cliente con ID '{customer_id}' è già registrato.")

        else:
            costumer: Customer = Customer(customer_id, name)
            self.customers[customer_id] = costumer

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        '''
        ● rent_movie(customer_id: str, movie_id: str): Permette al cliente di noleggiare un
        film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
        "Cliente o film non trovato."
        '''

        if movie_id not in self.movies or customer_id not in self.customers:
            print("Cliente o film non trovato.")

        else:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].rent_movie(movie)


    def return_movie(self, customer_id: str, movie_id: str) -> None:
        '''
        ● return_movie(customer_id: str, movie_id: str): Permette al cliente di restituire un
        film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
        "Cliente o film non trovato."
        '''

        if movie_id in self.movies and customer_id in self.customers:
            movie: Movie = self.movies[movie_id]
            self.customers[customer_id].return_movie(movie)

        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        '''
        ● get_rented_movies(customer_id: str): list[Movie] - Restituisce la lista dei film
        noleggiati dal client (customer.rented_movies) se il cliente esiste nel
        videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
        lista vuota.
        '''

        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies

        else:
            print("Il cliente non esiste")

    def get_all_movies(self) -> list[Movie]:
        '''
        Una lista di oggetti movie
        Intera lista di film noleggiati
        Ritorna la lista di film che sono stati dati dal videonoleggio a tutti i clienti
        '''
        lista_generale: list[Movie] = []

        for cliente in self.customers.values():
            lista_generale.extend(cliente.rented_movies)

        return lista_generale
        # #--------------------------------------------------------------------------
        # for utente in self.customers.values():
        #     lista_personale: list[str] = []
        #     lista_personale.append(str(utente.customer_id))
        #     lista_personale.append(str(utente.name))
        #     lista_personale.append([str(movie)for movie in utente.rented_movies])
        #     lista_generale.append(lista_personale)
        # return lista_generale
        # #--------------------------------------------------------------------------


        #print(f"{self.movies} # {self.customers}")
        #provafor = [indice for indice in mat1]