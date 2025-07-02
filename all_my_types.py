from typing import Self, Any
from enum import *
import re

'''
Classe:             Parametro/i:            ?Eredetarietà:

- CAP               cap                     <-str
- CODICEFISCALE     cf                      <-str
- CONTINENTE        auto()                  <-StrSnum
- DENARO            imp, val(Valuta)
- EMAIL             v                       <-str
- FLOATDENARO       imp, val                <-float
- GENERE            auto()                  <-StrEnum
- INDIRIZZO         via civ cap
- INDIRIZZO2        via civ
- INTGE1900         v                       <-int
- INTGEZ            v						<-int
- POSIZIONEMILITARE -						<-StrEnum
- REALGEZ           v                       <-float
- RUOLO				-						<-StrEnum
- TELEFONO          tel                     <-str
- VALUTA            v                       <-str
- VOTO              v                       <-int
'''

class CAP(str):
	def __new__(cls, cap: str) -> Self:
		if re.fullmatch(r'^\d{5}$', cap):
			return super().__new__(cls, cap)
		
		raise ValueError(f"La stringa '{cap}' non è un CAP italiano valido!")

class CodiceFiscale(str):
	# Gli oggetti di questa classe *sono* stringhe
	#  che rispettano il formato del codice fiscale

	def __new__(cls, cf: str) -> Self:
		cff: str = cf.upper().strip() # rendo la stringa maiuscola e senza spazi iniziali e finali
		if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
			return super().__new__(cls, cff)
		
		raise ValueError(f"La stringa '{cff}' non è un codice fiscale italiano valido!")

class Continente(StrEnum):

    asia = auto()
    europa = auto()
    america = auto()
    africa = auto()
    antartide = auto()

class Denaro:
	# Rappresenta il tipo di dato concettuale composto
	#  con i seguenti campi:
	# 	- importo: Reale
	# 	- valuta: Valuta
	_importo: float
	_valuta: "Valuta"

	def __init__(self, imp: float, val: "Valuta") -> None:
		self._importo = imp
		self._valuta = val

	def importo(self) -> float:
		return self._importo

	def valuta(self) -> "Valuta":
		return self._valuta

	def __str__(self) -> str:
		return f"{self.importo()} {self.valuta()}"

	def __repr__(self) -> str:
		return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"

	def __hash__(self) -> int:
		return hash( (self.importo(), self.valuta()) )

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, type(self)) or \
			hash(self) != hash(other):
			return False
		return self.importo() == other.importo() and \
			self.valuta() == other.valuta()

	def __add__(self, other: Self) -> Self:
		"""
		Somma self ad un'altra istanza di Denaro,
		 ma solo se la valuta è la stessa.
		Restituisce una nuova istanza di Denaro
		"""
		if self.valuta() != other.valuta():
			raise ValueError(f"Non posso sommare importi di valute diverse: '{self.valuta()}' e '{other.valuta()}'")
		
		somma: float = self.importo() + other.importo()
		return Denaro(somma, self.valuta())

class Email(str):
	def __new__(cls, v: str | Self) -> Self:
		if re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 
, v):
			return super().__new__(cls, v)
		raise ValueError(f"{v} non è un indirizzo email valido")

class FloatDenaro(float):
	_valuta: "Valuta"

	def __new__(cls, imp: float|int|str, val: "Valuta") -> Self:
		d = super().__new__(cls, imp)
		
		d._valuta = val
		return d

	def importo(self) -> float:
		return self.real

	def valuta(self) -> "Valuta":
		return self._valuta

	def __str__(self) -> str:
		return f"{self.importo()} {self.valuta()}"

	def __repr__(self) -> str:
		return f"Denaro: {self.importo()} unità di valuta {self.valuta()}"

	def __hash__(self) -> int:
		return hash( (self.importo(), self.valuta()) )

	def __eq__(self, other: Any) -> bool:
		if not isinstance(other, type(self)) or \
			hash(self) != hash(other):
			return False
		return self.importo() == other.importo() and \
			self.valuta() == other.valuta()

	def __add__(self, other: Self) -> Self:
		"""
		Somma self ad un'altra istanza di Denaro,
		 ma solo se la valuta è la stessa.
		Restituisce una nuova istanza di Denaro
		"""
		if self.valuta() != other.valuta():
			raise ValueError(f"Non posso sommare importi di valute diverse: '{self.valuta()}' e '{other.valuta()}'")

		somma: float = self.importo() + other.importo()
		return FloatDenaro(somma, self.valuta())

	def __sub__(self, other: Self) -> Self:
		return self + FloatDenaro(-other, other.valuta())

