'''
Progettare un sistema di videonoleggio con i seguenti requisiti:

1. Classe Movie:

    Attributi:

        movie_id: str - Identificatore di un film.
        title: str - Titolo del film.
        director: str - Regista del film.
        is_rented: boolean - Booleano che indica se il film è noleggiato o meno.

    Metodi:

        rent():
        Contrassegna il film come noleggiato se non è già noleggiato.
        Se il film non è già noleggiato imposta is_rented a True,
        altrimenti stampa il messaggio "Il film '{self.title}' è già noleggiato."

        return_movie():
        Contrassegna il film come restituito.
        Se il film è già noleggiato imposta is_rented a False,
        altrimenti stampa il messaggio "Il film '{self.title}' non è stato noleggiato da questo cliente."

2. Classe Customer:

    Attributi:

        customer_id: str - Identificativo del cliente.
        name: str - Nome del cliente.
        rented_movies: list[Movie] - Lista dei film noleggiati.

    Metodi:

        rent_movie(movie: Movie):
        Aggiunge il film nella lista rented_movies se non è già stato noleggiato,
        altrimenti stampa il messaggio "Il film '{movie.title}' è già noleggiato."

        return_movie(movie: Movie):
        Rimuove il film dalla lista rented_movies se già presente,
        altrimenti stampa il messaggio "Il film '{movie.title}' non è stato noleggiato da questo cliente."

3. Classe VideoRentalStore:

    Attributi:

        movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
        customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.

    Metodi:

        add_movie(movie_id:str, title: str, director: str):
        Aggiunge un nuovo film nel videonoleggio se non è già presente,
        altrimenti stampa il messaggio "Il film con ID '{movie_id}' esiste già."

        register_customer(customer_id: str, name: str):
        Iscrive un nuovo cliente nel videonoleggio se non è già presente,
        altrimenti stampa il messaggio "Il cliente con ID '{customer_id}' è già registrato."

        rent_movie(customer_id: str, movie_id: str):
        Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio,
        altrimenti stampa il messaggio "Cliente o film non trovato."

        return_movie(customer_id: str, movie_id: str):
        Permette al cliente di restituire un film se entrambi esistono nel videonoleggio,
        altrimenti stampa il messaggio "Cliente o film non trovato."

        get_rented_movies(customer_id: str):
        list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies)
        se il cliente esiste nel videonoleggio,
        altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.
'''

class Movie:
    '''
    Attributi:

        movie_id: str - Identificatore di un film.
        title: str - Titolo del film.
        director: str - Regista del film.
        is_rented: boolean - Booleano che indica se il film è noleggiato o meno.

    Metodi:

        rent():
        Contrassegna il film come noleggiato se non è già noleggiato.
        Se il film non è già noleggiato imposta is_rented a True,
        altrimenti stampa il messaggio "Il film '{self.title}' è già noleggiato."

        return_movie():
        Contrassegna il film come restituito.
        Se il film è già noleggiato imposta is_rented a False,
        altrimenti stampa il messaggio "Il film '{self.title}' non è stato noleggiato da questo cliente."
    '''
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self) -> None|str:
        if not self.is_rented:
            self.is_rented = True

        else:
            print(f"Il film '{self.title}' è già noleggiato.")

    def return_movie(self) -> None|str:
        if self.is_rented:
            self.is_rented = False

        else:
            print(f"Il film '{self.title}' nont è stato noleggiato da questo cliente.")

class Customer:
    '''
    Attributi:

        customer_id: str - Identificativo del cliente.
        name: str - Nome del cliente.
        rented_movies: list[Movie] - Lista dei film noleggiati.

    Metodi:

        rent_movie(movie: Movie):
        Aggiunge il film nella lista rented_movies se non è già stato noleggiato,
        altrimenti stampa il messaggio "Il film '{movie.title}' è già noleggiato."

        return_movie(movie: Movie):
        Rimuove il film dalla lista rented_movies se già presente,
        altrimenti stampa il messaggio "Il film '{movie.title}' non è stato noleggiato da questo cliente."
    '''
    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = None) -> None:
        self.customer_id: str = customer_id
        self.name: str = name
        self.rented_movies: list[Movie] = rented_movies if rented_movies else []

    def rent_movie(self, movie: Movie) -> None:
        lista_id_noleggiati: list[str] = [film_id.movie_id for film_id in self.rented_movies]
        if movie.movie_id not in lista_id_noleggiati:

            self.rented_movies.append(movie)

        else:
            print(f"Il film '{movie.title}' è già noleggiato.")

    def return_movie(self, movie: Movie) -> None:
        lista_id_noleggiati: list[str] = [film_id.movie_id for film_id in self.rented_movies]
        if movie.movie_id in lista_id_noleggiati:

            for film in self.rented_movies:

                if film.movie_id == movie.movie_id:
                    self.rented_movies.remove(film)
                    break

        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")

class VideoRentalStore:
    '''
    Attributi:

        movies: dict[str, Movie] - Dizionario che ha per chiave l'id del film e per valore l'oggetto Movie.
        customers: dict[str, Customer] - Dizionario che ha per chiave l'id del cliente e per valore l'oggetto Customer.

    Metodi:

        add_movie(movie_id:str, title: str, director: str):
        Aggiunge un nuovo film nel videonoleggio se non è già presente,
        altrimenti stampa il messaggio "Il film con ID '{movie_id}' esiste già."

        register_customer(customer_id: str, name: str):
        Iscrive un nuovo cliente nel videonoleggio se non è già presente,
        altrimenti stampa il messaggio "Il cliente con ID '{customer_id}' è già registrato."

        rent_movie(customer_id: str, movie_id: str):
        Permette al cliente di noleggiare un film se entrambi esistono nel videonoleggio,
        altrimenti stampa il messaggio "Cliente o film non trovato."

        return_movie(customer_id: str, movie_id: str):
        Permette al cliente di restituire un film se entrambi esistono nel videonoleggio,
        altrimenti stampa il messaggio "Cliente o film non trovato."

        get_rented_movies(customer_id: str):
        list[Movie] - Restituisce la lista dei film noleggiati dal client (customer.rented_movies)
        se il cliente esiste nel videonoleggio,
        altrimenti stampa il messaggio "Cliente non trovato." e ritorna una lista vuota.
    '''
    def __init__(self, movies: dict[str, Movie], customers: dict[str, Customer]) -> None:
        self.movies = movies
        self.customers = customers
    
    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        '''
        add_movie(movie_id:str, title: str, director: str):
        Aggiunge un nuovo film nel videonoleggio se non è già presente,
        altrimenti stampa il messaggio "Il film con ID '{movie_id}' esiste già."
        '''
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id, title, director)
        
        else:
            print(f"Il film con ID '{movie_id}' esiste già.")