# per ripristinare i json dei moduli rotti (evita puliza cache)
# import importlib
# import CodiceVolo
# import IATACode
# import Age

# importlib.invalidate_caches()
# importlib.reload(CodiceVolo)
# importlib.reload(IATACode)
# importlib.reload(Age)

# from CodiceVolo import CodiceVolo
# from IATACode import IATACode
# from Age import Age

class PartitaIva(str):

    def __new__(cls, iva: str):

        # check

        return str.__new__(cls, iva)
    
    # new si utilizza "soltanto" quando si eredita un "tipo di dato base"

class NomeClasse:
    def __init__(self, attrib):
        # Costruttore
        ...

    def __str__(self):
        # Rappresentazione leggibile (per print, str(), f-string)
        ...

    def __repr__(self):
        # Rappresentazione per debugging (opzionale)
        ...

    def __eq__(self, other):
        # Confronto per uguaglianza
        ...

    def __hash__(self):
        # Hash per set, dict, ecc.
        ...

    # Altri metodi...