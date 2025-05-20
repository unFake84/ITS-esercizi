class PartitaIva(str):

    def __new__(cls, iva: str):

        # check

        return str.__new__(cls, iva)
    
    # new si utilizza "soltanto" quando si eredita un tipo di dato base