'''
### Test con codice driver
Scrivere un codice driver in cui si crea una lista di 10 film,
di cui 5 sono film d'azione, 4 sono commedie e 1 è un film drammatico.
Successivamente:

    Creare un oggetto Noleggio.
    Stampare: "Quale film vuoi nolleggiare?"
    Simulare il noleggio di un film di un primo cliente.
    Simulare il noleggio di un secondo film sempre da parte del primo cliente.
    Simulare il noleggio del film precedente da parte di un secondo cliente.
    (assicurarsi che il codice avvisi il secondo cliente che il film richiesto non è disponibile).

    Simulare il noleggio di un terzo film da parte del secondo cliente.
    Simulare il reso del secondo film noleggiato dal primo cliente.
    Stampare la lista dei film disponibili in negozio.
'''

from movie_genre import *
from noleggio import Noleggio

film1: Film = Azione(100, "True Lies")
film2: Film = Azione(119, "Terminator 2 - Il giorno del giudizio")
film3: Film = Azione(189, "Live Action Hero")
film4: Film = Azione(459, "Predator")
film5: Film = Azione(756, "Arma Letale 4")
film6: Film = Commedia(304, "Pretty Woman")
film7: Film = Commedia(176, "Tutto può succedere")
film8: Film = Commedia(399, "Notting Hill")
film9: Film = Commedia(58, "Il diario di Bridget Jones")
film10: Film = Drama(248, "Vi presento Joe Black")

database_di_films: list[Film] = [film1, film2, film3, film4, film5, film6, film7, film8, film9, film10]

noleggio: Noleggio = Noleggio(database_di_films)
print(f"- Quale film vuoi noleggiare?\n- E'disponibile {film3.getTitle()}?")
noleggio.rentAMovie(film3, 999)