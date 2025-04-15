'''

Verifica se una stringa è un numero intero

1.
    Scrivi una funzione is_integer(s) che restituisce True
    se la stringa è un numero intero (positivo o negativo),
    
2.
    False altrimenti.

                            Esempio:

                            is_integer("123")      # True
                            is_integer("-456")     # True
                            is_integer("12.3")     # False

'''

import sys

def is_integer(s: str) -> bool:

    if 're' not in sys.modules:

        import re

    if re.fullmatch('-?\d+', s) == None:

        return False
    
    else:

        return True
    
    # return False if re.fullmatch('-?\d+', s) == None else True
    # return re.fullmatch('-?\d+', s) is not None