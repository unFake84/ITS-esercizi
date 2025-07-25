from datetime import date
from azienda_types import *

class Impiegato:

    _nome: str
    _cognome: str
    _nascita: date
    _stipendio: RealGEZ

    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ) -> None:
        if not isinstance(nome, str) or not isinstance(cognome, str) or not isinstance(nascita, Date) or not isinstance(stipendio, RealGEZ):

            raise TypeError("The type entered is incorrect.")
        
        self.set_name(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    def __str__(self) -> str:
        return (
            f"Name: {self._nome}\n"
            f"Lastname: {self._cognome}\n"
            f"Birthday: {self._nascita}\n"
            f"Salary: {self._stipendio}\n"
            )
    
    # def __eq__(self, other: Self) -> bool:        
    #     return (self._nome == other._nome and
    #         self._cognome == other._cognome and
    #         self._nascita == other._nascita and
    #         self._stipendio == other._stipendio)

    def __hash__(self) -> int:
        return hash((self._nome, self._cognome, self._nascita, self._stipendio))

    def set_name(self, new_name: str) -> None:
        self._nome = new_name

    def get_name(self) -> str:
        return self._nome

    def set_cognome(self, new_last: str) -> None:
        self._cognome = new_last

    def get_cognome(self) -> str:
        return self._cognome

    def get_nascita(self) -> date:
        return self._nascita

    def set_stipendio(self, new_stipendio: RealGEZ) -> None:
        self._stipendio = new_stipendio

    def get_stipendio(self) -> RealGEZ:
        return self._stipendio
    
class Dipartimento:

    _nome: str
    _telefoni: set[str]
    _indirizzo: Indirizzo

    def __init__(self, nome: str, telefono: set[str], indirizzo: Indirizzo|None) -> None:
        if not isinstance(nome, str) or not isinstance(telefono, set) or indirizzo is not None and not isinstance(indirizzo, Indirizzo):

            raise TypeError("The type entered is incorrect.")

        self.set_name(nome)
        self._telefoni = set()
        self.set_telefono(telefono)
        self.set_indirizzo(indirizzo)

    def __str__(self):

        return (
            f"Name: {self._nome}\n"
            f"Tel: {self._telefoni}\n"
            f"Address: {self._indirizzo}\n"
        )

    # def __eq__(self, other: Self) -> bool:
    #     if self._indirizzo and other._indirizzo:

    #         return (self._nome == other._nome and
    #                 self._telefoni == other._telefoni and
    #                 self._indirizzo == other._indirizzo)

    #     else:

    #         return (self._nome == other._nome and
    #                 self._telefoni == other._telefoni)

    # def __hash__(self):
    #     telefoni_tuple: tuple = tuple(self._telefoni)

    #     if self._indirizzo:

    #         return hash((self._nome, telefoni_tuple, self._indirizzo))

    #     else:

    #         return hash((self._nome, telefoni_tuple))

    def set_name(self, newname2: str) -> None:
        if not isinstance(newname2, str):

            raise ValueError("The type entered is incorrect.")

        self._nome = newname2

    def get_name(self) -> str:

        return self._nome

    def set_telefono(self, newtel: set[str]) -> None:
        if not isinstance(newtel, set):

            raise ValueError("The type entered is incorrect.")

        elif newtel == {}:

            raise ValueError("Cannot be emtpy.")

        for check in newtel:
            if not isinstance(check, str) or check == "":

                raise ValueError(f"{check} not supported" if check != "" else "Cannot be empty")

        self._telefoni = newtel

    def get_telefono(self) -> frozenset[str]:

        return frozenset(self._telefoni)

    def add_telefono(self, add: str) -> None:
        self._telefoni.add(add)

    def remove_telefono(self, remove: str) -> None:
        if remove not in self.set_telefono():
            raise RuntimeError(f"{remove} is not in database.")

        elif len(self.get_telefono()) == 1:
            raise RuntimeError("Cannot be empty.")

        elif len(self.set_telefono()) > 1:

            self._telefoni.remove(remove)

    def set_indirizzo(self, newaddr: Indirizzo|None) -> None:
        if newaddr is None:

            self._indirizzo = None

        elif not isinstance(newaddr, Indirizzo):

            raise ValueError("The type entered is incorrect.")

        else:

            self._indirizzo = newaddr

    def get_indirizzo(self) -> Indirizzo:

        return self._indirizzo

class Progetto:

    _nome: str
    _budget: RealGEZ

    def __init__(self, nome: str, budget: RealGEZ) -> None:

        if not isinstance(nome, str):

            raise ValueError("The type entered is incorrect.")

        self.set_nome(nome)
        self.set_budget(budget)

    def __str__(self):

        return (
             f"Name: {self._nome}\n"
             f"Budget: {self._budget}\n"
        )

    def __eq__(self, other: Self):

        return (self._nome == other._nome and
                self._budget == other._budget)

    def __hash__(self):

        return hash((self._nome, self._budget))

    def set_nome(self, newname: str) -> None:
        if not isinstance(newname, str):

            raise ValueError("The type entered is incorrect.")

        self._nome = newname

    def get_nome(self) -> str:

        return self._nome

    def set_budget(self, newbudget: RealGEZ) -> None:
        if not isinstance(newbudget, RealGEZ):

            raise ValueError("The type entered is incorrect.")

        self._budget = newbudget

    def get_budget(self) -> RealGEZ:

        return self._budget
    
class Citta:
    def __init__(self, nome: str) -> None:
        if not isinstance(nome, str):

            raise ValueError("The type entered is incorrect.")