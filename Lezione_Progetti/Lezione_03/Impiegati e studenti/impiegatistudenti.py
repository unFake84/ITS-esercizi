# class Persona che aggregga PosizioneMilitare come opzionale
# class Impiegato
# class Studente
# class Progetto

# class Resp_prog(link)
####tipididato####
# CodiceFiscale
# Data
# Genere
# Ruolo
# Posizione militare
# Maternità
# Matricola
# IntGez
# RealGez

from progetti_types import CodiceFiscale, Genere, IntGez, PosizioneMilitare, Ruolo
from datetime import date

class Persona:
    _nome: str
    _cognome: str
    _cf: CodiceFiscale
    _nascita: date
    _maternita: IntGez
    _genere: Genere
    _posMil: PosizioneMilitare
    
    ##########################################################################
    #INIT#########################################################################

    def __init__(

            self,
            nome: str,
            cognome: str,
            cf: CodiceFiscale,
            nascita: date,
            maternita: IntGez | None,
            genere: Genere,
            posMil: PosizioneMilitare | None

            ) -> None:

        self.setNome(nome)
        self.setCognome(cognome)
        self.setCF(cf)
        self._nascita = nascita
        self.setGenere(genere, maternita, posMil)
        

    #NOME#########################################################################

    def setNome(self, nNome: str) -> None:
        if not isinstance(nNome, str):
            raise ValueError("Non è una stringa!")

        self._nome = nNome

    def getNome(self) -> str:
        return self._nome

    #COGNOME#########################################################################

    def setCognome(self, nCognome: str) -> None:
        if not isinstance(nCognome, str):
            raise ValueError("Non è una stringa!")

        self._cognome = nCognome

    def getCognome(self) -> str:
        return self._cognome

    #CF#########################################################################

    def setCF(self, cf: CodiceFiscale) -> None:
        self._cf = cf

    def getCF(self) -> CodiceFiscale:
        return self._cf

    #NASCITA#########################################################################

    def getNascita(self) -> date:
        return self._nascita

    #MATERNITA#########################################################################

    def getMaternita(self) -> IntGez |None:
        return self._maternita if self._maternita else None
    
    def addMaternita(self) -> None:
        self._maternita += 1

    #GENERE#########################################################################

    def setGenere(self, genere: Genere, maternita: IntGez|None, nposMil:PosizioneMilitare|None ) -> None:
        if genere == Genere.donna and maternita is None\
            or genere == Genere.uomo and posMil is None:
            raise ValueError("Errato, deve essere conosciuta la maternità o la posizione militare")
        
        if genere == Genere.donna:
            posMil = None
            self._maternita = maternita

        if genere == Genere.uomo:
            self._maternita = None
            self._posmil = nposMil

    def getGenere(self) -> Genere:
        return Genere.donna if self._maternita is not None else Genere.uomo

    #POSMIL#########################################################################

    def setPosMil(self, nposmil: PosizioneMilitare) -> None:
        self._posmil = nposmil

    def getPosMil(self) -> PosizioneMilitare | str:
        return self._posMil if self._posMil else "Nessuna posizione registrata"