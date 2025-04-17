'''

Sintassi

Scrivi una funzione lambda che prenda un numero intero e ritorni il suo quadrato.

Esempio atteso:

quadrato = lambda x: ...

'''

from typing import Callable

quadrato:Callable[[int], int] = lambda a: a ** 2

print(quadrato(2))