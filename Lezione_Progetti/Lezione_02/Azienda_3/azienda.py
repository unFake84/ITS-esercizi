
from typing import Self
from datetime import date

class RealGEZ(float):
	# Tipo di dato specializzato Reale >= 0
	def __new__(cls, v: float|int|str|bool|Self) -> Self:
		n: float = float.__new__(cls, v) # prova a convertire v in un float

		if n >= 0:
			return n

		raise ValueError(f"The value {n} is negative!")

class Impiegato:

    _nome: str
    _cognome: str
    _nascita: date
    _stipendio: RealGEZ
	
    def __init__(self, nome: str, cognome: str, nascita: str, stipendio: RealGEZ) -> None:
        self.set_name(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    def __str__(self) -> str:
        return f"\
                Nome: {self._nome}\n\
                Cognome: {self._cognome}\n\
                Nascita: {self._nascita}\n\
                Stipendio: {self._stipendio}\n"

    def set_name(self, new_name: str):
        self._name = new_name

    def get_name(self) -> str:
        return self._nome

    def set_cognome(self, new_last: str):
        self._cognome = new_last

    def get_cognome(self) -> str:
        return self._cognome

    def get_nascita(self):
        return self._nascita

    def set_stipendio(self, new_stipendio: RealGEZ):
        self._stipendio = new_stipendio

    def get_stipendio(self) -> RealGEZ:
        return self._stipendio