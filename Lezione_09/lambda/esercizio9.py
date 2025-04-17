'''

Ritorna una lambda

Scrivi una funzione moltiplicatore(n) che 
ritorni una lambda che moltiplica un valore per n.

Esempio d'uso:

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20

'''

from typing import Callable

def moltiplicatore(n: int) -> Callable[[int], int]:

    return lambda x: x*n

per_due = moltiplicatore(2)
print(per_due(10))  # Output: 20