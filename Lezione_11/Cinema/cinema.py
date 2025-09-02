'''
Sistema di Prenotazione Cinema

Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema.
Il cinema ha diverse sale, ognuna con un diverso film in programmazione.
Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

'''

class Film:
    '''
    Rappresenta un film con titolo e durata.
    '''

    titolo: str
    durata: int

    def __init__(self, titolo: str, durata: int) -> None:
        self.set_titolo(titolo)
        self.set_durata(durata)

    def set_titolo(self, t: str) -> None:
        self.titolo = t

    def set_durata(self, d: int) -> None:
        if d < 1:

            raise ValueError(f"{self.get_titolo()} duration cannot be less than 1")

        self.durata = d

    def get_titolo(self) -> str:
        return self.titolo

    def get_durata(self) -> int:
        return self.durata

    def __str__(self) -> str:
        string: str = f"{'Title: ':<19}{self.titolo}\n{'Length: ':<19}{self.get_durata()} min"

        return string

class Sala:
    '''
    Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

    Metodi:
        - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
        - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
    '''

    id: str
    film_inprog: Film
    tot_posti: int
    posti_pren: int

    def __init__(self, id: str, film_inprog: Film, tot_posti: int) -> None:
        self.set_id(id)
        self.set_film_inprog(film_inprog)
        self.set_tot_posti(tot_posti)

    def set_id(self, set_id: str) -> None:
        self.id = set_id

    def set_film_inprog(self, film: Film) -> None:
        self.film_inprog = film

    def set_tot_posti(self, posti: int) -> None:
        if posti <= 0:

            raise ValueError("There must be at least one seat")

        self.posti_pren = 0
        self.tot_posti = posti

    def get_id(self) -> str:
        return self.id

    def get_film_inprog(self) -> Film:
        return self.film_inprog

    def get_tot_posti(self) -> int:
        return self.tot_posti

    def prenota_posto(self, num_posto: int) -> str:
        if self.tot_posti - self.posti_pren - num_posto < 0:

            raise ValueError(f"It's impossible to reserve seats, {self.posti_disp()} seats remain")

        self.posti_pren  += num_posto
        return "Seats booked correctly"

    def posti_disp(self) -> int:
        posti: int = self.tot_posti - self.posti_pren

        return posti

    def __str__(self) -> str:
        stringa: str = f"{'Movie screen: ':<19}{self.get_id()}\n{'*'*40}\n"\
                    f"{'Total seats: ':<19}{self.get_tot_posti()}\n"\
                    f"{self.get_film_inprog()}\n"\
                    f"{'Seats available: ':<19}{self.posti_disp()}\n"

        return stringa

class Cinema:
    '''
    Gestisce le operazioni legate alla gestione delle sale.

    Metodi:
        - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
        - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
    '''

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        self.lista_sale: list[Sala] = []

    def set_nome(self, n: str) -> None:
        self.nome = n

    def get_nome(self) -> str:
        return self.nome

    def aggiungi_sala(self, sala: Sala) -> None:
        if sala in self.lista_sale:

            raise ValueError("Movie screen already exists")

        self.lista_sale.append(sala)

    def prenota_film(self, titolo_film: Film, num_posti: int) -> str:
        for sala in self.lista_sale:

            if sala.get_film_inprog() == titolo_film:
                if sala.posti_disp() < num_posti:

                    return f"Impossible to reserve seats, {sala.posti_disp()} avaiable"

                sala.prenota_posto(num_posti)
                return f"Confirmed {num_posti} seats for the \"{titolo_film.get_titolo()}\" show"

        return "Movie not in catalogue"

    def __str__(self) -> str:
        return "#" * 48 + f"\n\n{self.nome}\n\n" + '\n'.join([str(n) for n in self.lista_sale]) + "\n"+ "#" * 48

if __name__ == "__main__":

    try:
        # TEST FILM
        film1: Film = Film("Interstellar", 139)
        film2: Film = Film("Barry Lyndon", 187)

        # TEST SALA
        sala1: Sala = Sala("01", film1, 40)
        sala1.prenota_posto(5)
        sala1.prenota_posto(8)
        #vvvvvvvvvvvvvvvvvvvv#
        # TEST CINEMA
        sala2: Sala = Sala("02", film2, 40)
        sala2.prenota_posto(8)
        sala2.prenota_posto(2)
        sala2.prenota_posto(4)

        cinema1: Cinema = Cinema("Serafino Gubbio's Village")
        cinema1.aggiungi_sala(sala1)
        cinema1.aggiungi_sala(sala2)
        # cinema1.aggiungi_sala(sala2)


        # istanze
        ##########################################################################
        # print


        # PRINT FILM
        # print(film1)
        # print(film2)

        # PRINT SALA
        # print(f"Posti disponibili: {sala1.posti_disp()}\nFilm: {film1.get_titolo()}")
        # print(sala1)

        # PRINT CINEMA
        print(cinema1)

        print(cinema1.prenota_film(film1, 6), '\n')
        print(cinema1.prenota_film(film1, 8), '\n')
        print(cinema1.prenota_film(film2, 12), '\n')

    except ValueError as err:
        print("EXCEPTIONS:\n")
        print(err)

    print(cinema1)