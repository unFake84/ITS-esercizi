from typing import Self, Any
from enum import *
import re

'''
Classe:             Parametro/i:            ?Eredetarietà:

- CODICEFISCALE     cf                      <-str
- GENERE            auto()                  <-StrEnum
- INTGEZ            v						<-int
- POSIZIONEMILITARE -						<-StrEnum
- RUOLO				-						<-StrEnum
'''

class CodiceFiscale(str):
	# Gli oggetti di questa classe *sono* stringhe
	#  che rispettano il formato del codice fiscale

	def __new__(cls, cf: str) -> Self:
		cff: str = cf.upper().strip() # rendo la stringa maiuscola e senza spazi iniziali e finali
		if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
			return super().__new__(cls, cff)
		
		raise ValueError(f"La stringa '{cff}' non è un codice fiscale italiano valido!")

class Genere(StrEnum):

    uomo = auto()
    donna = auto()

class IntGez(int):
	# Tipo di dato specializzato Intero >= 0
	def __new__(cls, v:int | float | str | bool | Self) -> Self:
		n: int = int.__new__(cls, v) # prova a convertire v in un int

		if n >= 0:
			return n
		
		raise ValueError(f"Il valore {n} è negativo!")
	
class PosizioneMilitare(StrEnum):
	GENERALE = "Generale"
	COLONELLO = "Colonello"
	SERGENTE = "Sergente"
	SOLDATO = "Soldato"
	
class Ruolo(StrEnum):
	SEGRETARIO = auto()
	DIRETTORE = auto()
	PROGETTISTA = auto()