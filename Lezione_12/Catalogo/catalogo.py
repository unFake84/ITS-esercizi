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

    _catalogue: dict[str, list[str]]

    def __init__(self, catalogue: dict[str, list[str]]|None = None) -> None:
        self._catalogue = {} if catalogue is None else catalogue
    
    def add_movie(self, director_name, movies: str|list[str]) -> None:
        '''
        - Aggiunge uno o più film a un regista specifico nel catalogo.
            Se il regista non esiste, viene creato un nuovo record.
            Se il regista esiste, la sua lista di film viene aggiornata.
        '''

        if director_name not in self._catalogue.keys():
            self._catalogue[director_name] = [movies]
            return

        if isinstance(movies, str):
            for director, film_list in self._catalogue.items():

                if director == director_name:

                    if movies not in film_list:
                        film_list.append(movies)
                                                                                # DRY
        elif isinstance(movies, list):
            for director, film_list in self._catalogue.items():

                if director == director_name:
                    for movie in movies:

                        if movie not in film_list:
                            film_list.append(movie)

    def __str__(self) -> str:
        return f"Cataloque:\n{self._catalogue}"

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

    # try:
    film_regista2: list[str] = ["Il cavaliere oscuro", "Inception", "Oppenheimer"]      # con film_regista1.append("Oppenheimer") non funzionava bene
    catalogo1.add_movie(regista1, film_regista2)

    # except ValueError as err:
    #     print(f"EXCEPTION\n\n{err}")

    print(catalogo1)