'''
Sistema di Gestione Catalogo Film 
Sviluppa un sistema in Python per la gestione di un catalogo film che permetta di aggiungere,
rimuovere e cercare film di un particolare regista.
Il sistema dovrebbe consentire anche di visualizzare tutti i registi e i loro film.

Classe:
- MovieCatalog: Gestisce tutte le operazioni legate al catalogo dei film.

    Metodi della classe:
    - add_movie(director_name, movies): Aggiunge uno o più film a un regista specifico nel catalogo.
        Se il regista non esiste, viene creato un nuovo record.
        Se il regista esiste, la sua lista di film viene aggiornata.

    - remove_movie(director_name, movie_name): Rimuove un film specifico dall'elenco dei film di un regista.
        Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.

    - list_directors(): Elenca tutti i registi presenti nel catalogo.

    - get_movies_by_director(director_name): Restituisce tutti i film di un regista specifico.

    - search_movies_by_title(title): Trova tutti i film che contengono una certa parola nel titolo.
        Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o
        un messaggio di errore se nessun film contiene la parola cercata nel titolo.

Codice driver

    Crea un’istanza della classe MovieCatalog.
    Aggiungi nuovi film e registi.
    Aggiungi film a registi già presenti nel catalogo.
    Rimuovi film dal catalogo.
    Elenca i registi presenti nel catalogo.
    Visualizza film di uno specifico regista.
    Cerca film per parola chiave nel titolo, gestendo il caso con risultati che senza.

'''

class MovieCatalog:
    '''Gestisce tutte le operazioni legate al catalogo dei film.'''

    _catalog: dict[str, list[str]]

    def __init__(self, catalog: dict[str, list[str]]|None = None) -> None:
        self._catalog = {} if catalog is None else catalog

    def add_movie(self, director_name, movies: str|list[str]) -> None:
        '''
        - Aggiunge uno o più film a un regista specifico nel catalogo.
            Se il regista non esiste, viene creato un nuovo record.
            Se il regista esiste, la sua lista di film viene aggiornata.
        '''

        if director_name not in self._catalog:
            self._catalog[director_name] = [movies] if isinstance(movies, str) else movies
            return

        movies_list: list[str] = self._catalog[director_name]

        if isinstance(movies, str):
            if movies not in movies_list:

                movies_list.append(movies)

        if isinstance(movies, list):
            for movie in movies:

                if movie not in movies_list:
                    movies_list.append(movie)

    def remove_movie(self, director_name: str, movie_name: str|list[str]|None = None, delete_director: bool = False, delete_list: bool = False) -> None:
        '''
    - Rimuove un film specifico dall'elenco dei film di un regista.
        Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.
        - movie_name = specifica film singoli o multipli.
        - delete_list = True cancella tutta la lista dei film, lasciando il regista nel catalogo.
        - delete_director = True cancella direttamente il regista con tutti i film.
        '''

        if director_name not in self._catalog:
            raise ValueError(f"{director_name} not in catalogue")

        movie_list: list[str] = self._catalog[director_name]

        if movie_name is not None and isinstance(movie_name, str) and not delete_director and not delete_list:
            if movie_name in movie_list:

                movie_list.remove(movie_name)

        elif movie_name is not None and isinstance(movie_name, list) and not delete_director and not delete_list:
            for movie in movie_name:

                if movie in movie_list:
                    movie_list.remove(movie)

        elif movie_name is None and delete_director:
            self._catalog.pop(director_name)

        elif movie_name is None and not delete_director and delete_list:
            self._catalog[director_name] = []

        elif movie_name is None and delete_director and delete_list:
            self._catalog.pop(director_name)

        else:
            raise ValueError(f"Something goes wrong:\nremove_movie(director_name: {director_name}, Movie_name: {movie_name}, delete_director: {delete_director}, delete_list: {delete_list})")

    def list_directors(self) -> str:
        '''- Elenca tutti i registi presenti nel catalogo.'''

        directors_list: list[str] = list(self._catalog.keys())

        if not directors_list:
            return "NO DIRECTOR IN CATALOGUE"

        return "DIRECTORS IN CATALOGUE:\n- " + "\n- ".join(directors_list)

    def get_movies_by_director(self, director_name: str) -> str:
        '''- Restituisce tutti i film di un regista specifico.'''

        if director_name in self._catalog:
            movies_list: list[str] = self._catalog[director_name]

            if movies_list:
                return f"{director_name}'s movies:\n- " + "\n- ".join(movies_list)

            else:
                return f"There are no movies by the director: {director_name}"

        else:
            raise ValueError(f"Director '{director_name}' not in catalogue")

    def search_movies_by_title(self, title: str) -> str:
        '''
        - Trova tutti i film che contengono una certa parola nel titolo.
            Restituisce un elenco dei registi e dei rispettivi film che contengono la parola cercata o
            un messaggio di errore se nessun film contiene la parola cercata nel titolo.
        '''

        found_movies: list[str] = []
        list_found: dict[str, list[str]] = {}

        for director, movies_list in self._catalog.items():

            for movie in movies_list:

                if title.lower() in movie.lower():
                    found_movies.append(movie)

            if found_movies:
                list_found[director] = found_movies
                found_movies = []

        final_string: str = f"Found movies with \"{title}\"\n"

        for f_director, f_movies in list_found.items():

            final_string += f"- {f_director}: " + ", ".join(f_movies) + "\n"

        return final_string if list_found else f"No results with this criteria: {title}"

    def __str__(self) -> str:
        total_movies: int = 0

        for movies_item in self._catalog.values():

            for item in movies_item:
                total_movies += 1

        info_str: str =  f"Contents of the catalog\n\nTotal directors: {len(self._catalog.keys())}\nTotal movies: {total_movies}\n"
        context_str: str = ""
        lines: list[str] = []

        for drt, lst in self._catalog.items():

            lines.append(f"+ Director: {drt}")
            if lst == []:
                lines.append("   - empty")
                continue

            for movie in lst:
                lines.append(f"    - {movie}")

            lines.append('')

        context_str += '\n'.join(lines)

        return f"{info_str}\n{context_str}"