class Genere(StrEnum):

    uomo = auto()
    donna = auto()

class Indirizzo:
	_via:str
	_civico: str
	_cap: CAP

	def __init__(self, via:str, civico:str, cap:CAP) -> None:

		self._via:str = via

		if not re.search("^[0-9]+[a-zA-Z]*$", civico):
			raise ValueError(f"value for civico '{civico}' not allowed")
		self._civico:str = civico
		self._cap = cap

	def via(self)->str:
		return self._via
	def civico(self)->str:
		return self._civico

	def cap(self) -> CAP:
		return self._cap

	def __repr__(self) -> str:
		return f"Indirizzo(via={self.via()}, civico={self.civico()}, cap={self.cap()})"

	def __str__(self)->str:
		return f"{self.via()} {self.civico()} -- {self.cap()}"

	# class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
	def __hash__(self)->int:
		return hash( (self.via(), self.civico(), self.cap()) )

	def __eq__(self, other:Any)->bool:
		if other is None or \
				not isinstance(other, type(self)) or \
				hash(self) != hash(other):
			return False
		return (self.via(), self.civico(), self.cap()) == (other.via(), other.civico(), other.cap())

class Indirizzo2:

    _via: str
    _civ: int

    def __init__(self, via: str, civ: int) -> None:
        self._via= via
        self._civ = civ

    def via(self) -> str:

        return self._via
    
    def civico(self) -> int:

        return self._civ
    
    def __hash__(self) -> int:

        return hash((self._via, self._civ))
    
    def __eq__(self, other: Any) -> bool:
        
        if not isinstance(other, type(self)) or \
            hash(self) != hash(other):
            
            return False
        
        return self._via == other._via and self._civ == other._civ

class IntGE1900(int):
	# Tipo di dato specializzato Intero >= 1900
	def __new__(cls, v: float|int|str|bool|Self) -> Self:
		n: int = super().__new__(cls, v) # prova a convertire v in un int

		if n >= 1900:
			return n

		raise ValueError(f"Il valore {n} è minore di 1900!")

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

class RealGEZ(float):
	# Tipo di dato specializzato Reale >= 0
	def __new__(cls, v: float|int|str|bool|Self) -> Self:
		n: float = float.__new__(cls, v) # prova a convertire v in un float

		if n >= 0:
			return n

		raise ValueError(f"Il valore {n} è negativo!")
	
class Ruolo(StrEnum):
	SEGRETARIO = auto()
	DIRETTORE = auto()
	PROGETTISTA = auto()

class Telefono(str):
	def __new__(cls, tel: str | Self) -> Self:
		if re.fullmatch(r'^\d{10}$', tel):
			return super().__new__(cls, tel)
		raise ValueError(f"{tel} non è un numero di telefono italiano valido")

class Valuta(str):
	def __new__(cls, v: str) -> Self:
		if re.fullmatch(r'^[A-Z]{3}$', v):
			return super().__new__(cls, v)
		
		raise ValueError(f"La stringa '{v}' non è un codice valido per una valuta!")

class Voto(int):

    def __new__(cls, v: int|float|Self) -> Self:

        if v < 18 or v > 30:

            raise ValueError(f"Value v == {v} must be between 18 and 30")
        
        return int.__new__(cls, v)
    
    def __add__(self, other: Self) -> Self:

        return Voto(int(self) + int(other))

if __name__ == "__main__":

    print(Genere.uomo.upper())
    print(type(Genere.donna))
    print(Continente.america.capitalize())

    v18: Voto = Voto(18)
    type(v18)
    l = [Voto(18), Voto(21), Voto(30)]
    print(sum(l))

    i1: Indirizzo2 = Indirizzo2(via= "Viale Cesare Pavese", civ= 305)