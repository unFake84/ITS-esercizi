class Movie:
    def __init__(self, movie_id: str, title: str, director: str) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False

    def rent(self) -> None:
        if not self.is_rented:
            self.is_rented = True

        else:
            print(f"Il film '{self.title}' è già noleggiato.")

    def return_movie(self) -> None:
        if self.is_rented:
            self.is_rented = False

        else:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")

class Customer:

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

    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}) -> None:
        self.movies = movies
        self.customers = customers
    
    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        if movie_id not in self.movies:
            self.movies[movie_id] = Movie(movie_id, title, director)
        
#        else:
#            print(f"Il film con ID '{movie_id}' esiste già.")
    
    def register_customer(self, customer_id: str, name: str) -> None:
        if customer_id not in self.customers:
            self.customers[customer_id] = Customer(customer_id, name)
        
#        else:
#            print(f"Il cliente con ID '{customer_id} è già registrato'.")

    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        
        else:
            print("Cliente o film non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str) -> None:
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])

        else:
            print("Cliente o film non trovato.")

    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        
        else:
            print("Cliente non trovato")
            return []