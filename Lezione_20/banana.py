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
    
    # new si utilizza "soltanto" quando si eredita un tipo di dato base