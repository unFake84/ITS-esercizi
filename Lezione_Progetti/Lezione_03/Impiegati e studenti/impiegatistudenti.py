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

from all_my_types import CodiceFiscale, Genere, IntGez, PosizioneMilitare, Ruolo
from datetime import date

class Persona:
    _nome: str
    
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

        self.nome = nNome

    def getNome(self) -> str:
        return self.nome

    #COGNOME#########################################################################

    def setCognome(self, nCognome: str) -> None:
        if not isinstance(nCognome, str):
            raise ValueError("Non è una stringa!")

        self.cognome = nCognome

    def getCognome(self) -> str:
        return self.cognome

    #CF#########################################################################

    def setCF(self, cf: CodiceFiscale) -> None:
        self.cf = cf

    def getCF(self) -> CodiceFiscale:
        return self.cf

    #NASCITA#########################################################################

    def getNascita(self) -> date:
        return self._nascita

    #MATERNITA#########################################################################

    def getMaternita(self) -> IntGez |None:
        return self.maternita if self.maternita else None
    
    def addMaternita(self) -> None:
        self.maternita += 1

    #GENERE#########################################################################

    def setGenere(self, genere: Genere, maternita: IntGez|None, posMil:PosizioneMilitare|None ) -> None:
        if genere == Genere.donna and maternita is None\
            or genere == Genere.uomo and posMil is None:
            raise ValueError("Errato, deve essere conosciuta la maternità o la posizione militare")
        
        if genere == Genere.donna:
            posMil = None
            self.maternita = maternita

        if genere == Genere.uomo:
            self.maternita = None
            self.posmil = posMil

    def getGenere(self) -> Genere:
        return Genere.donna if self.maternita is not None else Genere.uomo

    #POSMIL#########################################################################

    def setPosMil(self, posmil: PosizioneMilitare) -> None:
        self.posmil = posmil