if __name__ == "__main__":

    regista1: str = "Nolan"
    film_regista1: list[str] = ["Il cavaliere oscuro", "Inception"]
    regista1_catalogo: dict[str, list[str]] = {
        regista1: film_regista1
    }

    catalogo1: MovieCatalog = MovieCatalog(regista1_catalogo)

    catalogo1.add_movie("Kubrick", "Barry Lyndon")
    catalogo1.add_movie("Nolan", "Interstellar")
    catalogo1.add_movie("Kubrick", "Shining")

    film_regista2: list[str] = ["Il cavaliere oscuro", "Inception", "Oppenheimer"]      # con film_regista1.append("Oppenheimer") non funzionava bene
    catalogo1.add_movie(regista1, film_regista2)

    try:
        catalogo1.remove_movie("Nolan", ["Oppenheimer", "Inception"])
        # catalogo1.remove_movie("Kubrick", None, True)                                 # prima dell'aggiornameto dei parametro movie_name = None
        # catalogo1.remove_movie("Kubrick", delete_director=True)                       # OK
        # catalogo1.remove_movie("Nolan", delete_list=True)                             # OK
        # catalogo1.remove_movie("Nolan", delete_director=True)                         # OK

    except ValueError as err:
        print(f"\nEXCEPTION\n\n>> {err}\n\n")

    print(catalogo1)

    print(catalogo1.list_directors())
    print(catalogo1.get_movies_by_director("Nolan"))

    try:
        catalogo1.get_movies_by_director("Spielberg")

    except ValueError as err:
        print(f"\nEXCEPTION\n\n>> {err}\n\n")

    catalogo1.add_movie(regista1, "Il cavaliere oscuro")
    catalogo1.add_movie("Kubrick", "Il dottor stranamore")
    catalogo1.add_movie("Kubrick", "Il bacio")

    print(catalogo1.search_movies_by_title("il"))