# from __future__ import annotations
from datetime import date
from all_my_types import RealGZ, RealGEZ, IntGez
from enum import *
from abc import *

class Utente(ABC):

    username: str
    registrazione: date

    @abstractmethod # le classi devono per forza reiplementare l'init
    def __init__( self, username: str, registrazione: date ) -> None:
        self.setUsername( username )
        self.registrazione = registrazione

    def setUsername( self, setterUS: str ) -> None:
        self.username = setterUS

    def getUsername( self ) -> str:
        return self.username
    
    def getRegistrazione( self ) -> date:
        return self.registrazione
    
class Privato(Utente):

    def __init__( self, username, registrazione ) -> None:
        super().__init__( username, registrazione )

class Bid:

    istante: date

    def __init__( self, istante: date )  -> None:
        self.istante = istante

    def getIstante( self ) -> date:
        return self.istante

class Condizione( StrEnum ):

    ottimo = auto()
    buono = auto()
    discreto = auto()
    da_sistemare = auto()


class PostOggetto(ABC):

    descrizione: str
    pubblicazione: date # IMM
    anni_garanzia: IntGez
    prezzo: RealGEZ
    is_nuovo: bool # IMM
    condizione: Condizione | None # IMM[0..1]

    @abstractmethod
    def __init__(

        self,
        descrizione: str,
        pubblicazione: date,
        anni_garanzia: IntGez,
        prezzo: RealGEZ,
        is_nuovo: bool,
        condizione: Condizione = None

    ) -> None:

        self.setDescrizione( descrizione )
        self.pubblicazione = pubblicazione
        self.setAnniGar( anni_garanzia )
        self.setPrezzo( prezzo )
        self.is_nuovo = is_nuovo
        self.condizione = condizione

    def setDescrizione( self, setDesc: str ) -> None:
        self.descrizione = setDesc

    def getDescrizione( self ) -> str:
        return self.descrizione
    
#-------------------------------------------------------------------------

    def getPubblicazione( self ) -> date:
        return self.pubblicazione
    
#-------------------------------------------------------------------------

    def setAnniGar( self, setAG ) -> None:
        self.anni_garanzia = setAG

    def getAnniGar( self ) -> IntGez:
        return self.anni_garanzia
    
#-------------------------------------------------------------------------

    def setPrezzo( self, setP: RealGEZ) -> None:
        self.prezzo = setP

    def getPrezzo( self ) -> RealGEZ:
        return self.prezzo
    
#-------------------------------------------------------------------------
    
    def setIs_nuovo( self, setIN) -> None:
        self.is_nuovo = setIN

    def getIs_nuovo( self ) -> bool:
        return self.is_nuovo
    
#-------------------------------------------------------------------------

    def setCondizione( self, setC: Condizione = None ) -> None:
        self.condizione = setC

    def getCondizione( self ) -> Condizione:
        return self.condizione
    
class Asta(PostOggetto):

    prezzo_bid: RealGZ
    scadenza: date
    #_bids: dict[Bid, asta_bid._link] = ?

    def __init__(self, descrizione, pubblicazione, anni_garanzia, prezzo, is_nuovo, prezzo_bid: RealGZ, scadenza: date, condizione = None):

        super().__init__(descrizione, pubblicazione, anni_garanzia, prezzo, is_nuovo, condizione)

        self.setPrezzoBid( prezzo_bid )
        self.setScadenza( scadenza )

    def setPrezzoBid( self, setPB: RealGEZ ) -> None:
        # implementare qui astabidlink?!?!?!!?
        self.prezzo_bid = setPB

    def getPrezzoBid( self ) -> RealGEZ:
        return self.prezzo_bid
    
    def setScadenza( self, setS: date ) -> None:
        self.scadenza = setS
    
    def getScadenza( self ) -> date:
        return self.scadenza
    
class asta_bid:
    pass

class bid_ut:
    pass